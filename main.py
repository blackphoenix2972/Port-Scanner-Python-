# Project: Port Scanner
# Function of program: To check which ports are open on a target host

import socket
import subprocess
import sys
import time
import os


# Asks the user to enter target IP address
is_valid_address = True
while is_valid_address:

    try:

        target_host = input('[*] Enter the IP address at the target computer: ')
        target_host_ip  = socket.gethostbyname(target_host)

        cmd = os.system('ping ' + target_host_ip)
        if (cmd == 0):
            print('\nTarget host is up and running...')
            is_valid_address = False
            print('\nConnecting to ' + target_host_ip + '...\n')
            time.sleep(2)
        else:
            print('Target host is unreachable...\n')




    except socket.gaierror:
        print('Incorrect address! Please try again.\n')



def menu():
    is_valid = True
    while is_valid:

        try:

            print('[1] Scan for a specific port number')
            print('[2] Scan a range of ports')
            user_choice = int(input('\n Please select an option: '))

            if (user_choice == 1):
                port_number = int(input('\nEnter a port number you wish to scan: '))
                search_specific_port(port_number)
                is_valid = False
            elif (user_choice == 2):
                user_port_choice = int(input("Please enter up to which port to scan: "))
                search_range_port(user_port_choice)
                is_valid = False
        except ValueError:
            print('\n Incorrect option! Please enter one of the options from above.\n')



def search_specific_port(port_number):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target_host_ip, port_number))
    if (result == 0):
        print('Port ' + str(port_number) + " Open")
    else:
        print('Port ' + str(port_number) + ' Closed')

    sock.close()

def search_range_port(port_number):


    for port in range(1, port_number+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_host_ip, port))
        if (result == 0):
            print('Port ' + str(port) + ' Open')

        else:
            pass

    sock.close()


menu()
