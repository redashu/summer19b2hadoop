#!/usr/bin/python3
import   cgi,subprocess,os
import  cgitb
cgitb.enable()

print("Content-type:text/html")
print("")

#  get  html page  and  data
web=cgi.FieldStorage()
data=web.getvalue('x')

#print(data)
#check=os.system('sudo  rpm  -q  docker')
if data  ==   "installd"  :
	print("Docker   aleardy   install ...")

else  :
	print("don't  know whats going  on ")
