#! /usr/bin/env python
# coding:utf-8

import time
import xlrd


workbook = xlrd.open_workbook('C:\Python27\examples\utilization-ECUT.xls')
worksheet = workbook.sheet_by_index(0)

print "                                          Rob STP Utilzation(%)                              "
print "0------------------------25------------------------50----------------------75-----------------------100"
#data from row 9th and column 3th
rownum=8
column=2
#print(worksheet.cell(rownum,column).value)
#while worksheet.cell(rownum,column).value != xlrd.empty_cell.value:
while rownum <= 68:
	b=int(worksheet.cell(rownum,column).value)
	i=0
	while i<=b:
		print '',
		i=i+1;
	print '*\n'
	rownum=rownum+1
	#time.sleep(1) 


	
