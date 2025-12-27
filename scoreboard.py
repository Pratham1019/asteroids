import pygame

WHITE = (255, 255, 255)

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.position = (x, y)
        self.image = None
        self.rect = None
        self.re_render()
        
    def re_render(self):
        self.image = self.font.render(f"Score: {self.score}", True, WHITE)
        self.rect = self.image.get_rect(topleft=self.position)
    
    def update_score(self, points):
        self.score += points
        self.re_render()

    def draw(self, screen):
        screen.blit(self.image, self.rect)