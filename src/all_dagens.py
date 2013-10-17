import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
import os


# Set the directory where you wants to store the cartoons
directory = "./Downloaded_cartoons/"

# Check if the directory exists. If not - create it
if not os.path.exists(directory):
    os.makedirs(directory)


### VG ###
def download_VG (cart_id, storing_name):

    # Make a new url
    today = str(datetime.date.today())
    td = today.split('-')
    url_string_array = ["http://www.heltnormalt.no/img/",cart_id,td[0],"/",td[1],"/",td[2],".jpg"]
    picture_url = ''.join(url_string_array)

    # Make a new name for the file with timestamp
    name_string_array = [directory,storing_name,today,"_VG",".jpg"]
    tag = ''.join(name_string_array)

    # Downlad the picture
    urllib.request.urlretrieve(picture_url, tag)

    print ("Finished " + tag)
   
    return

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
    string_array = [directory,storing_name,today,"_DB",".jpg"]
    tag = ''.join(string_array)

    # Downlad the picture
    urllib.request.urlretrieve(picture_url, tag)

    print ("Finished " + tag)
   
    return



### -------- VG --------- ###

### Tommy og Tigern ###
cart_id = "tommytigern/"
storing_name = "tommy_&_tigern_"
download_VG (cart_id, storing_name)

### Kollektivet ###
cart_id = "kollektivet/"
storing_name = "kollektivet_"
download_VG (cart_id, storing_name)

### Dilbert ###
cart_id = "dilbert/"
storing_name = "dilbert_"
download_VG (cart_id, storing_name)

### Wumo ###
cart_id = "wumo/"
storing_name = "woumo_"
download_VG (cart_id, storing_name)

### Hjalmar ###
cart_id = "hjalmar/"
storing_name = "hjalmar_"
download_VG (cart_id, storing_name)

### Truth Facts ###
cart_id = "truth_facts/"
storing_name = "truth_facts_"
download_VG (cart_id, storing_name)

### -------- DAGBLADET --------- ###

### Pondus ###
url = "http://www.dagbladet.no/tegneserie/pondus/"
cart_id = "pondus-stripe"
storing_name = "pondus_"
download_DB (url, cart_id, storing_name)

### Lunch ###
url = "http://www.dagbladet.no/tegneserie/lunch/"
cart_id = "lunch-stripe"
storing_name = "lunch_"
download_DB (url, cart_id, storing_name)

### Nemi ###
url = "http://www.dagbladet.no/tegneserie/nemi/"
cart_id = "nemi-stripe"
storing_name = "nemi_"
download_DB (url, cart_id, storing_name)

### Storefri ###
url = "http://www.dagbladet.no/tegneserie/gjesteserie/storefri/"
cart_id = "gjesteserie/storefri-stripe"
storing_name = "storefri_"
download_DB (url, cart_id, storing_name)

### Rocky ###
url = "http://www.dagbladet.no/tegneserie/rocky/"
cart_id = "rocky-stripe"
storing_name = "rocky_"
download_DB (url, cart_id, storing_name)

### Fagprat ###
url = "http://www.dagbladet.no/tegneserie/fagprat/"
cart_id = "fagprat-stripe"
storing_name = "fagprat_"
download_DB (url, cart_id, storing_name)

### Zelda ###
url = "http://www.dagbladet.no/tegneserie/zelda/"
cart_id = "zelda-stripe"
storing_name = "zelda_"
download_DB (url, cart_id, storing_name)

### Kellermannen ###
url = "http://www.dagbladet.no/tegneserie/kellermannen/"
cart_id = "kellermannen-stripe"
storing_name = "kellermannen_"
download_DB (url, cart_id, storing_name)

### --------------------------- ###

print ("*** FINISHED downloading ***")
