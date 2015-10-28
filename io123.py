date=([1,2,3],[4,8,6],[7,8,9])
date2=([9,8,7],[6,5,4],[3,2,1])
split=' '
first_dimension=3
second_dimension=3
def save():
    j=0
    while j<first_dimension:
        i=0
        while i<second_dimension:
            file=open('./date','a')
            file.write(str(date[j][i]))
            file.write(split)
            i=i+1
        j=j+1
    file.write('\n')
    print(date)
    file.close()




def load():
    file=open('./date','r')
    tmp_file=file.readlines()
    tmp=tmp_file[-1]
    j=0
    while j<first_dimension:
        i=0
        while i<second_dimension:
            date2[j][i]=int(tmp[:tmp.find(split)])
            tmp=tmp[tmp.find(split)+1:]
            i=i+1
        j=j+1
    
#    print(tmp)
    print(date2)
    file.close()
