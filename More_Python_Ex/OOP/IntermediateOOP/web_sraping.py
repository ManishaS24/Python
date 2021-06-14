from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

for article in soup.find_all('article'):
    # print(article.prettify())
    
    headline = article.h2.a.text
    print('Article Headline:',headline)
    
    summary = article.find('div', class_='entry-content').p.text
    print('Article Summary:',summary)
    
    if article.find('iframe', class_='youtube-player') is None:
        continue
    else:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        #print(vid_src)
    
    vid_id = vid_src.split('/')[4].split('?')[0]
    print(vid_id)
    
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print('Video Link:',yt_link)
    
    print()