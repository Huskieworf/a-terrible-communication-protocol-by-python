out_date=([1,2,3],[4,8,6],[7,8,9])
out_date2=([9,8,7],[6,5,4],[3,2,1])
split=' '
first_dimension=3
second_dimension=3
file_num=1
import os
import time
os.system('touch 1 2 3 4 5')
os.system('rm 2015*')
num=0
name_record=['1','2','3','4','5']
def save():
    file_num=1
    out_file='./result'+str(file_num%5)
    j=0
    while j<first_dimension:
        i=0
        while i<second_dimension:
            file=open(out_file,'a')
            file.write(str(out_date[j][i]))
            file.write(split)
            i=i+1
        j=j+1
    file.write('\n')
    print(out_date)
    file.close()
    #########
    new_filename=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())
    os.rename(out_file,new_filename)
    name_record.insert(0,new_filename)
    del_file='./'+name_record[5]
    print(del_file)
    os.remove(name_record[5])
    name_record.pop()

def load(num):
    file=open(name_record[num],'r')
    tmp_file=file.readlines()
    tmp=tmp_file[-1]
    j=0
    while j<first_dimension:
        i=0
        while i<second_dimension:
            out_date2[j][i]=int(tmp[:tmp.find(split)])
            tmp=tmp[tmp.find(split)+1:]
            i=i+1
        j=j+1
    print(out_date2)
    file.close()



