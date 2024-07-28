import requests # sending request to the website (url) and getting response
from bs4 import BeautifulSoup # getting specific content and making it readable
import pandas as pd # for exporting it to csv or excel file
import re # for regular expressions

URL = 'https://www.yelp.com/search?find_desc=Home+Developers&find_loc=San+Francisco%2C+CA%2C+USA&mapsize=393%2C208'

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36','Accept-language':'en-US, en;q=0.5'})


webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content,'html.parser')



# scrapping data from front page

data = []
divs = soup.find_all('div', attrs={'class':'mainAttributes__09f24__n3n6Q arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG y-css-1iy1dwt'})
# divs = soup.find_all('div', attrs={'class':'businessName__09f24__HG_pC y-css-ohs7lg'})
for i in range (len(divs)):
    reviews =int(re.search(r'\d+',  divs[i].find('span', attrs={'class':'y-css-wfbtsu'}).text).group())
    rating = divs[i].find('span', attrs={'class':'y-css-jf9frv'}).text
    tags = []
    tags_element = divs[i].findAll('span', attrs={'class':'y-css-1cn4gbs'})
    for j in range(len(tags_element)):
        tags.append(tags_element[j].text)
    h3_element = divs[i].find('h3', attrs={'class':'y-css-hcgwj4'})
    if h3_element:
        heading = h3_element.text
        a_element = h3_element.find('a')
        href = a_element.get('href')
        href = 'https://www.yelp.com' + href
    data.append({
        'Reviews': reviews,
        'Rating': rating,
        'Tags': tags,
        'Heading': heading,
        'Link': href
    })
df = pd.DataFrame(data)
df.to_csv('yelp_data_frontPage.csv', index=False)
print("Data scraped and saved successfully to yelp_data_frontPage.csv!")
        