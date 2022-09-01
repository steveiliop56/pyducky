#!/usr/bin/env/python3

#Import libraries

import os

from time import sleep 

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

#Get drive letter

letter = input("Please enter the drive letter: ")

print("")

sleep(2)

print("Formating pico...")

os.system(f"copy src\format.uf2 {letter}:\ ")

sleep(20)

print("Flashing circuit python...")

os.system(f"copy src\circuit_python.uf2 {letter}:\")

sleep(20)

print("Copying libraries...")

os.system(f"copy  src\lib/adafruit_hid {letter}:\CIRCUITPY\lib\")

sleep(10)

print("Copying main program...")

os.system(f"copy src\code.py {letter}:\CIRCUITPY\code.py")

sleep(2)

print("Preparation done!\n")

#Flashing the right program

if file == 1:

    input("Please modify the file src/scripts/reverse.dd to your needs the press enter...")

    os.system(f"copy src\scripts\reverse.dd {letter}:\CIRCUITPY\payload.dd")

    print("Transfered Reverse Shell")

elif file == 2:

    os.system(f"copy src\scripts\antivaitusoff.dd {letter}:\CIRCUITPY\payload.dd")

    print("Transfered Turn off Antivairus")

elif file == 3:

    input("Please modify src/scripts/extractor.dd to your needs then press enter...")

    os.system(f"copy src\scripts\extractor.dd {letter}:\CIRCUITPY\payload.dd")

    print("Transfered Wifi Extractor\n")

elif file == 4:

    oneortwo = int(input("Please select 1 for complicated or 2 for simple: "))

    if oneortwo == 1:

        os.system(f"copy src\scripts\rickrollcomp.dd {letter}:\CIRCUITPY\payload.dd")

    elif oneortwo == 2:

        os.system(f"copy src\scripts\rickrollsimple.dd {letter}:\CIRCUITPY\payload.dd")

    print("Tranfered Rickroll\n")

elif file == 5:

    os.system(f"copy src\scripts\hacked.dd {letter}:\CIRCUITPY\payload.dd")

    print("Transfered Hacked Message\n")

elif file == 6:

    input("Create your custom file src/scripts/custom.dd and press enter...")

    os.system(f"copy src\scripts\custom.dd {letter}:\CIRCUITPY\payload.dd")

   print("Transfered custm file.\n")

else:

    exit("Wrong number please rerun the script...")

print("Your pico is ready to go but please do not use this for mailicious purposes...")

sleep(0.5)

exit("Bye!")

    
