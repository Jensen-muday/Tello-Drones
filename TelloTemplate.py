# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nJensen Muday")
print("Program Name: Square")
print("Date: 2.6.2024 ")
print("Drone WIFI = DEC5")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')
        '''
     # Square - Pilot = Avonlea Thalmann - CoPilot = Jensen Muday
        sendmsg('forward 100', )
        sendmsg('cw 90')
        sendmsg('forward 100')
        sendmsg('cw 90')
        sendmsg('forward 100')
        sendmsg('cw 90')
        sendmsg('forward 100')
        sendmsg('cw 90',)
        '''




     # Triangle - Pilot = Jensen Muday - CoPilot = Avonlea Thalmann
        for i in range (3):
            sendmsg('forward 80', 10)
            sendmsg('cw 120', 10)

     # Circle - Pilot = Avonlea Thalmann - CoPilot = Jensen Muday

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')

except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()