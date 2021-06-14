from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

'''print(soup)
print(soup.prettify())

## finding contents of a page by using the attributes directly-will return the first match
match = soup.title
print(match)

match = soup.title.text
print(match)

match = soup.div
print(match)

## find() - To grab specific content
match = soup.find('div')
print(match)

match = soup.find('div', class_ = 'footer')
print(match)
'''
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.p.text
    print(summary)
    
    print()