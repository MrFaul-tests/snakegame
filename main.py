import time 
import random 



class Snake:

	def __init__(self, sizeX, sizeY):
		self.first = 0
		self.score = 0
		self.direction = "down"
		if sizeX % 10 == 0 and sizeY % 10 == 0:
			#условные координаты змеи 
			self.cords_of_snake = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
			#края карты 
			self.max_size_x = sizeX / 10
			self.max_size_y = sizeY / 10
			self.apple = False
		else:
			print("Поле должно быть кратно 10")


	def move_right(self):
		if self.direction == "left":
			self.move_left()
		else:	
			self.direction = "right"
			change1 = self.cords_of_snake[-1]
			self.cords_of_snake[-1][0] = self.cords_of_snake[-1][0] + 1
			for i in range(len(self.cords_of_snake) - 1):
				change2 = self.cords_of_snake[i]
				self.cords_of_snake[i] = [change1[0], change1[1]]
				change1 = change2


	def move_left(self):
		if self.direction == "right":
			self.move_right()
		else:	
			self.direction = "left"
			change1 = self.cords_of_snake[-1]
			self.cords_of_snake[-1][0] = self.cords_of_snake[-1][0] - 1
			for i in range(len(self.cords_of_snake) - 1):
				change2 = self.cords_of_snake[i]
				self.cords_of_snake[i] = [change1[0], change1[1]]
				change1 = change2


	def move_up(self):
		if self.direction == "down":
			self.move_down()
		else:	
			self.direction = "up"
			change1 = self.cords_of_snake[-1]
			self.cords_of_snake[-1][1] = self.cords_of_snake[-1][1] - 1
			for i in range(len(self.cords_of_snake) - 1):
				change2 = self.cords_of_snake[i]
				self.cords_of_snake[i] = [change1[0], change1[1]]
				change1 = change2


	def move_down(self):
		if self.direction == "up":
			self.move_up()
		else:	
			self.direction = "down"
			change1 = self.cords_of_snake[-1]
			self.cords_of_snake[-1][1] = self.cords_of_snake[-1][1] + 1
			for i in range(len(self.cords_of_snake) - 1):
				change2 = self.cords_of_snake[i]
				self.cords_of_snake[i] = [change1[0], change1[1]]
				change1 = change2

	
	def add_block(self):
		if self.direction == "down":
			self.cords_of_snake.append([self.cords_of_snake[-1][0], self.cords_of_snake[-1][1] + 1])
		elif self.direction == "up":
			self.cords_of_snake.append([self.cords_of_snake[-1][0], self.cords_of_snake[-1][1] -1])
		elif self.direction == "right":
			self.cords_of_snake.append([self.cords_of_snake[-1][0] + 1, self.cords_of_snake[-1][1]])
		elif self.direction == "left":
			self.cords_of_snake.append([self.cords_of_snake[-1][0] - 1, self.cords_of_snake[-1][1]])


	def create_apple(self):
		if self.apple == True:
			pass
		else:
			self.apple_rectx = random.randint(0, self.max_size_x) * 10
			self.apple_recty = random.randint(0, self.max_size_y) * 10
			self.apple = True
			self.add_block()
			self.score = self.score + 1
			print("Score:" + str(self.score))

	
	def check_apple(self):
		if self.apple_rectx == self.cords_of_snake[-1][0] * 10 and self.apple_recty == self.cords_of_snake[-1][1] * 10:
			self.apple = False
		else:
			pass

	def check_border(self):
		if self.max_size_x < self.cords_of_snake[-1][0]:
			self.cords_of_snake[-1][0] = 0

		elif self.cords_of_snake[-1][0] < 0:
			self.cords_of_snake[-1][0] = self.max_size_x
			
		elif self.max_size_y < self.cords_of_snake[-1][1]:
			self.cords_of_snake[-1][1] = 0
			
		elif self.cords_of_snake[-1][1] < 0:
			self.cords_of_snake[-1][1] = self.max_size_y



	def draw(self):
		for i in range(len(self.cords_of_snake)):
			rectx = self.cords_of_snake[i][0] * 10
			recty = self.cords_of_snake[i][1] * 10
			rect(rectx, recty, 10, 10)
			fill(255)
		rect(self.apple_rectx, self.apple_recty, 10, 10)
		fill(255)



def setup():
    size(800, 800)
    snake = Snake(800,800)
    global snake


def draw():
	time.sleep(0.02)
	rect(0, 0, 800, 800)
	fill(0)
	snake.create_apple()
	snake.check_apple()
	snake.check_border()
	if key == "w":
		snake.move_up()
		rect(0, 0, 800, 800)
		fill(0)
	elif key == "s":
		snake.move_down()
		rect(0, 0, 800, 800)
		fill(0)
	elif key == "a":
		snake.move_left()
		rect(0, 0, 800, 800)
		fill(0)
	elif key == "d":
		snake.move_right()
		rect(0, 0, 800, 800)
		fill(0)
	else:
		snake.move_down()
		rect(0, 0, 800, 800)
		fill(0)
	snake.draw()
