from player import Player
from appliance import Appliance
from customer import Customer
import sys

import pygame

class game:
    BACKGROUND_COLOR = (255, 255, 255)
    # Initialize Pygame

    
    #sprites
    appliances = pygame.sprite.Group()
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.timer = 0
        

        self.inventory = []
        self.player = Player() 
        self.burrito = Appliance(4, "burrito", "burrito maker", 0)
        self.chips = Appliance(2, "chips", "chips maker", 1)
        self.customer = Customer()

        # Set up the display
        width, height = 800, 600
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pygame Input Example")
        
        
            
    def run(self):
        running = True
        order = self.customer.place_order()
        while running:
            self.timer += self.clock.tick(120)
            if self.timer > 120:
                self.screen.fill(self.BACKGROUND_COLOR)
                self.draw_table()
                self.burrito.draw(self.screen)
                self.chips.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    # Check for specific keys
                    if event.key == pygame.K_b:
                        if self.burrito.get_state() == "mt":
                            self.burrito_timer = self.timer
                            self.burrito.update("int")
                        elif self.burrito.get_state() == "rdy":
                            self.burrito.update("int")
                            self.inventory.append("burrito")
                    if event.key == pygame.K_c:
                        if self.chips.get_state() == "mt":
                            self.chips_timer = self.timer
                            self.chips.update("int")
                        elif self.chips.get_state() == "rdy":
                            self.chips.update("int")
                            self.inventory.append("chips")
                    if event.key == pygame.K_f:
                        for i in range (len(self.inventory)):
                            if self.inventory[i] == order:
                                self.customer.receive_order()
                                self.inventory.pop(i)
                                order = self.customer.place_order()
                                break
            if self.burrito.get_state() == "ck" and self.timer - self.burrito_timer > 5000:
                self.burrito.update("tu")
            elif self.chips.get_state() == "ck" and self.timer - self.chips_timer > 2000:
                self.chips.update("tu")
                
    def draw_table(self):
        pygame.draw.rect(self.screen, "black", (200, 200, 400, 400))
        pygame.draw.rect(self.screen, "white", (300, 300, 200, 200))

           

if __name__ == "__main__":
    g = game()
    g.run()