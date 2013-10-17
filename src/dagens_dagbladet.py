import urllib.request
from bs4 import BeautifulSoup as BS
import datetime


### DAGBLADET ###
def download_DB (url, cart_id, storing_name):

    # Download the html-code from the given url and convert to "BS"
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    html_code = f.read()
    soup = BS(html_code)

    # Find the url to the right picture
    picture = soup.find(id=cart_id)
    picture_url = picture['src']

    # Make a new name for the file with timestamp
    today = str(datetime.date.today())
    string_array = ["pictures/",storing_name,today,".jpg"]
    tag = ''.join(string_array)

    # Downlad the picture
    urllib.request.urlretrieve(picture_url, tag)

    print ("Finished " + tag)
   
    return





### -------- DAGBLADET --------- ###

### Pondus ###
url = "http://www.dagbladet.no/tegneserie/pondus/"
cart_id = "pondus-stripe"
storing_name = "pondus_DB_"
download_DB (url, cart_id, storing_name)

### Lunch ###
url = "http://www.dagbladet.no/tegneserie/lunch/"
cart_id = "lunch-stripe"
storing_name = "lunch_DB_"
download_DB (url, cart_id, storing_name)

### Nemi ###
url = "http://www.dagbladet.no/tegneserie/nemi/"
cart_id = "nemi-stripe"
storing_name = "nemi_DB_"
download_DB (url, cart_id, storing_name)

### Storefri ###
url = "http://www.dagbladet.no/tegneserie/gjesteserie/storefri/"
cart_id = "gjesteserie/storefri-stripe"
storing_name = "storefri_DB_"
download_DB (url, cart_id, storing_name)

### Rocky ###
url = "http://www.dagbladet.no/tegneserie/rocky/"
cart_id = "rocky-stripe"
storing_name = "rocky_DB_"
download_DB (url, cart_id, storing_name)

### Fagprat ###
url = "http://www.dagbladet.no/tegneserie/fagprat/"
cart_id = "fagprat-stripe"
storing_name = "fagprat_DB_"
download_DB (url, cart_id, storing_name)

### Zelda ###
url = "http://www.dagbladet.no/tegneserie/zelda/"
cart_id = "zelda-stripe"
storing_name = "zelda_DB_"
download_DB (url, cart_id, storing_name)

### Kellermannen ###
url = "http://www.dagbladet.no/tegneserie/kellermannen/"
cart_id = "kellermannen-stripe"
storing_name = "kellermannen_DB_"
download_DB (url, cart_id, storing_name)

### --------------------------- ###
