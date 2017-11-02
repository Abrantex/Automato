#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AUTOMATO DE EVENTOS NÃO CONTROLÁVEIS

import rospy
from std_msgs.msg import Int8
from std_msgs.msg import String



#######################################
### FUNÇÕES DE CALLBACK - NÃO MEXER ###
#######################################

# Callback para novo evento
def eventCallback(data):
	print('eventCallback')
	global newEvent

	newEvent = data.data


# Função que manda índice de movimento para o Cyton
def sendMovement(move):
	print('sendMovement')
	print(move)
	global pub
	moveToSend = Int8()
	moveToSend = move
	pub.publish(moveToSend)


###########################################
### LISTA DE ESTADOS - EDITE ESTA PARTE ###
###########################################

# Exemplo de estado inicial

def init():
	print('init')

	global state
	global newEvent

	while True:
		if newEvent == 'greenNew':
			newEvent = 'none'
			state = state1
			break
		elif newEvent == 'redNew':
			newEvent = 'none'
			state = state6
			break
	
def state1():
	print('state1')
	global state
	global newEvent

	#sendMovement(2)

	while True:
		if newEvent == 'greenLoad':
			newEvent = 'none'
			state = state2
			break

def state2():
	print('state2')
	global state
	global newEvent

	sendMovement(1)

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state3
			break
def state3():
	print('state3')
	global state
	global newEvent


	while True:
		if newEvent == 'greenDone':
			newEvent = 'none'
			state = state4
			break
def state4():
	print('state4')
	global state
	global newEvent


	while True:
		if newEvent == 'greenUnload':
			newEvent = 'none'
			state = state5
			break

def state5():
	print('state5')
	global state
	global newEvent

	sendMovement(3) #greenUnload

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init
			break


def state6():
	print('state6')
	global state
	global newEvent


	while True:
		if newEvent == 'redLoad':
			newEvent = 'none'
			state = state7
			break

def state7():
	print('state7')
	global state
	global newEvent

	sendMovement(0)

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state8
			break

def state8():
	print('state8')
	global state
	global newEvent



	while True:
		if newEvent == 'redDone':
			newEvent = 'none'
			state = state9
			break

def state9():
	print('state9')
	global state
	global newEvent


	while True:
		if newEvent == 'redUnload':
			newEvent = 'none'
			state = state10
			break



def state10():
	print('state10')
	global state
	global newEvent

	sendMovement(2)

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init
			break

###################################################
### DECLARAÇÃO DE VARIÁVEIS GLOBAIS - NÃO MEXER! ###
###################################################


state = init
newEvent = 'none'


##############################
### LOOP MAIN - NÃO MEXER! ###
##############################

def main():
	global state
	global pub

	rospy.init_node('automato', anonymous=False)
	pub = rospy.Publisher('move', Int8, queue_size = 10)
	rospy.Subscriber('event', String, eventCallback)

	rospy.sleep(1)

	while not rospy.is_shutdown():
		state()



if __name__ == '__main__':
	main()
