''' A simple start to a text maze game with a single path thru the maze
Players have to choose the correct direction to get out of a room.

This also is an introduction to making objects in Python.
'''

class Player:

    
    
    def __init__ (self, name, room):
        self.things = ['marshmallow']   #list of objects
        self.visited=[]
        self.commands =['eat', 'hit']
        self.lifes = 2
        self.name = name
        self.room = room
        self.action = {'hit':'You hit the cat with a marshmallow',\
         'eat':'You eat the marshmallow'}
        self.numberOfRooms = 10
        
    def info(self):
        print ('Hi {}.  Your room {}. You have {} lifes left \n' \
        .format(self.name, self.room, self.lifes))
        print ('*'* 60)
        
    def change_room(self):
         if self.room == 10:
             self.win()
         else:
             self.room += 1  # use this if you want to go from room 1 to 2 to 3.  Change for random rooms
             self.visited.append(self.room) #where I have already been
             if 1 in self.visited:
                print ("You have already been to this room and there is nothing to be found here.")
                self.change_room()
             else:
                 print(" ")
         return (self.room)

    def take(self, thing):
        pass
        
    def inventory(self):
        print (self.things)
        
    def win(self):
        print ('Congratulations, You have completed the maze')
        #play again?

    def lose(self):
        self.lifes = self.lifes -1
        if self.lifes == 0:
            print ('Sorry Jack, Your dead!')

    def mallow(self, action):
        action = str.lower(action)
        print (self.action[action] + '\n\n')
            
 
