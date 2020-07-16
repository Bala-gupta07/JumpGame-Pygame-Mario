import pygame,random
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load('bgsong.mp3')
mixer.music.play(-1)
bulletSound=mixer.Sound('bullet.wav')
win = pygame.display.set_mode((1000,550))
pygame.display.set_caption("Jump Game")
image = pygame.image.load('Penguin_Mario.PNG.png')
image = pygame.transform.scale(image,(100,100))
imageB = pygame.image.load('bullet.png')
imageB = pygame.transform.scale(imageB,(40,40))
enemyImage = pygame.image.load('enemy.png')
enemyImage = pygame.transform.scale(enemyImage,(150,90))
bgColor = (5,100,150)

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def checkBoundary(self,x,y):
        if (x < 0):
            self.x = 0
        if (x > 900):
            self.x = 900
        if (y < 0):
            self.y = 0
        if (y > 450):
            self.y = 450

class Bullet(object):
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
    def hit(self):
        print('hit')

class projectile(object):
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius

    def draw(self,win):
        win.blit(imageB, (self.x, self.y))

if __name__=='__main__':
    man = Player(100,100,50,50)
    bullet = Bullet(1000,200,10)
    score = 0
    lives = 3
    fire = []
    run = True
    speed = 5
    font = pygame.font.SysFont('comicsansms',20,True,True)
    while run:
        hit = False
        pygame.time.delay(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for f in fire:
            if f.x > bullet.x and f.x < bullet.x+40 and f.y > bullet.y and f.y < bullet.y+40 :
                bullet.hit()
                score += 1
                if score % 2 == 0:
                    speed += 2
                if(score >= 10):
                    bgColor = (0,0,0)
                hit = True
                fire.pop(fire.index(f))
                bullet.x=9

            if f.x<1000 and f.x>0:
                f.x+=10
            else:
                fire.pop(fire.index(f))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            man.y-=25
        if keys[pygame.K_DOWN]:
            man.y+=5
        if keys[pygame.K_RIGHT]:
            man.x+=10
        if keys[pygame.K_LEFT]:
            man.x-=10
        if keys[pygame.K_SPACE]:
            pygame.time.delay(100)
            bulletSound.play()
            fire.append(projectile(man.x+50,man.y+50,10))

        man.checkBoundary(man.x,man.y)
        win.fill(bgColor)
        win.blit(image,(man.x,man.y))
        bullet.x -= bullet.speed
        for i in fire:
            i.draw(win)
        if(bullet.x <= 10):
            if(hit==False):
                lives -= 1
            if(lives==0):
                break
            bullet.x = 1000
            bullet.y = random.randint(50,450)
            bullet.speed = speed
        win.blit(enemyImage, (bullet.x, bullet.y))
        text = font.render("Score : "+str(score),1,(255,255,255))
        win.blit(text,(850,10))
        text = font.render("lives :- "+str(lives)+"/ 3",1,(255,255,255))
        win.blit(text,(850,30))
        pygame.display.update()

    pygame.quit()