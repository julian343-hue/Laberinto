from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x  < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
     def update(self):
          if self.rect.x <= 470:
               self.direction = "derecha"
          if self.rect.x >= win_width - 85:
               self.direction = "izquierda"

          if self.direction == "izquierda":
               self.rect.x -= self.speed
          else:
               self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self. color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_hei):
        super().__init__()
        self.color1 = color1
        self.width = wall_width
        self.height = player_x
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))




def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Escena del juego:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

packman = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(154, 285, 50, 100, 20, 450, 10)
w2 = Wall(154, 285, 50, 100, 400, 350, 10)
w3 = Wall(154, 285, 50, 100, 20, 10, 300)

game = True
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if final != True:
        window.blit(background,(0, 0))
        packman.update()
        monster.update()

        packman.reset()
        monster.reset()
        final.reset()

    display.update()
    clock.tick(FPS)
    
