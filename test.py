
def funto(code ,i):
    line1 = 'cout<<"this is added as test line";'
    code.insert(i+1,line1)

file = open('test.cpp','r')

code=[]

i =0 
flag = True

for each in file:
    each.strip()
    code.append(each)
    if '#1234567' in each:
        flag=False
    
    if flag:
        i=i+1


funto(code,i);

file.close()

file = open('test.cpp','w')

for each in code:
    file.write(each)

file.close()






