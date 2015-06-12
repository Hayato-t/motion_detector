import numpy as np
import random

num_ecell = 256
num_out1 = 400
num_out2 = 100
branch_num = 10

a = np.loadtxt('con_var_i2o1.dat')
b = a[0,:]
c = b.sum()
max_c = 0

for i in range(0,len(a)-1) :
    b = a[i,:]
    c = b.sum()
    if c > max_c :
        max_c = c
        max_index = i

lists = range(int(max_c))
for i in range (0,num_out1*branch_num):
    random.shuffle(lists)
    print '\t'.join([str(i) for i in lists])
