#written by Amit

import curses
from curses import wrapper 
import time
import random as r
def gameover(screen,snake):
	screen.addstr(0,0,f'''
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█ █
█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄ ▄\n\n\n
▀█▀ █▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄░█
░█░ █▀▄ ░█░   █▀█ █▄█ █▀█ █ █░▀█\n\n\n
SCORE:{len(snake)-5}''',curses.color_pair(5))
	screen.refresh()
	screen.nodelay(0)
	time.sleep(5)
	run = False

def main(screen):
	curses.resize_term(30,60)
	apple = list(map(r.randrange,screen.getmaxyx()))
	apple[1] = apple[1] // 2 * 2
	change = (0,2)
	run = True
	snake = [(10,18),(10,16),(10,14),(10,12),(10,10)]
	eaten = True
	while run:
		curses.curs_set(0)
		screen.nodelay(1)
		curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_RED)
		curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_CYAN)
		curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_BLUE)
		curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)
		curses.init_pair(5,curses.COLOR_GREEN,curses.COLOR_BLACK)
		try:
			char = screen.getkey()
		except:
			char = 'none'
		screen.clear()
		if char == 'q':
			break

		change = (1,0) if char == 's' else (0,-2) if char == 'a' else (-1,0) if char == 'w' else (0,2) if char == 'd' else change
		snake = [(snake[0][0]+change[0],snake[0][1]+change[1])]+snake
		try:
			screen.addstr(*snake[0],'  ',curses.color_pair(4))
		except:
			gameover(screen,snake)
			break
		for i in range(1,len(snake)):
			screen.addstr(*snake[i],'  ',curses.color_pair(2) if i % 2 == 0 else curses.color_pair(3))
		if any(snake[i]==snake[j] and i!=j for i in range(len(snake)) for j in range(len(snake))):
			gameover(screen,snake)
			break
		#apple
		eaten = list(snake[0]) == apple 
		if not eaten:
			snake.pop()
		else:
			apple = list(map(r.randrange,screen.getmaxyx()))
			apple[1] = apple[1] // 2 * 2
			eaten = False
		screen.addstr(*apple,'  ',curses.color_pair(1))
		screen.refresh()
		time.sleep(0.1)
wrapper(main)
