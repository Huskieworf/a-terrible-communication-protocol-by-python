#实现上位机和下位机通信，创建了Raspberrpi类和Arduino类
#author liyujiang
#time of birth  2015.10.29
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Arduino(object):
  #属性区
  #校验值arduino_check
  





  #函数区
  def __init__(self,arduino_check=0):
  #"""下位机的一些属性变量"""
    self.arduino_check=arduino_check


  def ask(self,raspberrypi):
  #"""ask函数，询问上位机是否可以发送""" 
    if raspberrypi.yes():
      return True
    else:
      return False

  def sent(self，raspberrypi，message):
  #"""sent函数，向上位机发送数据"""
    if self.ask():
      self.message=message
      raspberrypi.request(self.messsage)
      print("data has sent successfully ")
    else:
     print("data communication failed,please try again")

  def checkout(self):
  #"""计算校验值"""
   for letter in self.message: 
    self.arduino_check+=ord(letter)
   return self.arduino_check





class Raspberrypi(object):
  #校验码raspberrypi_check
  #应答标志flag=None
  #接受消息元组message = ('','','','','','','','','','')
  #消息元组脚标计数count=0
  #元组大小size=10
 
 

  #函数区
  def __init__(self,raspberrypi_check=0,flag=False,message = ('','','','','','','','','',''),count=0,size=10):
   #"""上位机的一些属性变量"""
    self.raspberrypi_check=raspberrypi_check
    self.flag=flag
    self.massage=message
    self.count=count
    self.size=size


  def yes(self): 
  #"""yes函数，对下位机ask的应答,可以接受消息返回true"""
    self.flagvalue()
    if self.flag:
      return True
    else:
      return False
 

  def flagvalue(self):
  #判断flag值
    self.flag=False
    for item in self.message:
      if item == '' :
         self.flag=True
  
  def check(self,arduino):
   #"""校验"""
    if self.checkout()==arduino.checkout():
       print("消息无误")
       return True
    else:
       print("消息有误")
       self.message[count]=''
       count-=1
       return False
  

  def request(self,message):
   #"""接受消息函数"""
    self.message[count]=message
    self.count+=1
    self.count%=self.size 
  

  def extract(self):
   """提取上位机的数据"""
    value=self.message[count]
    self.count-=1
    self.count%=self.size 
    self.message[count]=''
    return value
     

  def checkout(self):
  #"""计算校验值"""
  for letter in self.message[count]: 
    self.arduino_check+=ord(letter)
  return self.raspberrypi_check


 
