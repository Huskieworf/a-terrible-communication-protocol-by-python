#Warning: Angle inputed to NN should be only Angle[Z],fixed below.
#a function calcspd is added,to calculate body speed v[3] from EP[4] or ET[4]
#a saveoff function is added
import time
max=50
sx=13#variables in a sample
sy=5 #number of samples
# Variables might be used and can be added if needed
ET[4]=0 #body status from arduino
EP[4]=0
a[3]=0
w[3]=0
Angle[3]=0
v[3]=0

iw[3]=0 #ideal body status,for fr...use
iAngle[3]=[0]
iv[3]=[0]
spd=0
time=0
save_matrix_time=15#second

#sigmoids
VAL_AVAIL=FALSE
SND_AVAIL=FALSE
SNDING=FALSE
KEY_AVAIL=FALSE
STUDY_ON=FALSE

data_input[MAX]={'\0'} #Data from keyboard
data_recv[MAX]
samp[sx][sy]
#all arrays are defined by a function in judge()
#all variables above except imports will be deleted because this function will be imported into judge.py and global variables exist there

def main():
  while(1)
    if KEY_AVAIL:
      judgeK()
      #judge command from keyboard
      #import data_inpot[MAX]
    if Serial.avaliable():
      judgeD()
      #judge command from arduino
      #Serial is not read out yet

def judgeK():
  if data_input[0]=='f'&&data_input[1]='r':
    processStr()#Process key input to variable
    fr(spd,time)#spd scope is +-255,time is second,all integer,input should be checked
  else if data_input[0]=='b'&&data_input[1]'k':
    processStr()
    bk(spd,time)      
  else if data_input[0]=='l'&&data_input[1]'t':
    processStr()
    lt(spd,time)  
  else if data_input[0]=='r'&&data_input[1]'t':
    processStr()
    rt(spd,time)  
  else if data_input[0]=='r'&&data_input[1]'d':
    processStr()
    rd(spd,time)
  #all below might add '\0'
  else if data_input=='stop':
    stop0()
    #stop all actions and stay balanced
  else if data_input=='quit':
    quit0()
    #quit and poweroff
  else if data_input=='studyon':
    studyon()
    #study mode on
  else if data_input=='studyoff':
    studyoff()
    #study mode off
  else if data_input=='save':
    save0()
    #auto save samples to files,folder 20xx.xx.xx file xx:xx(ep.file ./2015.09.02/12:30),one file every minute
  else if data_input=='saveoff':
    saveoff()
    #auto save samples off
  else if data_input=='load':
    load0()
    #load samples from inputed time scope(20xx.xx.xx-xx:xx to 20xx.xx.xx-xx:xx)
    #to matrix samp[sx][sy]
  else if data_input=='saveD':
    saveD()
    #save NN matrix to default file
    #there are 3 matrix files named m1 m2 m3
  else if data_input=='autoon':
    autoon()
    #auto save matrix on
  else if data_input=='autooff':
    autooff()
    #off saving matrix
  else if data_input=='set_save_time':
    setST()
    #set matrix auto save time 
  else
    print "Input false"

def processStr():
#process data_input[] and get spd and time
def fr(spd,time):
#import speed and time
#return ideal body status
#iw[3] iAngle[3](Angle Z only) iv[3]
def bk(spd,time):
def lt(spd,time):
def rt(spd,time)
def rd(spd,time):
#return {(0,0,spd),90,(0,0,0)}
def stop0()
#return (0,0,0,90,0,0,0)
def quit0()
#poweroff
def studoon()
#study mode on,STUDY_ON is true
def studyoff()
def save0()
def saveoff()
def load0()
def saveD()
def autoon()
def autooff()
def setST()
#save_matrix_time is gonna be modified here

def judgeD():
#process data_recvd(String from Arduino)
#and give datas to variables

 
  while(Serial.avaliable)
    Serial.read()#read Serial one by one to data_recv[MAX]
  #then give values to variables ET[4] EP[4] a[3] w[3] Angle[3]
  calcspd();
  if self.sum==sum#check sum
    VAL_AVAIL=1
    send('Recv')#to arduino,"send" function is at "judge.py"
  else
   VAL_AVAIL=0
    send('Eror')#to arduino

def calcspd():
#calculate body speed v[3] from EP[4] or ET[4]

