import socket 
import struct 
import fcntl
import pyttsx
import time
def getIP(ethname):
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0X8915, struct.pack('256s', ethname[:15]))[20:24])
while (1):
        ip=getIP('eth0')
        engine = pyttsx.init()
        #engine.setProperty("rate",200)
        print ip
        engine.say("dddddd")
        engine.runAndWait()
        for i in list(ip.replace('.','d')):
                engine.say(i)
                engine.runAndWait()
                time.sleep(1)
        time.sleep(10) 
