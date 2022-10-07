#!/usr/bin/env/python3

#Import libraries

import os
from time import sleep 


#Sudo check

#if os.geteuid() != 0:
 #   exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

#Welcome

print("Welcome to the pyducky script, please choose a program: \n")

#Get the required instructions

print("1) Reverse Shell\t 2) Turn off antivairus")
print("3) Wifi Extractor\t 4) Rickroll")
print("5) Hacked Message\t 6) Custom\n")

file = int(input("Please type a number and press enter: "))

print("")

#Preparing the pico

input("Please hold the boot select button and connect the pico. Press enter when it shows up...")

sleep(5)

print("Formating pico...")
os.system("cp src/format.uf2 /media/$USER/RPI-RP2/ ")

sleep(20)

print("Flashing circuit python...")
os.system("cp src/circuit_python.uf2 /media/$USER/RPI-RP2/ ")

sleep(20)

print("Copying libraries...")
os.system("cp -r src/lib/adafruit_hid /media/$USER/CIRCUITPY/lib/")

sleep(10)

print("Copying main program...")
os.system("cp src/code.py /media/$USER/CIRCUITPY/code.py")

sleep(2)

print("Preparation done!\n")

#Flashing the right program

if file == 1:
    input("Please modify the file src/scripts/reverse.dd to your needs the press enter...")
    os.system("cp src/scripts/reverse.dd /media/$USER/CIRCUITPY/payload.dd")
    print("Transfered Reverse Shell")
elif file == 2:
    os.system("cp src/scripts/antivaitusoff.dd /media/$USER/CIRCUITPY/payload.dd")
    print("Transfered Turn off Antivairus")
elif file == 3:
    input("Please modify src/scripts/extractor.dd to your needs then press enter...")
    os.system("cp src/scripts/extractor.dd /media/$USER/CIRCUITPY/payload.dd")
    print("Transfered Wifi Extractor\n")
elif file == 4:
    oneortwo = int(input("Please select 1 for complicated or 2 for simple: "))
    if oneortwo == 1:
        os.system("cp src/scripts/rickrollcomp.dd /media/$USER/CIRCUITPY/payload.dd")
    elif oneortwo == 2:
        os.system("cp src/scripts/rickrollsimple.dd /media/$USER/CIRCUITPY/payload.dd")
    print("Tranfered Rickroll\n")
elif file == 5:
    os.system("cp src/scripts/hacked.dd /media/$USER/CIRCUITPY/payload.dd")
    print("Transfered Hacked Message\n")
elif file == 6:
    input("Create your custom file src/scripts/custom.dd and press enter...")
    os.system("cp src/scripts/custom.dd /media/$USER/CIRCUITPY/payload.dd")
    print("Transfered custm file.\n")
else:
    exit("Wrong number please rerun the script...")


print("Your pico is ready to go but please do not use this for mailicious purposes...")
sleep(0.5)
exit("Bye!")
    
