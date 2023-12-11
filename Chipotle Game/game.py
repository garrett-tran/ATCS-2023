from player import Player
from appliance import Appliance
from customer import Customer
import sys

import pygame

class game:
    BACKGROUND_COLOR = (196, 164, 132)
    # Initialize Pygame

    
    #sprites
    appliances = pygame.sprite.Group()
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.timer = 2001
        self.player = Player() 
        self.inventory = []
        

        
        self.burrito = Appliance(4, "burrito", "burrito maker", (0,0))
        self.chips = Appliance(2, "chips", "chips maker", (1,0))
        self.rice = Appliance(3, "rice", "rice cooker", (2,0))
        self.tortilla = Appliance(1, "tortilla", "tortilla press", (3,0))
        self.cheese = Appliance(2, "cheese", "cheese grater", (3,1))
        self.quesadilla = Appliance(4, "quesadilla", "quesadilla oven", (0,1))
        self.drink = Appliance(2, "drink", "drink machine", (0,2))

        self.appliances = []
        self.appliances.append(self.burrito)
        self.appliances.append(self.chips)
        self.appliances.append(self.rice)
        self.appliances.append(self.tortilla)
        self.appliances.append(self.cheese)
        self.appliances.append(self.quesadilla)
        self.appliances.append(self.drink)

        self.customer = Customer()
        self.money = 0
        self.values = {"burrito": 10, "chips": 5, "quesadilla": 8, "drink": 3}

        # Set up the display
        width, height = 800, 600
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chipotle Game")
        background_image_path = "Chipotle Game/images/chipotle_logo.png"  # Replace with the path to your background image file
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, (200, 200))

        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 35)
        
        #Timer Setup
        start_time = 60  # seconds
        self.current_time = start_time * 1000  # convert to milliseconds
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000) 
        seconds = self.current_time/1000
        timer_text = seconds
        self.timer_surface = self.font.render(str(timer_text), True, self.text_color)
        
        
            
    def run(self):
        running = True
        order = self.customer.place_order()
        self.text_time = 0
        while running:
            self.timer += self.clock.tick(120)
            
            if self.timer > 120:
                self.screen.fill(self.BACKGROUND_COLOR)
                self.draw_table()
                self.draw_background()
                for a in self.appliances:
                    a.draw(self.screen)
                
                self.draw_text()
                if self.timer - self.text_time > 2000:
                    self.customer.draw(self.screen, False)
                else:
                    self.customer.draw(self.screen, True)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    # Check for specific keys
                    if event.key == pygame.K_b:
                        if "tortilla" in self.inventory and "rice" in self.inventory:
                            if self.burrito.get_state() == "mt":
                                self.burrito_timer = self.timer
                                self.burrito.update("int")
                                self.inventory.remove("tortilla")
                                self.inventory.remove("rice")
                        if self.burrito.get_state() == "rdy":
                            self.burrito.update("int")
                            self.inventory.append("burrito")
                    if event.key == pygame.K_c:
                        if self.chips.get_state() == "mt":
                            self.chips_timer = self.timer
                            self.chips.update("int")
                        if self.chips.get_state() == "rdy":
                            self.chips.update("int")
                            self.inventory.append("chips")
                    if event.key == pygame.K_r:
                        if self.rice.get_state() == "mt":
                            self.rice_timer = self.timer
                            self.rice.update("int")
                        if self.rice.get_state() == "rdy":
                            self.rice.update("int")
                            self.inventory.append("rice")
                    if event.key == pygame.K_t:
                        if self.tortilla.get_state() == "mt":
                            self.tortilla_timer = self.timer
                            self.tortilla.update("int")
                        if self.tortilla.get_state() == "rdy":
                            self.tortilla.update("int")
                            self.inventory.append("tortilla")
                    if event.key == pygame.K_e:
                        if self.cheese.get_state() == "mt":
                            self.cheese_timer = self.timer
                            self.cheese.update("int")
                        if self.cheese.get_state() == "rdy":
                            self.cheese.update("int")
                            self.inventory.append("cheese")
                    if event.key == pygame.K_d:
                        if self.drink.get_state() == "mt":
                            self.drink_timer = self.timer
                            self.drink.update("int")
                        if self.drink.get_state() == "rdy":
                            self.drink.update("int")
                            self.inventory.append("drink")
                    if event.key == pygame.K_q:
                        if "tortilla" in self.inventory and "cheese" in self.inventory:
                            if self.quesadilla.get_state() == "mt":
                                self.quesadilla_timer = self.timer
                                self.quesadilla.update("int")
                                self.inventory.remove("tortilla")
                                self.inventory.remove("cheese")
                        if self.quesadilla.get_state() == "rdy":
                            self.quesadilla.update("int")
                            self.inventory.append("quesadilla")


                    #Logic for fufilling order
                    if event.key == pygame.K_f:
                        in_list = False
                        for i in range (len(self.inventory)):
                            if self.inventory[i] == order:
                                self.current_time +=2000
                                self.customer.receive_order()
                                self.inventory.pop(i)
                                self.money += self.values[order]
                                self.text_time = self.timer
                                order = self.customer.place_order()
                                in_list = True
                                break
                        if in_list == False:
                            self.current_time -= 5000
                elif event.type == self.timer_event:
                    # Decrease the current time
                    self.current_time -= 1000
                    seconds = self.current_time/1000
                    timer_text = seconds
                    self.timer_surface = self.font.render(str(timer_text), True, self.text_color)
                    

                    if self.current_time <= 0:
                    # Timer reached zero, you can handle this event as needed
                        running = False
                        print("Time's up!")
                        running = False
            if self.burrito.get_state() == "ck" and self.timer - self.burrito_timer > self.burrito.time*1000:
                self.burrito.update("tu")
            elif self.chips.get_state() == "ck" and self.timer - self.chips_timer > self.chips.time*1000:
                self.chips.update("tu")
            elif self.rice.get_state() == "ck" and self.timer - self.rice_timer > self.rice.time*1000:
                self.rice.update("tu")
            elif self.tortilla.get_state() == "ck" and self.timer - self.tortilla_timer > self.tortilla.time*1000:
                self.tortilla.update("tu")
            elif self.cheese.get_state() == "ck" and self.timer - self.cheese_timer > self.cheese.time*1000:
                self.cheese.update("tu")
            elif self.quesadilla.get_state() == "ck" and self.timer - self.quesadilla_timer > self.quesadilla.time*1000:
                self.quesadilla.update("tu")
            elif self.drink.get_state() == "ck" and self.timer - self.drink_timer > self.drink.time*1000:
                self.drink.update("tu")
                
    def draw_table(self):
        pygame.draw.rect(self.screen, "black", (200, 200, 400, 400))
        pygame.draw.rect(self.screen, "white", (300, 300, 200, 200))
    def draw_background(self):
        self.screen.blit(self.background_image, (300, 300))
    def draw_text(self):
        self.screen.blit(self.timer_surface, (0,50))
        self.screen.blit(self.font.render("Profit: $" + str(self.money), True, self.text_color), (0, 100))
        self.screen.blit(self.font.render("Inventory" + str(self.inventory), True, self.text_color), (0, 0))

           

if __name__ == "__main__":
    g = game()
    g.run()