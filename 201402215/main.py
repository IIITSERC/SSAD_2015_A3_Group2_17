import pygame,sys,time
from pygame.locals import*
from board import *
fire_list=pygame.sprite.Group()
FPS=20
FPSCLOCK=pygame.time.Clock()
pygame.init()
displaysurf=pygame.display.set_mode((600,415),0,32)
basicfont=pygame.font.SysFont("Courier",20)
basicfont1=pygame.font.SysFont("Courier",50)

def game():

	frequency=0
	down=0
	while True:
		c=pygame.sprite.groupcollide(play_list,princess_list,False,False)
		if len(c)>0:
			text2=basicfont.render("congratulations!! you saved princess",True,(0,0,0))
			displaysurf.blit(text2,(50,200))
			pygame.display.update()
			time.sleep(2)
			play.rect.x=100
			play.rect.y=360
		if play.life==0:
			text3=basicfont1.render("Your game is over",True,(0,0,0))
			displaysurf.blit(text3,(50,200))
			pygame.display.update()
			time.sleep(2)
			pygame.quit()
			sys.exit()
		if frequency%50==0:
			fire=fireball()
			fire_list.add(fire)
			all_items.add(fire)

		for i in fire_list:
#			collide=pygame.sprite.groupcollide(ladder_list,fire_list,False,False)
#			if len(collide)>0:
#				num=random.randint(0,1)
#				if num==0:
#					i.direction=2
#				if i.rect.y+30==collide.values()[0][0].rect.y+100 and i.rect.x>=collide.values()[0][0].rect.x and i.rect.x<collide.values()[0][0].rect.x+45:		
#					i.direction=random.randint(0,1)		
			if i.direction==0:									
				i.rect.x+=5
				if i.rect.x>=600:
					i.direction=random.randint(0,1)
			if i.direction==1:
				i.rect.x-=5
				if i.rect.x<=0:
					i.direction=random.randint(0,1)
#			if i.direction==2:
#				i.rect.y+=5
			
			j=i.rect.y
			i.rect.x,i.rect.y=i.lowerco(fire_list,i)
			if j!=i.rect.y:
				num=random.randint(0,1)
				if num==0:
					i.direction=0
				else:
					i.direction=1
#	collide=pygame.sprite.groupcollide(ladder_list,fire_list,False,False)
#				if len(collide)>0:
#					i.direction=2

		frequency+=1
		(frequency)%=50
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				play.handleplayer(event)
		col=pygame.sprite.groupcollide(play_list,line_list,False,False)
		if play.velocity==-8:
			play.falling=False
		if play.falling and play.velocity!=-8:
			play.velocity-=1
			play.rect.y-=play.velocity
		collisions=pygame.sprite.groupcollide(play_list,ladder_list,False,False)
		if len(collisions)==0 and not play.falling:
			play.rect.x,play.rect.y=play.lowerco(line_list)
		coll=pygame.sprite.groupcollide(play_list,coins_list,False,True)
		if len(coll)>0:
			play.score+=5
			sound=pygame.mixer.Sound('coin.wav')
			sound.play()
		
		col=pygame.sprite.groupcollide(play_list,fire_list,False,True)
		
	
		text1=basicfont.render("you lost a life",True,(0,0,0))
		displaysurf.blit(text1,(300,300))
		displaysurf.fill(white)
		all_items.draw(displaysurf)
		text=basicfont.render("Score:" + str(play.score),True,(0,0,0))
		displaysurf.blit(text,(450,20))
		if len(col)>0:
			if play.rect.x+40>=col.values()[0][0].rect.x:
				play.life-=1
				play.score=0
				play.rect.x=20
				play.rect.y=360
				text1=basicfont1.render("you lost a life",True,(0,0,0))
				displaysurf.blit(text1,(50,200))
				pygame.display.update()
				time.sleep(2)
		if play.rect.y>370:
				play.life-=1
				play.score=0
				play.rect.x=20
				play.rect.y=360
				if play.life!=0:
					text1=basicfont1.render("you lost a life",True,(0,0,0))
					displaysurf.blit(text1,(50,200))
					pygame.display.update()
					time.sleep(2)
				
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
