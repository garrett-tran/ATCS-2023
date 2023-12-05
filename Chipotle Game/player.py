import random
import pygame

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def pick_up_food(self, appliance):
        food = appliance.food
        if appliance.get_state == "rdy":
            appliance.pick_up()
            self.inventory.append(appliance.food)
            print(f"{self.name} picked up {food}.")

    def cook(self, appliance):
        if appliance.get_state == "mt":
            appliance.cook()
