
##############################################################################
#                                                                            #
#                              Snake Game                                    #
#                                                                            #
#                                                                            #
# CREATED BY    :    Nithin.P                                                #
#                    nithup123@gmail.com                                     #
#                    http://facebook.com/nithin.nithinp                      #
#                                                                            #
# Description   :    This is Snake Game  coded by me                         #
#                    in python using pygame module.                          #
#                                                                            #
# License       :    This Source Code is free to use                         #
#                    for educational purpose only.                           #
#                                                                            #
# Instructions  :    Use 'UP' key to change direction of snake to 'UP'       #
#                    Use 'DOWN' key to change direction of snake to 'DOWN'   #
#                    Use 'LEFT' key to change direction of snake to 'LEFT'   #
#                    Use 'RIGHT' key to change direction of snake to 'RIGHT' #
#                                                                            #
##############################################################################



import pygame
import sys
import random


# Initial Conditions.

white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
gray=(128,128,128)
size=[720,630]
cube_size=30
snake=[{'i_cord' : 5,'j_cord' : 7},{'i_cord' : 5,'j_cord' : 8},{'i_cord' : 5,'j_cord' : 9},{'i_cord' : 5,'j_cord' : 10}]
new_food=True
food=None
time1=pygame.time.get_ticks()
direction='right'
game_over=False
score=0
paused_game=False
time_limit=300       # Increase this time limit to decrease speed of snake






# Function to reset the game.

def reset_game() :
	global snake
	global new_food
	global food
	global time1
	global direction
	global game_over
	global score

	snake=[{'i_cord' : 5,'j_cord' : 7},{'i_cord' : 5,'j_cord' : 8},{'i_cord' : 5,'j_cord' : 9},{'i_cord' : 5,'j_cord' : 10}]
	new_food=True
	food=None
	time1=pygame.time.get_ticks()
	direction='right'
	game_over=False
	score=0




# Function to wait for any key press.

def wait_for_any_key() :
	while True :
		for event in pygame.event.get() :
			if event.type==pygame.QUIT :
				sys.exit()
				pygame.quit()
			if event.type == pygame.KEYDOWN :
				return True





# Function to print press any key.

def print_press_any_key() :
	global paused_game
	font=pygame.font.Font(None,30)
	if paused_game :
		text = font.render("Press Escape key to continue", True, gray)
	else :
		text = font.render("Press any key to continue", True, gray)
	rect = text.get_rect()
	rect.centerx=size[0]-150
	rect.centery=size[1]-50
	screen.blit(text, rect)









# Function to print 'Paused'.

def print_paused_game() :
	font=pygame.font.Font(None,230)
	overText = font.render('Paused', True, white)
	overRect = overText.get_rect()
	overRect.centerx=(size[0]/2)
	overRect.centery=(size[1]/2)
	screen.blit(overText, overRect)
	print_press_any_key()








# Function to draw initial screen.

def draw_initial_screen() :
	play()
	draw_screen()
	font=pygame.font.Font(None,220)
	gameText = font.render("Nithin's", True, white)
	overText = font.render('Snake', True, white)
	over1Text = font.render('Game', True, white)
	gameRect = gameText.get_rect()
	overRect = overText.get_rect()
	over1Rect = over1Text.get_rect()
	gameRect.centerx=(size[0]/2)
	gameRect.centery=(size[1]/2)-150
	overRect.centerx=(size[0]/2)
	overRect.centery=(size[1]/2)
	over1Rect.centerx=(size[0]/2)
	over1Rect.centery=(size[1]/2+150)
	screen.blit(gameText, gameRect)
	screen.blit(overText, overRect)
	screen.blit(over1Text, over1Rect)
	print_press_any_key()
	pygame.display.update()








# Function print Game Over.

def print_game_over() :
	font=pygame.font.Font(None,270)
	font1=pygame.font.Font(None,50)
	gameText = font.render('Game', True, white)
	overText = font.render('Over', True, white)
	sc="Your Score : "+str(score)
	scoreText = font1.render(sc, True, white)
	gameRect = gameText.get_rect()
	overRect = overText.get_rect()
	scoreRect = scoreText.get_rect()
	gameRect.centerx=(size[0]/2)
	gameRect.centery=(size[1]/2)-120
	overRect.centerx=(size[0]/2)
	overRect.centery=(size[1]/2)+30
	scoreRect.centerx=(size[0]/2)
	scoreRect.centery=(size[1]/2)+150
	screen.blit(gameText, gameRect)
	screen.blit(overText, overRect)
	screen.blit(scoreText, scoreRect)






# Function create new food location.

def create_new_food_location() :
	tmp=[]
	for i in range(19) :
		for j in range(24) :
			t={'i_cord' : i,'j_cord' : j}
			if t not in snake :
				tmp.append(t)
	loc=(int(random.random()*100000000))%len(tmp)
	food=tmp[loc]
	return food







# Function to draw game screen.

def draw_screen() :
	screen.fill(black)
	i=0
	while i<(size[0]) :
		pygame.draw.line(screen,gray,(i,60),(i,size[1]))
		i+=cube_size
	i=60
	while i<(size[1]) :
		pygame.draw.line(screen,gray,(0,i),(size[0],i))
		i+=cube_size
	font=pygame.font.Font(None,30)
	score1='Score : '+str(score)
	scoreText=font.render(score1,True,white)
	scoreRect=scoreText.get_rect()
	scoreRect.centerx=int(size[0]/2)
	scoreRect.centery=30
	screen.blit(scoreText,scoreRect)
	for part in snake :
		left=(part['j_cord']*cube_size)+1
		up=(part['i_cord']*cube_size)+60+1
		pygame.draw.rect(screen,red,(left,up,(cube_size-1),(cube_size-1)))
	left=(food['j_cord']*cube_size)+1
	up=(food['i_cord']*cube_size)+60+1
	pygame.draw.rect(screen,green,(left,up,(cube_size-1),(cube_size-1)))





# Main play function.

def play() :
	global game_over
	global food
	global snake
	global new_food
	global time1
	global score
	if new_food :
		food=create_new_food_location()
		new_food=False
		#print food
	if pygame.time.get_ticks() > (time1+time_limit) :
		new_snake_head={'i_cord' : 0,'j_cord' : 0}                       # Create new snake head.
		if direction=='right' :
			new_snake_head['i_cord']=snake[(len(snake)-1)]['i_cord']
			new_snake_head['j_cord']=snake[(len(snake)-1)]['j_cord']+1
		if direction=='left' :
			new_snake_head['i_cord']=snake[(len(snake)-1)]['i_cord']
			new_snake_head['j_cord']=snake[(len(snake)-1)]['j_cord']-1
		if direction=='up' :
			new_snake_head['i_cord']=snake[(len(snake)-1)]['i_cord']-1
			new_snake_head['j_cord']=snake[(len(snake)-1)]['j_cord']
		if direction=='down' :
			new_snake_head['i_cord']=snake[(len(snake)-1)]['i_cord']+1
			new_snake_head['j_cord']=snake[(len(snake)-1)]['j_cord']
		if new_snake_head==food :                                          # Snake catches food.
			snake.append(new_snake_head)
			new_food=True
			score+=1
		else :
			if new_snake_head['i_cord']<0 or new_snake_head['i_cord']>=19 or new_snake_head['j_cord']<0 or new_snake_head['j_cord']>=24 :  # new_new_snake_head exceeds screem size. 
				game_over=True
			if new_snake_head in snake :             # new_new_snake_head strikes with snake body.
				game_over=True
			if game_over==False :
				snake.append(new_snake_head)
			snake.remove(snake[0])
		time1=pygame.time.get_ticks()







# Initial screen.

pygame.init()
screen=pygame.display.set_mode(size,0,32)
pygame.display.set_caption("Nithin's Snake Game")
draw_initial_screen()
while True :
	if wait_for_any_key() :
		break


# Main game loop

while True :
	for event in pygame.event.get() :
		if event.type==pygame.QUIT :
			if paused_game :
				sys.exit()
				pygame.quit()
			game_over=True
			print_game_over()
			pygame.display.update()
			time3=pygame.time.get_ticks()
			while pygame.time.get_ticks() < (time3+1000) :
				pygame.time.get_ticks()
			sys.exit()
			pygame.quit()
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_ESCAPE :
				if paused_game==False :
					paused_game=True
					print_paused_game()
					pygame.display.update()
				else :
					paused_game=False
			if event.key == pygame.K_LEFT :                       # Change direction of snake to Left.
				if direction!='right' :
					direction='left'
			if event.key == pygame.K_RIGHT :                      # Change direction of snake to RIGHT.
				if direction!='left' :
					direction='right'
			if event.key == pygame.K_DOWN :                       # Change direction of snake to DOWN.
				if direction!='up' :
					direction='down'
			if event.key == pygame.K_UP :                         # Change direction of snake to UP.
				if direction!='down' :
					direction='up'


	if game_over==True :
		print_game_over()
		pygame.display.update()
		if wait_for_any_key() :
			reset_game()
	elif paused_game==False :
		play()
		draw_screen()
		pygame.display.update()
