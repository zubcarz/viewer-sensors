# Sensor Viewer
# Author : zubcarz@gmail.com

import serial
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
import time
import datetime
import atexit
import os, sys
import threading

def pressKey():
	signal = 6
	while True:    # infinite loop
		keyPress = raw_input("Key Instruction :")
		printAction(keyPress)
		signal = int(keyPress)
		if ser.isOpen():
			ser.write(str(signal) + '\r')
		time.sleep(0.2)

def printAction(action):
	if action == "0":
		print("HallSimple")
	elif action == "1":
		print("HallCompleted")
	elif action == "2":
		print("ReedSwitchSimple")
	elif action == "3":
		print("ReedSwitchCompleted")
	elif action == "4":
		print("FlowSensor")
	elif action == "5":
		print("FlowSensorCumulative")
	elif action == "6":
		print("FlowSeonsorSpeed")
	elif action == "7":
		print("Stop")
	elif action == "8":
		print("Speed 1")
	elif action == "9":
		print("Speed 2")
	elif action == "10":
		print("Speed 3")
	elif action == "11":	
		print("Pwm Dinamic")
	else:
		print("Unknow Action")


def exit_handler():
	stream.close()
	print 'Sensor Viewer Close!'

def enum(**enums):
    return type('Enum', (), enums)

atexit.register(exit_handler)

Modes = enum(
	HallSimple = 0,
	HallCompleted = 1,
	ReedSwitchSimple = 2,
	ReedSwitchCompleted = 3,
	FlowSensor = 4,
	FlowSensorCumulative = 5,
	FlowSensorSpeed = 6,
	Stop = 7,
	Speed1 = 8,
	Speed2 = 9,
	Speed3 = 10,
	PWMDinamic = 11
)

username = 'c.zubieta'
api_key = 'HOI7Hy0aPK6oRWXjlYP1'
stream_token = '46ul5ckyga'

#username = 'zubcarz'
#api_key = 'xanoTynG94z8fJCcIFEk'
#stream_token = 'kl5dognpno'

#serialPort = '/dev/cu.usbmodem1411'
serialPort = '/dev/ttyACM0'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=50
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Hall Effect Data',
    yaxis=dict(
        autorange=True,
        autotick=True,
        ticks='',
        #range=[100, 900]
    )
)

fig = Figure(data=[trace1], layout=layout)
py.plot(fig, filename='Raspberry Pi Streaming Example Values')
stream = py.Stream(stream_token)
stream.open()

threads = list()
t = threading.Thread(target=pressKey)
threads.append(t)
t.start()

with serial.Serial( serialPort, 9600, timeout=1) as ser:
		while True:
			try:
				#value = int(str(ser.readline(),"utf-8").strip())
				value = int(ser.readline()[:-2].decode())
				timeX = int(round(time.time() * 1000))

				print(value)

				ser.flushInput()
				ser.flushOutput()
				
				# Write Plot
				stream.write({'x': timeX, 'y': value})

			except ValueError:
				value = ser.readline()[:-2].decode()	
				print("Value Error : " + value)

			time.sleep(0.2) # delay between stream posts
