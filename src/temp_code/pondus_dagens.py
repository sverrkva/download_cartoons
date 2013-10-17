import urllib.request
from bs4 import BeautifulSoup as BS
import datetime

# Download picture from this webpage
url = "http://www.dagbladet.no/tegneserie/pondus/"

# Download the html-code from the given url and convert to "BS"
opener = urllib.request.FancyURLopener({})
f = opener.open(url)
html_code = f.read()
soup = BS(html_code)

# Find the url to the right picture
pondus_picture = soup.find(id="pondus-stripe")
pondus_picture_url = pondus_picture['src']

# Make a new name for the file with timestamp
today = str(datetime.date.today())
pondus_string_array = ["pictures/","pondus_DB_",today,".jpg"]
pondus_tag = ''.join(pondus_string_array)

# Downlad the picture
urllib.request.urlretrieve(pondus_picture_url, pondus_tag)
