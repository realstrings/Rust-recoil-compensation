import win32api
import time
import ctypes
guntype=0
timer=0
smooth=5
import json
sensitivity=0
guns=['AssaultRifle','LR300AssaultRifle','Thompson','MP5A4','CustomSMG','M249']
AssaultRifle = [ [ -36.3583, 52.3906 ], [ 5, 46 ], [ -55, 42 ], [ -42, 37 ], [ 0, 33 ], [ 16, 28 ], [ 29, 24 ], [ 38, 19 ], [ 42, 14 ], [ 42, 9 ], [ 38, 9 ], [ 30, 18 ], [ 17, 25 ], [ 0, 29 ], [ -15, 32 ], [ -27, 33 ], [ -37, 32 ], [ -43, 29 ], [ -46, 24 ], [ -45, 17 ], [ -42, 8 ], [ -35, 5 ], [ -24, 14 ], [ -11, 21 ], [ 12, 25 ], [ 36, 28 ], [ 49, 28 ], [ 49, 26 ], [ 38, 21 ] ]
AssaultRifleTime = 0.121

LR300AssaultRifle = [ [ -2, 25 ], [ -6, 31 ], [ -10, 33 ], [ -14, 31 ], [ -15, 25 ], [ -14, 20 ], [ -9, 17 ], [ -2, 15 ], [ 9, 12 ], [ 17, 10 ], [ 20, 8 ], [ 17, 7 ], [ 10, 5 ], [ 0, 4 ], [ -5, 4 ], [ -9, 4 ], [ -12, 3 ], [ -14, 3 ], [ -15, 3 ], [ -15, 2 ], [ -14, 2 ], [ -13, 2 ], [ -10, 2 ], [ -7, 2 ], [ -3, 2 ], [ 13, 2 ], [ 30, 2 ], [ 36, 3 ], [ 30, 3 ] ]
LR300AssaultRifleTime = 0.110

Thompson = [ [ -15, 33 ], [ -5, 32 ], [ 3, 31 ], [ 11, 29 ], [ 13, 26 ], [ 10, 22 ], [ 2, 18 ], [ -7, 16 ], [ -13, 14 ], [ -13, 13 ], [ -7, 11 ], [ 2, 10 ], [ 10, 9 ], [ 12, 8 ], [ 11, 7 ], [ 5, 7 ], [ -2, 6 ], [ -6, 6 ], [ -7, 6 ] ]
ThompsonTime = 0.120

MP5A4 = [ [ 0, 40 ], [ 0, 29 ], [ 0, 33 ], [ 12, 33 ], [ 29, 29 ], [ 33, 22 ], [ 23, 13 ], [ 0, 10 ], [ -18, 9 ], [ -25, 8 ], [ -19, 7 ], [ -3, 6 ], [ 7, 5 ], [ 14, 4 ], [ 16, 4 ], [ 16, 3 ], [ 12, 2 ], [ 6, 2 ], [ -1, 1 ], [ -5, 1 ], [ -8, 0 ], [ -10, 0 ], [ -12, 0 ], [ -13, 0 ], [ -13, 0 ], [ -12, 0 ], [ -11, 0 ], [ -8, 0 ], [ -5, 0 ] ]
MP5A4Time = 0.11

CustomSMG = [ [ -13, 27 ], [ -6, 27 ], [ 0, 26 ], [ 6, 25 ], [ 10, 23 ], [ 11, 21 ], [ 9, 18 ], [ 4, 16 ], [ -3, 14 ], [ -9, 13 ], [ -11, 12 ], [ -10, 10 ], [ -6, 9 ], [ 0, 9 ], [ 6, 8 ], [ 9, 7 ], [ 10, 6 ], [ 9, 6 ], [ 4, 5 ], [ 0, 5 ], [ -4, 5 ], [ -6, 5 ], [ -5, 5 ] ]
CustomSMGTime = 0.09

M249 = [ [ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ],[ 0, 35 ] ] 
M249Time = 0.120
with open('settings') as json_file:
    data = json.load(json_file)
    sensitivity = float(data['sensitivity'])


def ispressedchangenum():
    global guntype
    global timer
    a = win32api.GetKeyState(0x61)
    if a < 0:
        guntype=AssaultRifle
        timer=AssaultRifleTime
    b = win32api.GetKeyState(0x62)
    if b < 0:
        guntype=LR300AssaultRifle
        timer=LR300AssaultRifleTime
    c = win32api.GetKeyState(0x63)
    if c < 0:
        guntype=Thompson
        timer=ThompsonTime
    d = win32api.GetKeyState(0x64)
    if d < 0:
        guntype=MP5A4
        timer=MP5A4Time
    e = win32api.GetKeyState(0x65)
    if e < 0:
        guntype=CustomSMG
        timer=CustomSMGTime
    f = win32api.GetKeyState(0x66)
    if f < 0:
        guntype=M249
        timer=M249Time
    return

def menu():
    global guntype
    global timer
    i=1
    for x in guns:
        print(f'{i} - {x}')
        i+=1
    print("0 - None")
def ispressed():
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    if a < 0 and b < 0:
        return True
def ispressednumbar():
    global guntype
    a = win32api.GetKeyState(0x60)
    if a < 0:
        guntype = 0
        loop()
def move(x,y):
    global lost
    ctypes.windll.user32.mouse_event(0x0001, x, y, 0,0)
    millis2 = int(round(time.time() * 1000))
    lost +=(millis2-millis)/1000
lost = 0
millis=0
def godown(guntype,timer):
    global millis
    global lost
    lost = 0
    for x in guntype:
        truex=((x[0]/2)/sensitivity)
        truey=((x[1]/2)/sensitivity)
        millis = int(round(time.time() * 1000))
        for x in range(8):
            movex=(truex/8)
            movey=(truey/8)
            move(int(movex),int(movey))
            time.sleep((timer/8))
        millis2 = int(round(time.time() * 1000))
        # print((millis2-millis)/1000)
        lost = 0
        # lostx=(truex%4)
        # losty=(truey%4)
        # move(int(lostx),int(losty))
        if not ispressed():
            return
        # time.sleep(timer-lost)
        lost = 0
def loop():
    while guntype == 0:
        ispressedchangenum()
    while guntype != 0:
        ispressedchangenum()
        ispressednumbar()
        if ispressed():
            godown(guntype,timer)
menu()
loop()