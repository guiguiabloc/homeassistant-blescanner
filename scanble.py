from bluepy.btle import Scanner, DefaultDelegate
import sys
import json

try:
    import paho.mqtt.publish as publish
except:
    print('You do not have mqtt installed, which is needed to talk to the broker.')
    print('Install using sudo pip3 install paho-mqtt')

voiture1=False
voiture2=False
poubellejaune=False

# change by your mac adresses
voiture2ble="a1:c1:11:11:11:11"
voiture1ble="a1:c1:11:11:11:11"
poubellejauneble="e1:11:11:11:11:11"

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def identifiantndleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)

        elif isNewData:
            print("Received new data from", dev.addr)


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)



for dev in devices:
   #print(dev.addr)
   if voiture2ble in dev.addr:
       voiture2 = True
   if voiture1ble in dev.addr:
       voiture1 = True
   if poubellejauneble in dev.addr:
       poubellejaune = True

if voiture2 == True:
   topic = "maison/voiture/voiture2"
   message = "home"
   publish.single(topic, message, hostname="ipMQTT", port=1883, auth={"username":"identifiant", "password":"motdepasse"}, tls=None)

if voiture2 == False:
   topic = "maison/voiture/voiture2"
   message = "not_home"
   publish.single(topic, message, hostname="ipMQTT", port=1883, auth={"username":"identifiant", "password":"motdepasse"}, tls=None)

if voiture1 == True:
   topic = "maison/voiture/voiture1"
   message = "home"
   publish.single(topic, message, hostname="ipMQTT", port=1883, auth={"username":"identifiant", "password":"motdepasse"}, tls=None)

if voiture1 == False:
   topic = "maison/voiture/voiture1"
   message = "not_home"
   publish.single(topic, message, hostname="ipMQTT", port=1883, auth={"username":"identifiant", "password":"motdepasse"}, tls=None)

if poubellejaune == True:
   topic = "maison/presence/poubellejaune"
   message = "home"
   publish.single(topic, message, hostname="ipMQTT", port=1883, auth={"username":"identifiant", "password":"motdepasse"}, tls=None)

if poubellejaune == False:
   topic = "maison/presence/poubellejaune"
   message = "not_home"
   publish.single(topic, message, hostname="ipMQTT", port=1883, auth={"username":"identifiant", "password":"motdepasse"}, tls=None)
