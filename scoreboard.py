import requests, sys
from bs4 import BeautifulSoup
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    if(len(sys.argv) == 1):
        print "Please specify the number corresponding to the match"
        exit(0)
    index = int(sys.argv[1])
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("description")
    score = data[index].text
    sendmessage("Score", score)
    sleep(30)