import numpy as np
import random

num_ecell = 256
num_out1 = 400
num_out2 = 100
branch_num = 10


a = np.loadtxt('con_var_out1.dat')
b = a[0,:]
#print a
#print b

c = b.sum()
#print c

#print len(a), len(a[0])
max_c = 0
max_index = -1
for i in range(0,len(a)-1):
    b = a[i,:]
    c = b.sum()
    if c>max_c :
        max_c = c
        max_index = i

print int(max_c)
#lists = range(int(max_c))
#for i in range (0,num_out1):
#random.shuffle(lists)
#print '\t'.join([str(i) for i in lists])


#print max_index

max_c = 0
a = np.loadtxt('con_var_out2.dat')
for i in range(0,len(a)-1) :
    b = a[i,:]
    c = b.sum()
    if c > max_c :
        max_c = c
        max_index = i

print int(max_c)



max_c = 0
a = np.loadtxt('con_var_i2o1.dat')
for i in range(0,len(a)-1) :
    b = a[i,:]
    c = b.sum()
    if c > max_c :
        max_c = c
        max_index = i
print int(max_c)


max_c = 0
a = np.loadtxt('con_var_i2o2.dat')
for i in range(0,len(a)-1) :
    b = a[i,:]
    c = b.sum()
    if c > max_c :
        max_c = c
        max_index = i
print int(max_c)




