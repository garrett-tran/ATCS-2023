import pygame 
from fsm import FSM

class Appliance(pygame.sprite.Sprite):
    
    #States
    COOKING = "ck"
    READY = "rdy"
    EMPTY = "mt"

    #Inputs
    INTERACT = "int"
    TIMER_UP = "tu"

    def __init__(self, time, food, name, position):
        super().__init__()
        self.time = time 
        self.food = food
        self.name = name
        self.color = "gray"
        self.timer_duration = time
        self.position = position
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 20)
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
        print (self.food + " Ready")
        self.color = "green"
    def food_collected(self):
        print ("Picked up " + self.food)
        self.color = "grey"
    def food_cooking(self):
        print(self.name + " Cooking...")
        self.color = "yellow"
    def get_state(self):
        return self.fsm.current_state
    
    def draw(self, screen):
        x = 200+100*self.position
        y = 500
        text_surface = self.font.render(self.name, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x+50, y+50)
        pygame.draw.rect(screen, self.color, (x, y, 100, 100))
        screen.blit(text_surface, text_rect)
        
        
        