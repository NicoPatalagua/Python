#!/usr/bin/env python

from picar import front_wheels
from picar import back_wheels
import time
import picar

import bluetooth


host = ""
port = 1

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Socket de Bluetooth creado')
try:
    server.bind((host, port))
    print("Binding completo")
except:
    print("Binding incompleto")

server.listen(1)
cliente, direccion = server.accept()
print("Conectado a:", direccion)
print("Cliente:", cliente)

#dato = cliente.recv(1024)
#print(dato)


picar.setup()

forward_speed = 80
backward_speed = 70
turning_angle = 40

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

fw.ready()
bw.ready()
fw.turning_max = 45

def reve():
    bw.stop()
    bw.forward()
    bw.speed=50
def adela():
    bw.stop()
    bw.backward()
    bw.speed=50
def derecha():
    fw.turn_right()
def izquierda():
    fw.turn_left()
def centro():
    fw.turn_straight()
def parar():
    bw.stop()
    centro()
    
    
if  __name__ ==  '__main__' :
    print("start_follow")
    while True:
    
        #reve()
        dato = cliente.recv(1024)
        if dato== "a":
            adela()
        if dato== "r":
            reve()
        if dato== "d":
            derecha()
        if dato== "i":
            izquierda()
        if dato== "c":
            centro()
        if dato== "s":
            parar()
        print(dato)
