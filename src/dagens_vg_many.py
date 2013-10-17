import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
from datetime import date, timedelta
import functions #my own

def download_VG_many (cart_id, map_name, storing_name, number):

    # Spesify where to store the files
    directory = "../Downloaded_cartoons/" + map_name
    
    functions.make_dir(directory) #  Function that check if the directory exists. If not - create it

    for i in range(number):
        # Make a new url
        date_ = date.today() - timedelta(int(i+1))
        date_ = str(date_)
        td = date_.split('-')
        url_string_array = ["http://www.heltnormalt.no/img/",cart_id,td[0],"/",td[1],"/",td[2],".jpg"]
        picture_url = ''.join(url_string_array)
 
        # Make a new name for the file with timestamp
        name_string_array = [directory,storing_name,"_",date_,"_VG",".jpg"]
        tag = ''.join(name_string_array)
        

        # Downlad the picture
        if (functions.download_file(picture_url, tag) == 0):
            break

        if ((i+1)%10 == 0):
            print ("finished with picture # " , i+1)

    print ("*** Finished " + storing_name + ". Downloaded " + str(i) + " pictures")
    return



### -------- VG --------- ###

### Tommy og Tigern ###
cart_id = "tommytigern/"
map_name = "Tommy&Tigern/"
storing_name = "tommy_&_tigern"
download_VG_many (cart_id,map_name,storing_name,300)

### Kollektivet ###
cart_id = "kollektivet/"
map_name = "Kollektivet/"
storing_name = "kollektivet"
download_VG_many (cart_id,map_name,storing_name,300)

### Dilbert ###
cart_id = "dilbert/"
map_name = "Dilbert/"
storing_name = "dilbert"
download_VG_many (cart_id,map_name,storing_name,300)

### Wumo ###
cart_id = "wumo/"
map_name = "Wumo/"
storing_name = "woumo"
download_VG_many (cart_id,map_name,storing_name,300)

### Hjalmar ###
cart_id = "hjalmar/"
map_name = "Hjalmar/"
storing_name = "hjalmar"
download_VG_many (cart_id,map_name,storing_name,300)

### Truth Facts ###
cart_id = "truth_facts/"
map_name = "Truth_Facts/"
storing_name = "truth_facts"
download_VG_many (cart_id,map_name,storing_name,300)

##### --------------------------- ###

print ("*** FINISHED downloading ***")
