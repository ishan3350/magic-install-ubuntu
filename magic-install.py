import os
myCmd = 'apt-get update -y'
os.system(myCmd)

myCmd = 'apt-get upgrade -y'
os.system(myCmd)

myCmd = 'apt-get dist-upgrade -y'
os.system(myCmd)

myCmd = 'apt-get install python3-pip'
os.system(myCmd)

myCmd = 'apt-get install apache2 -y'
os.system(myCmd)
