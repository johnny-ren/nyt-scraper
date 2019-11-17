import requests, bs4

res = requests.get("https://www.nytimes.com/section/opinion")

res.raise_for_status()

raw_text = bs4.BeautifulSoup(res.text)

#Scrape the authors for the day
header_authors = raw_text.find_all('span', itemprop='name')
body_authors = raw_text.find_all('span', {'class': 'css-1n7hynb'})

for elem in header_authors:
    print(elem.contents)

for elem in body_authors:
    print(elem.contents)

