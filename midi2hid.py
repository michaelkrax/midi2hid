import subprocess
import serial
import struct
import atexit

ttyATH0 = serial.Serial('/dev/ttyATH0', 115200)


def send_serial(command, value):
    ttyATH0.write(struct.pack('cb', command, value))


def send_midi(midi):
    a, b, c = midi.split(" ")
    subprocess.call("echo -ne '\\x"+a+"\\x"+b+"\\x"+c+"' > /dev/midi", shell=True)
    print "\033[0;31m: "+midi+"\033[0m",


def initialize():
    # clear all LEDs
    send_midi("B0 00 00")
    
    # exit button
    # send_midi("B0 6F 0A")
    
    # mouse diamond
    send_midi("90 46 7F")
    send_midi("90 57 7F")
    send_midi("90 47 7F")
    send_midi("90 56 7F")
    
    # wsad diamond
    send_midi("90 03 7F")
    send_midi("90 12 7F")
    send_midi("90 02 7F")
    send_midi("90 13 7F")
    
    # mouse click
    send_midi("90 53 0A")

    # jump
    send_midi("90 42 28")
    
    # numbers
    send_midi("90 33 19")  # 1
    send_midi("90 23 19")  # 2
    send_midi("90 24 19")  # 3
    send_midi("90 25 19")  # 4
    send_midi("90 35 19")  # 5
    send_midi("90 45 19")  # 6
    send_midi("90 44 19")  # 7


def main():
    process = subprocess.Popen("amidi --dump", shell=True, stdout=subprocess.PIPE)
    atexit.register(cleanup)

    while True:
        output = process.stdout.readline(8)
        if output == '' and process.poll() is not None:
            break
        if output:
            midi = output.strip()
            print midi,

            # mouse left
            if midi == "90 46 7F": send_serial('L', -1); send_midi("90 46 0B")
            if midi == "90 46 00": send_serial('L', 0); send_midi("90 46 7F")

            # mouse right
            if midi == "90 57 7F": send_serial('R', 1); send_midi("90 57 0B")
            if midi == "90 57 00": send_serial('R', 0); send_midi("90 57 7F")

            # mouse up
            if midi == "90 47 7F": send_serial('U', -1); send_midi("90 47 0B")
            if midi == "90 47 00": send_serial('U', 0); send_midi("90 47 7F")

            # mouse down
            if midi == "90 56 7F": send_serial('D', 1); send_midi("90 56 0B")
            if midi == "90 56 00": send_serial('D', 0); send_midi("90 56 7F")

            # W
            if midi == "90 03 7F": send_serial('w', 1); send_midi("90 03 0B")
            if midi == "90 03 00": send_serial('w', 0); send_midi("90 03 7F")

            # S
            if midi == "90 12 7F": send_serial('s', 1); send_midi("90 12 0B")
            if midi == "90 12 00": send_serial('s', 0); send_midi("90 12 7F")

            # A
            if midi == "90 02 7F": send_serial('a', 1); send_midi("90 02 0B")
            if midi == "90 02 00": send_serial('a', 0); send_midi("90 02 7F")

            # D
            if midi == "90 13 7F": send_serial('d', 1); send_midi("90 13 0B")
            if midi == "90 13 00": send_serial('d', 0); send_midi("90 13 7F")

            # mouse click
            if midi == "90 53 7F": send_serial('M', 1); send_midi("90 53 0B")
            if midi == "90 53 00": send_serial('M', 0); send_midi("90 53 0A")

            # jump
            if midi == "90 42 7F": send_serial('j', 1); send_midi("90 42 38")
            if midi == "90 42 00": send_serial('j', 0); send_midi("90 42 28")

            # 1
            if midi == "90 33 7F": send_serial('1', 1); send_midi("90 33 1B")
            if midi == "90 33 00": send_serial('1', 0); send_midi("90 33 19")

            # 2
            if midi == "90 23 7F": send_serial('2', 1); send_midi("90 23 1B")
            if midi == "90 23 00": send_serial('2', 0); send_midi("90 23 19")

            # 3
            if midi == "90 24 7F": send_serial('3', 1); send_midi("90 24 1B")
            if midi == "90 24 00": send_serial('3', 0); send_midi("90 24 19")

            # 4
            if midi == "90 25 7F": send_serial('4', 1); send_midi("90 25 1B")
            if midi == "90 25 00": send_serial('4', 0); send_midi("90 25 19")

            # 5
            if midi == "90 35 7F": send_serial('5', 1); send_midi("90 35 1B")
            if midi == "90 35 00": send_serial('5', 0); send_midi("90 35 19")

            # 6
            if midi == "90 45 7F": send_serial('6', 1); send_midi("90 45 1B")
            if midi == "90 45 00": send_serial('6', 0); send_midi("90 45 19")

            # 7
            if midi == "90 44 7F": send_serial('7', 1); send_midi("90 44 1B")
            if midi == "90 44 00": send_serial('7', 0); send_midi("90 44 19")

            #exit
            if midi == "B0 6F 00": send_serial('X', 0); send_midi("B0 00 00"); break


def cleanup():
    # clear all LEDs
    send_midi("B0 00 00")

    # kill all amidi processes to be sure we don't leave device blocked
    subprocess.call("killall amidi", shell=True)

initialize()
main()

