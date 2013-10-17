import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
from datetime import date, timedelta


### VG ###
def download_VG (cart_id, storing_name):

    # Make a new url
    today = str(datetime.date.today())
    td = today.split('-')
    url_string_array = ["http://www.heltnormalt.no/img/",cart_id,td[0],"/",td[1],"/",td[2],".jpg"]
    picture_url = ''.join(url_string_array)
   

    # Make a new name for the file with timestamp
    name_string_array = ["pictures/",storing_name,today,".jpg"]
    tag = ''.join(name_string_array)

    # Downlad the picture
    urllib.request.urlretrieve(picture_url, tag)

    print ("Finished " + tag)
   
    return

def download_VG_many (cart_id, map_name, storing_name, number):

    for i in range(number):
        # Make a new url
        date_ = date.today() - timedelta(int(i+1))
        date_ = str(date_)
        td = date_.split('-')
        url_string_array = ["http://www.heltnormalt.no/img/",cart_id,td[0],"/",td[1],"/",td[2],".jpg"]
        picture_url = ''.join(url_string_array)
 
        # Make a new name for the file with timestamp
        name_string_array = ["Archive/",map_name, storing_name,date_,".jpg"]
        tag = ''.join(name_string_array)

        # Downlad the picture
        urllib.request.urlretrieve(picture_url, tag)

        if ((i+1)%10 == 0):
            print ("finished with picture # " , i+1)

    print ("*** Finished " + tag + ". # of pictures: " + number)
   
    return





### -------- VG --------- ###

### Tommy og Tigern ###
cart_id = "tommytigern/"
map_name = "Tommy&Tigern/"
storing_name = "tommy_&_tigern_VG_"
##download_VG_many (cart_id,map_name,storing_name,300)

### Kollektivet ###
cart_id = "kollektivet/"
map_name = "Kollektivet/"
storing_name = "kollektivet_VG_"
##download_VG_many (cart_id,map_name,storing_name,300)

### Dilbert ###
cart_id = "dilbert/"
map_name = "Dilbert/"
storing_name = "dilbert_VG_"
##download_VG_many (cart_id,map_name,storing_name,300)

### Wumo ###
cart_id = "wumo/"
map_name = "Wumo/"
storing_name = "woumo_VG_"
##download_VG_many (cart_id,map_name,storing_name,300)

### Hjalmar ###
cart_id = "hjalmar/"
map_name = "Hjalmar/"
storing_name = "hjalmar_VG_"
##download_VG_many (cart_id,map_name,storing_name,300)

### Truth Facts ###
cart_id = "truth_facts/"
map_name = "Truth_Facts/"
storing_name = "truth_facts_VG_"
download_VG_many (cart_id,map_name,storing_name,300)

##### --------------------------- ###

print ("*** FINISHED downloading ***")
