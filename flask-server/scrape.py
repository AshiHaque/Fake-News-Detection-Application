from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.bbc.co.uk/news/world-europe-64664560"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="ssrcss-q03fby-ContainerWithSidebarWrapper e1jl38b40")

with open('article.csv', 'w', encoding='utf8', newline='') as a:
    thewriter = writer(a)
    header = ['title', 'text']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h1', class_="ssrcss-15xko80-StyledHeading e1fj1fc10").text
        paragraphs = list.find_all('p', class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")
        text = "".join([p.text for p in paragraphs])

        info = [title, text]
        thewriter.writerow(info)