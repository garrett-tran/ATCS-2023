from appliance import Appliance
from customer import Customer
import pygame

class game:
    appliances = pygame.sprite.Group()
    BACKGROUND_COLOR = (196, 164, 132)

    def __init__(self):
        pygame.init()
        self.customer = Customer()

        #Starts clock for appliances to reference off of
        self.clock = pygame.time.Clock()
        self.timer = 2001
        self.inventory = []
        

        #Initialzing appliances with their name, item, and position
        self.burrito = Appliance(4, "Burrito", "Burrito (b)", (0,0))
        self.chips = Appliance(2, "Chips", "Chips (c)", (1,0))
        self.rice = Appliance(3, "Rice", "Rice (r)", (2,0))
        self.tortilla = Appliance(1, "Tortilla", "Tortilla (t)", (3,0))
        self.cheese = Appliance(2, "Cheese", "Cheese (e)", (3,1))
        self.quesadilla = Appliance(4, "Quesadilla", "Quesadilla (q)", (0,1))
        self.drink = Appliance(2, "Drink", "Drink (d)", (0,2))

        self.appliances = []
        self.appliances.append(self.burrito)
        self.appliances.append(self.chips)
        self.appliances.append(self.rice)
        self.appliances.append(self.tortilla)
        self.appliances.append(self.cheese)
        self.appliances.append(self.quesadilla)
        self.appliances.append(self.drink)


        #Values for how much money you can seel each item for
        self.money = 0
        self.values = {"Burrito": 10, "Chips": 5, "Quesadilla": 8, "Drink": 3}

        # Setting up elements of the main game display
        width, height = 800, 600
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chipotle Game")
        background_image_path = "Chipotle Game/images/chipotle_logo.png"
        self.background_image = pygame.transform.scale(pygame.image.load(background_image_path), (200, 200))
        formulas_path = "Chipotle Game/images/food_formulas.png" 
        self.formulas_image = pygame.transform.scale(pygame.image.load(formulas_path), (240, 100))
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
                #Update Screen every tick
                self.screen.fill(self.BACKGROUND_COLOR)
                self.draw_table()
                self.draw_background()
                self.draw_text()
                for a in self.appliances:
                    a.draw(self.screen)
                

                #Logic for customer how long customer says "Thank you" after recieving order
                if self.timer - self.text_time > 2000:
                    self.customer.draw(self.screen, False)
                else:
                    self.customer.draw(self.screen, True)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    #Logic for interacting with each appliance
                    if event.key == pygame.K_b:
                        if "Tortilla" in self.inventory and "Rice" in self.inventory:
                            if self.burrito.get_state() == "mt":
                                self.burrito_timer = self.timer
                                self.burrito.update("int")
                                self.inventory.remove("Tortilla")
                                self.inventory.remove("Rice")
                        if self.burrito.get_state() == "rdy":
                            self.burrito.update("int")
                            self.inventory.append("Burrito")
                    if event.key == pygame.K_c:
                        if self.chips.get_state() == "mt":
                            self.chips_timer = self.timer
                            self.chips.update("int")
                        if self.chips.get_state() == "rdy":
                            self.chips.update("int")
                            self.inventory.append("Chips")
                    if event.key == pygame.K_r:
                        if self.rice.get_state() == "mt":
                            self.rice_timer = self.timer
                            self.rice.update("int")
                        if self.rice.get_state() == "rdy":
                            self.rice.update("int")
                            self.inventory.append("Rice")
                    if event.key == pygame.K_t:
                        if self.tortilla.get_state() == "mt":
                            self.tortilla_timer = self.timer
                            self.tortilla.update("int")
                        if self.tortilla.get_state() == "rdy":
                            self.tortilla.update("int")
                            self.inventory.append("Tortilla")
                    if event.key == pygame.K_e:
                        if self.cheese.get_state() == "mt":
                            self.cheese_timer = self.timer
                            self.cheese.update("int")
                        if self.cheese.get_state() == "rdy":
                            self.cheese.update("int")
                            self.inventory.append("Cheese")
                    if event.key == pygame.K_d:
                        if self.drink.get_state() == "mt":
                            self.drink_timer = self.timer
                            self.drink.update("int")
                        if self.drink.get_state() == "rdy":
                            self.drink.update("int")
                            self.inventory.append("Drink")
                    if event.key == pygame.K_q:
                        if "Tortilla" in self.inventory and "Cheese" in self.inventory:
                            if self.quesadilla.get_state() == "mt":
                                self.quesadilla_timer = self.timer
                                self.quesadilla.update("int")
                                self.inventory.remove("Tortilla")
                                self.inventory.remove("Cheese")
                        if self.quesadilla.get_state() == "rdy":
                            self.quesadilla.update("int")
                            self.inventory.append("Quesadilla")


                    #Logic for fufilling order
                    if event.key == pygame.K_f:
                        in_list = False
                        for i in range (len(self.inventory)):
                            if self.inventory[i] == order:
                                self.current_time +=5000
                                self.inventory.pop(i)
                                self.money += self.values[order]
                                self.text_time = self.timer
                                order = self.customer.place_order()
                                in_list = True
                                break
                        if in_list == False:
                            self.current_time -= 5000
                #Logic for the game timer counting down
                elif event.type == self.timer_event:
                    # Decrease the current time
                    self.current_time -= 1000
                    seconds = self.current_time/1000
                    timer_text = seconds
                    self.timer_surface = self.font.render(str(timer_text), True, self.text_color)
                    

                    if self.current_time <= 0:
                        running = False
                        print("Time's up!")
                        print("Profit: $" + str(self.money))

            #Logic that handles the cooking times for each appliance         
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
                
    #Methods that draw each element of the scene
    def draw_table(self):
        pygame.draw.rect(self.screen, "black", (200, 200, 400, 400))
        pygame.draw.rect(self.screen, "white", (300, 300, 200, 200))
    def draw_background(self):
        self.screen.blit(self.background_image, (300, 300))
        self.screen.blit(self.formulas_image, (200, 100))
    def draw_text(self):
        self.screen.blit(self.timer_surface, (0,50))
        self.screen.blit(self.font.render("Profit: $" + str(self.money), True, self.text_color), (0, 100))
        self.screen.blit(self.font.render("Inventory" + str(self.inventory), True, self.text_color), (0, 0))
        self.screen.blit(self.font.render("Fulfill Order (f)", True, self.text_color), (320, 375))
           

if __name__ == "__main__":
    g = game()
    g.run()

