#!/usr/bin/env python

import urllib2
import pickle
from mailAlert import send_email

url = 'http://supersaas.fr/schedule/Modeles/centre_OPI?view=free'
#url = 'file:///Users/thomasmazaleyrat/Desktop/pageDispo.webarchive'

keyword = 'RDV'
fileDataStorage = 'state.pickle'

response = urllib2.urlopen(url)
webContent = response.readlines()

freeSpot = False

try:
    with open(fileDataStorage , 'r') as f:
        state = pickle.load(f)
        print 'state.pickle opened and contain ' , state
except IOError:
    state = False
    with open(fileDataStorage, 'w') as f:
        pickle.dump(state,f)
    print 'state.pickel created'

for line in webContent :
    if line.find(keyword) != -1 :#and line.find('<td>') != -1 :
        freeSpot = True

print freeSpot
print state
if state != freeSpot:
    if freeSpot :
        send_email()
        print 'mail sent'

    with open(fileDataStorage , 'w') as f:
        pickle.dump(freeSpot,f)
    print 'state.pickel updated'

print 'program finished'
