import urllib2
from mailAlert import send_email

url = 'http://supersaas.fr/schedule/Modeles/centre_OPI?view=free'

keyword = 'FRENCH'

response = urllib2.urlopen(url)
webContent = response.readlines()

freeSpot = False

with open('datas.state' , 'r+b') as f:
    state = f.read()
    print state

    for line in webContent :
        if line.find(keyword) != -1 and line.find('<td>') != -1 :
            freeSpot = True

    print freeSpot
    if state != str(freeSpot):
        if freeSpot :
            send_email()

        f.seek(0)
        f.truncate()
        f.write(str(freeSpot))
