import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
os.system("figlet FbiTactical")
print "Create By : FBI-Tactical"
print "Instagram   : https://instagram.com/fbitactical/"
print "github    : https://github.com/FBITactical"
print "Discord  : <tactical#8100>"
print
print "           [1]> Brute Force              "
print "           [2]> DDoS Attack              "
print "           [3]> NMap PortScanner         "
print "           [4]> Install Tools Hacking    "
print "           [5]> Phonenumber-DoxTool      "
print "           [6]> Ip-address DoxTool       "
print "           [7]> Tacticals Port-Scanner   "
print 
print " [0]> Exit "
print
A = raw_input("FbiTactical ==>> ")

if A == "1" or A == "01":
  os.system("python2 brute.py")

elif A == "2" or A == "02":
    os.system("clear")
    os.system("figlet DDoS Attack")
    ip = raw_input("Ip-Address : ")
    port = raw_input("Port       : ")
    packet =raw_input("Packet     : ")
    os.system("python2 pntddos %s %s %s" % (ip, port, packet))

elif A == "3" or A == "03":
    os.system("clear")
    os.system("figlet NMap Scan")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host))

elif A == "4" or A == "04":
    os.system("python2 lazymux.py")

elif A == "5" or A == "05":
    os.system("python3 tactical-scraper.py")

elif A == "6" or A == "06":
    os.system("python3 tactical-ip-osint.py")

elif A == "7" or A == "07":
    os.system("python3 tactical-portscanner.py")
    
elif A == "0" or A == "00":
    sys.exit()
    
else:
     print "\nERROR: Wrong Input"
     timeout(3)
     restart_program()
