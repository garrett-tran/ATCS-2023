import random 
import pygame
class Customer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.order = None
        
        #Speech bubble setup
        bubble_path = "Chipotle Game/images/speech_bubble.png"  # Replace with the path to your image file
        self.speech_bubble = pygame.transform.scale(pygame.image.load(bubble_path), (200, 200))
        self.bubble_rect = self.speech_bubble.get_rect()
        self.bubble_rect.center = (675, 100)

        #Customer Icon Setup
        smile_path = "Chipotle Game/images/smile.png"  # Replace with the path to your image file
        self.smile = pygame.transform.scale(pygame.image.load(smile_path), (60, 60))
        self.smile_rect = self.speech_bubble.get_rect()
        self.smile_rect.center = (625, 240)

        #Text Setup
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 15)
        self.text_surface = self.font.render(self.order, True, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (600,85)
        

    def place_order(self):
        menu = ["Chips", "Burrito", "Quesadilla", "Drink"]
        self.order = random.choice(menu)
        self.text_surface = self.font.render(f"I would like one {self.order}.", True, self.text_color)
        print(f"I would like one {self.order}.")
        return self.order

    def receive_order(self):
        print(f"Customer received {self.order}. Enjoy!")
    
    def draw(self, screen, thanks=False):
        
        screen.blit(self.speech_bubble, self.bubble_rect)
        screen.blit(self.smile, self.smile_rect)
        if thanks == False:
            self.text_surface = self.font.render(f"I would like one {self.order}.", True, self.text_color)
            screen.blit(self.text_surface, self.text_rect)
        else:
            self.text_surface = self.font.render("Thank you!", True, self.text_color)
            screen.blit(self.text_surface, self.text_rect)


        