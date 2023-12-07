from player import Player
from appliance import Appliance
from customer import Customer
import sys

import pygame


# Initialize Pygame

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Input Example")

class game:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.burrito_timer = 0

        self.player = Player() 
        self.burrito = Appliance(4, "burrito", "burrito maker")
        self.chips = Appliance(2, "burrito", "burrito maker")
        self.customer = Customer()

    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        #logic for the cars' response to keystrokes
        
            
    def run(self):
        running = True
        while running:
           self.burrito_timer += self.clock.tick(120)
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                # Check for specific keys
                    if event.key == pygame.K_LEFT:
                        print("Left arrow key pressed")
                    elif event.key == pygame.K_RIGHT:
                        print("Right arrow key pressed")
                    elif event.key == pygame.K_UP:
                        print("Up arrow key pressed")
                    elif event.key == pygame.K_DOWN:
                        print("Down arrow key pressed")
                    elif event.key == pygame.K_SPACE:
                        print("Spacebar pressed")
                    elif event.key == pygame.K_b:
                        if self.burrito.get_state() == "mt":
                            self.burrito_timer = 0 
                            self.burrito.update("int")
                elif self.burrito.get_state() == "ck" and self.burrito_timer > 5000:
                    self.burrito.update("tu")
                    print("ok")
                    

           

if __name__ == "__main__":
    g = game()
    g.run()