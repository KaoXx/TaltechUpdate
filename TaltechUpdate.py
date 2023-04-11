import pywhatkit
import time
import hashlib
from urllib.request import urlopen, Request
import datetime

# Setting up the URL that you want to monitor

TaltechUrl = Request('https://taltech.ee/en/courses-english'
                     ,headers={'User-Agent': 'Mozilla/5.0'})

# Get request and store the content 
response = urlopen(TaltechUrl).read()

# Initial Hash of the website
currentHash = hashlib.sha224(response).hexdigest()
print("[!] Running...")
time.sleep(10)

while True:
    try:
        # Permanent request and store the data
        response = urlopen(TaltechUrl).read()
        # Create the hash
        newHash = hashlib.sha224(response).hexdigest()
        # Check the hash
        if newHash == currentHash:
            continue
        # If something changes
        else:
            date = datetime.datetime.now()
            # Notify
            pywhatkit.sendwhatmsg_instantly(
            phone_no="+34XXXXXXXXX", 
            message="Something changed in the website",)
            print(str(date)+ " - Something changed")
            # Read the website
            response = urlopen(TaltechUrl).read()
            # Create a Hash
            currentHash = hashlib.sha224(response).hexdigest()
            # Wait 30 sec
            time.sleep(30)
            continue
    # Handle exception
    except Exception as e:
        print("Error")





