import random
#imports the methods into this namespace, less typing
from player import *


def change_room():
    pass

def r1():
    #code for whatever happens in each room 
    pass

def r2():
    pass



###########################  Setup game here ###########

############### Load the rooms #############
room =[]       
roomslist=[]
 
##############  convert to a list of lists ######################
for line in open("rooms.csv"):
    line = line.strip('\n')         # lose the newline characters
    room = line.split(",")          # single room
    roomslist.append(room)          # all the rooms
 
###############  make into a dictionary ######################
keys = []
number_of_rooms = (len(roomslist))
for i in range(number_of_rooms):
    keys.append(i)
rooms = dict(zip(keys, roomslist)) 

############### ############Start a player ######################
    
player = Player('Arlin', 'Living Room')
print (player.info())

############################ Game Loop #########################

while True:
    pass
