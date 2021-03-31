#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())

def getIPaddress(ifacename):
    if ifacename in netifaces.interfaces():
        ifindex = netifaces.interfaces().index(ifacename)
        #print(netifaces.ifaddresses(ifacename)[netifaces.AF_INET][0]['addr'])
        return (netifaces.ifaddresses(ifacename)[netifaces.AF_INET][0]['addr'])


for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try: 
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        #print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        print(getIPaddress(i))
    
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

