#!/usr/bin/python
#import start0.py
#import NN.py
import time
import threading
MAX=50
sx=13#variables in a sample
sy=5 #number of samples
# Variables might be used and can be added if needed
ET=[0,0,0,0] #body status from arduino
EP=[0,0,0,0]
a=[0,0,0]
w=[0,0,0]
Angle=[0,0,0]
v=[0,0,0]

iw=[0,0,0] #ideal body status,for fr...use
iAngle=[0,0,0]
iv=[0,0,0]
spd=0
time=0
pi=0 #process i,if pi=4 then means all threads started successfully
save_matrix_time=15#second

#sigmoids
VAL_AVAIL=True
SER_AVAIL=False
SND_AVAIL=False #whether send queue is avaliable
SNDING=False
KEY_AVAIL=False
STUDY_ON=False

data_input=['\0' for x in range (0,MAX)] #Data from keyboard
data_recv=[0 for x in range (0,MAX)]
samp=[[0 for x in range (0,sx)] for y in range (0,sy)]

class start1(threading.Thread): #father class is threading.Thread
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self):
    #start0.main()
    global pi #referece global variable
    pi=pi+1
    #print "pi=%d"%(pi)
    #print "start0.main()"

class NN1(threading.Thread):
  #Netual Network
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self):
    #NN.main()
    global pi
    pi=pi+1
    #print "pi=%d"%(pi)
    #print "NN.main()"

class monitD(threading.Thread):
  #monit Serial data
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self):
    global pi
    pi=pi+1
    monitDf()
    #print "pi=%d"%(pi)
    #print "monitDf.main()"

class monitK(threading.Thread):
  #monit Keyboard
  def __init__(self):
    #self.thread_stop=False;
    threading.Thread.__init__(self)
  def run(self):
    global pi
    pi=pi+1
    #print "pi=%d"%(pi)
    #print "monitKf.main()"
    monitKf()    

def main():
  #start0.Init()
  pi=0
  thread1=start1()
  thread2=NN1()
  thread3=monitD()
  thread4=monitK()
  thread1.start()
  thread2.start()
  thread3.start()
  thread4.start()
  #time.sleep(10)

def monitDf():
  #if Serial.avaliable==True:
    SER_AVAIL=True

def monitKf():
  global data_input
  print "type quit to quit"
  while data_input != "quit" and pi == 4:
  #i = 0
  #for i in range (3):  
    try:
      data_input=raw_input(">>")
      KEY_AVAIL=True
      print data_input
      #print "pi=%d"%(pi)
    except KeyboardInterrupt as e:
      print "KeyInterrupttttttttttt"
      print e
    #finally:
      #print "exit!"

def send(data):
  while SND_AVAIL==False:
    continue
  SND_AVAIL=False
  while SENDING==True:
    continue
  SENDING=True
  #Serial.println(data)
  SENDING=False
  SND_AVAIL==True

def send():
  while SND_AVAIL==False:
    continue
  SND_AVAIL=False
  while SENDING==True:
    continue
  SENDING=True
  #Serial.println(data_to_send)
  SENDING=False
  SND_AVAIL==True

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt as e:
    print "exit!" + e
