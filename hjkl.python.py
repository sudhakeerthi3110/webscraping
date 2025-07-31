import requests
from bs4 import BeautifulSoup
import csv

# Target Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_programming_languages"

# Send GET request
response = requests.get(url)

# Check request
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Container: all divs with class 'div-col'
    containers = soup.find_all('div', class_='div-col')

    data = []

    for container in containers:
        links = container.find_all('a')
        for link in links:
            name = link.get_text(strip=True)
            href = link.get('href')
            full_url = f"https://en.wikipedia.org{href}" if href.startswith('/wiki/') else href
            data.append([name, full_url])

    # Save to CSV
    with open('programming_languages.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Language", "Wikipedia URL"])
        writer.writerows(data)

    print(f" {len(data)} programming languages saved to 'programming_languages.csv'")
else:
    print(" Failed to fetch Wikipedia page. Status code:", response.status_code)
