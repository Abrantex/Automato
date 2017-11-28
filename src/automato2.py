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
	print('init - BCiRiGiS0')

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
	print('state1 - BCiRiGiS1')

	global state
	global newEvent

	while True:
		if newEvent == 'greenLoad':
			newEvent = 'none'
			state = state2
			break

def state2():
	print('state2 - BCwRiGwS2')

	global state
	global newEvent

	sendMovement(1) #greenLoad

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state3
			break
def state3():
	print('state3 - BCiRiGwS3')

	global state
	global newEvent

	while True:
		if (newEvent == 'greenNew') + (newEvent == 'redNew'):
			newEvent = 'none'
			state = state11
			break
		elif newEvent == 'greenDone':
			newEvent = 'none'
			state = state4
			break
def state4():
	print('state - BCiRiGiS4')

	global state
	global newEvent

	while True:
		if newEvent == 'greenUnload':
			newEvent = 'none'
			state = state5
			break

def state5():
	print('state - BCwRiGiS5')

	global state
	global newEvent

	sendMovement(3) #greenUnload	

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init
			break

def state6():
	print('state - BCiRiGiS6')

	global state
	global newEvent

	while True:
		if newEvent == 'redLoad':
			newEvent = 'none'
			state = state7
			break

def state7():
	print('state - BCwRwGiS7')

	global state
	global newEvent

	sendMovement(0) #redLoad		

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state8
			break
def state8():
	print('state - BCiRwGiS8')

	global state
	global newEvent

	while True:
		if newEvent == 'greenNew' or newEvent == 'redNew':
			newEvent = 'none'
			state = state12
			break
		elif newEvent == 'redDone':
			newEvent = 'none'
			state = state9
			break


def state9():
	print('state - BCiRiGiS9')

	global state
	global newEvent

	while True:
		if newEvent == 'redUnload':
			newEvent = 'none'
			state = state10
			break

def state10():
	print('state - BCwRiGiS10')

	global state
	global newEvent

	sendMovement(2) #redUnload	

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init
			break

def state11():
	print('state - BCiRiGwS11')

	global state
	global newEvent
	

	while True:
		if newEvent == 'redLoad':
			sendMovement(0) #redLoad
			newEvent = 'none'
			state = state13
			break

def state12():
	print('state - BCiRwGiS12')

	global state
	global newEvent
	
	

	while True:
		if newEvent == 'greenLoad':
			sendMovement(1) #greenLoad
			newEvent = 'none'
			state = state13
			break


def state13():
	print('state - BCwRwGwS13')

	global state
	global newEvent

		

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state14
			break

def state14():
	print('state - BCiRwGwS14')

	global state
	global newEvent
	

	while True:
		if newEvent == 'redDone':
			newEvent = 'none'
			state = state15
			break
		if newEvent == 'greenDone':
			newEvent = 'none'
			state = state17
			break
def state15():
	print('state - BCiRiGwS15')

	global state
	global newEvent
	

	while True:
		if newEvent == 'redUnload':
			newEvent = 'none'
			state = state16
			break

def state16():
	print('state - BCwRiGwS16')

	global state
	global newEvent

	sendMovement(2) #redUnload	

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state3
			break
def state17():
	print('state - BCiRwGiS17')

	global state
	global newEvent
	

	while True:
		if newEvent == 'greenUnload':
			newEvent = 'none'
			state = state18
			break
def state18():
	print('state - BCwRwGiS18')

	global state
	global newEvent

	sendMovement(3) #greenUnload	

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = state8
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
