f=open('Perepis.txt','r+')
with open('Perepis.txt') as f:
    l=f.readlines()
    for i in range(1,len(l)):
        print(l[i])

