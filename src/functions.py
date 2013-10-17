import urllib.request
import os

# Download a file from url
# store it with the given name which also contains the directory.
# Return 0 if error
def download_file (url, storing_name):
    try:
        urllib.request.urlretrieve(url,storing_name)
        return 1
    except urllib.request.HTTPError as e:
        print ("Error " + str(e.code) + "\n" + "Could not download from url: " + url)
        return 0


# Check if the directory exists. If not - create it
def make_dir (directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return
