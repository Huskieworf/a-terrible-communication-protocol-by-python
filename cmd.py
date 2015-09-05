#!/usr/bin/evn python
import action
import io123
#action.py include[fr bk lt rt rd] !! NULL
#io.py include save load
command=input()
#command = 'ab cde fgh'
sStr2 = ' '
options1='null'
options2='null'
#sStr3 = sStr1.find(sStr2)
#print(sStr3)
if command.find(sStr2)==-1:
    filename=command
else :
    filename = command[:command.find(sStr2)]
    command = command[command.find(sStr2) + 1:]
    if command.find(sStr2)==-1:
        options1 = command
        
    else :
        options1 = command[:command.find(sStr2)]
        command = command[command.find(sStr2) + 1:]
        options2 = command       
print(filename)
print(options1)
print(options2)
####################
if filename=='fr':
    processStr()
    action.fr(options1,options2)
elif filename=='bk':
    processStr()
    action.bk(options1,options2)
elif filename=='lt':
    processStr()
    action.lt(options1,options2)
elif filename=='rt':
    processStr()
    action.rt(options1,options2)
elif filename=='rd':
    processStr()
    action.rd(options1,options2)
#####-------------#####
elif filename=='save':
    io123.save()
    print('save')
##elif filename=='stop':
##    print('stop')
##else:
##    print('err')
###parameter=
##if command == 'fr':
##    print('done')
##else :
##    print('err')
##print(command)
