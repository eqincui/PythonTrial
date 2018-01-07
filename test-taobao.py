import time
import random

a=[1,2,4,6,7,9,12,15,20,25]
#random.shuffle(a)
print "淘宝11.11实时成交量（单位：亿元）"
print "--5--10--15--20-25--30--35--"
for i in a:
	ii=0
	while ii<i:
		print '',
		ii=ii+1;
	print '*\n'
	time.sleep(1) 
	
	