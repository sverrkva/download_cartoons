import urllib.request

# Download a file from url. Return 0 if error
def download_file (url):
    try:
        urllib.request.urlretrieve(url,"pondus2345.jpg")
        return 1
    except urllib.request.HTTPError as e:
        print ("Error " + str(e.code) + "\n" + "Could not download from url: " + url)
        return 0
