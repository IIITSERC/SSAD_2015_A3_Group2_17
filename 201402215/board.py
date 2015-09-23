import pygame,sys,random
from pygame.locals import *
from main import *
class person(pygame.sprite.Sprite):
	def __init__(self,image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image)
		self.image=pygame.transform.scale(self.image,(40,30))
		self.rect=self.image.get_rect()
class player(person):
	def handleplayer(self,event):
		collisions=pygame.sprite.groupcollide(play_list,ladder_list,False,False)
		if len(collisions)>0:
			if self.rect.y>collisions.values()[0][0].rect.y+15 or self.rect.y<collisions.values()[0][0].rect.y-25:	
				if event.key==pygame.K_LEFT or event.key==pygame.K_a:
					self.rect.x-=7
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					self.rect.x+=7
		if len(collisions)==0:
				if event.key==pygame.K_LEFT or event.key==pygame.K_a:
					self.rect.x-=5
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					self.rect.x+=5
 
		if len(collisions)>0:
			if self.rect.x>=collisions.values()[0][0].rect.x+5 and self.rect.x<collisions.values()[0][0].rect.x+45:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.rect.y-=4			
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:	
					self.rect.y+=4
					if self.rect.y>=collisions.values()[0][0].rect.y-30+100:
						self.rect.y=collisions.values()[0][0].rect.y-30+100
		if event.key==pygame.K_SPACE or event.key==pygame.K_w:
			if self.falling==False:
				self.falling=True
				self.velocity=10
		if self.rect.x<0:
			self.rect.x=0
		if self.rect.x>560:
				self.rect.x=560
	def lowerco(self,line_list):
		height=1005
		collisions=pygame.sprite.groupcollide(play_list,ladder_list,False,False)
		if len(collisions)==0:
	  		for i in line_list:
				if self.rect.x>=i.rect.x and self.rect.x<=i.rect.x+500 and self.rect.y+30<=i.rect.y:
					if height>=i.rect.y:
						height=i.rect.y
			return (self.rect.x,height-30)
class donkey(person):
	def getpos(self):
		return self.rect.x,self.rect.y
class lines(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([500,15])
		self.image.fill((255,255,153))
		self.rect=self.image.get_rect()
class ladder(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('ladder3.png')

		self.image=pygame.transform.scale(self.image,(80,115))
		self.rect=self.image.get_rect()
class coins(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('coin.png')
		self.image=pygame.transform.scale(self.image,(30,30))
		self.rect=self.image.get_rect()
class fireball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('fireball.png')
		self.image=pygame.transform.scale(self.image,(30,20))
		self.rect=self.image.get_rect()
		self.rect.x=random.randint(100,570)
		donkey.rect.x=self.rect.x
		self.rect.y=80
		num=random.randint(0,1)
		if num==0:
			self.direction=0
		else:
			self.direction=1
	def lowerco(self,fire_list,fire):
		height=1005
		collisions=pygame.sprite.groupcollide(fire_list,line_list,False,False)
		if len(collisions)==0:
	  		for i in line_list:
				if fire.rect.x>=i.rect.x and fire.rect.x<=i.rect.x+500 and fire.rect.y+20<=i.rect.y:
					if height>=i.rect.y:
						height=i.rect.y
			return (fire.rect.x,height-20)
class princess(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('princess.png')
		self.image=pygame.transform.scale(self.image,(30,40))
		self.rect=self.image.get_rect()
		self.rect.x=565
		self.rect.y=60
displaysurf=pygame.display.set_mode((600,415),0,32)			
pygame.display.set_caption('donkeykong')
line_list=pygame.sprite.Group()
all_items=pygame.sprite.Group()
coins_list=pygame.sprite.Group()
white=(255,255,255)
black=(0,0,0)
play_list=pygame.sprite.Group()
play=player('playerright.png')
play.rect.x=100
play.rect.y=360
play.score=0
play.life=3
play.falling=False
play.velocity=10
play_list.add(play)
all_items.add(play)
princess_list=pygame.sprite.Group()
prince=princess()
princess_list.add(prince)
all_items.add(prince)
		
ladder_list=pygame.sprite.Group()
donkey=donkey('donkey.png')
donkey.rect.y=60
all_items.add(donkey)

line=lines()
line.rect.x=100
line.rect.y=100
line_list.add(line)
all_items.add(line)
	
line=lines()
line.rect.x=0
line.rect.y=200
line_list.add(line)
all_items.add(line)

line=lines()
line.rect.x=0
line.rect.y=400
all_items.add(line)
line_list.add(line)

line=lines()
line.rect.x=100
line.rect.y=300
line_list.add(line)
all_items.add(line)

ladd=ladder()
ladd.rect.x=300
ladd.rect.y=98
ladder_list.add(ladd)
all_items.add(ladd)

ladd=ladder()
ladd.rect.x=100
ladd.rect.y=198
ladder_list.add(ladd)
all_items.add(ladd)

ladd=ladder()
ladd.rect.x=225
ladd.rect.y=298
ladder_list.add(ladd)
all_items.add(ladd)
for i in range(10):	
	coi=coins()
	coi.rect.x=random.randint(0,600)
	coi.rect.y=random.randrange(70,400,100)
	coins_list.add(coi)
	all_items.add(coi)
pygame.key.set_repeat(10,10)
	
