import pygame 
from fsm import FSM
import time 
class Appliance(pygame.sprite.Sprite):
    #States
    COOKING = "ck"
    READY = "rdy"
    EMPTY = "mt"

    #Inputs
    INTERACT = "int"
    TIMER_UP = "tu"

    def __init__(self, time, food, name):
        self.time = time 
        self.food = food
        self.name = name
        self.timer_duration = time

        self.fsm = FSM(self.EMPTY)
        self.init_fsm()

    def init_fsm(self):
        self.fsm.add_transition(self.INTERACT, self.EMPTY, self.food_cooking, self.COOKING)
        self.fsm.add_transition(self.TIMER_UP, self.COOKING, self.food_ready, self.READY)
        self.fsm.add_transition(self.INTERACT, self.READY, self.food_collected, self.EMPTY)


        
                

        
    def update(self, key):
        if key == "int":
            self.fsm.process(self.INTERACT)
        elif key == "tu":
            self.fsm.process(self.TIMER_UP)
                
                
    def food_ready(self):
        print (self.name + " Ready")
    def food_collected(self):
        print ("Picked up " + self.name)
    def food_cooking(self):
        print(self.name + " Cooking...")
    def get_state(self):
        return self.fsm.current_state