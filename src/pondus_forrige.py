import urllib.request
from bs4 import BeautifulSoup as BS
from datetime import date, timedelta
import re

###### Script for downloading previous pondus cartoons from Dagbladet ########

## Note: To make the script run you have to make a directory named pictures in the location of the script


# Download picture from this webpage
url = "http://www.dagbladet.no/tegneserie/pondus/"
opener = urllib.request.FancyURLopener({})

# Download the html-code from the given url and convert to "BS"
f = opener.open(url)
html_code = f.read()
soup = BS(html_code)

for i in range(14):
    # Finding the url from the day before. Using the last element of the for-loop
    for link in soup.find_all('a',{'class': 'db-button type3'}):
        prev = link.get('href')

    prev_string_array = [url,prev]
    new_url = ''.join(prev_string_array)

    # Download the html-code from the new url and convert to "BS"
    f = opener.open(new_url)
    html_code = f.read()
    soup = BS(html_code)

    # Find the url to the right picture
    pondus_picture = soup.find(id="pondus-stripe")
    pondus_picture_url = pondus_picture['src']

    # Make a new name for the file with timestamp
    date = date.today() - timedelta(int(i+1))
    date2 = str(date)
    pondus_string_array = ["pictures/","pondus_DB_",date2,".jpg"]
    pondus_tag = ''.join(pondus_string_array)

    # Downlad the picture
    urllib.request.urlretrieve(pondus_picture_url, pondus_tag)
