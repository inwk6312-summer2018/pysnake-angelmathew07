
import curses
import turtle
def game_area():
		turtle1=turtle.Turtle()
		turtle1.clear()
		turtle1.pu()
		turtle1.speed(0)
		turtle1.goto(-220,220)
		turtle1.pd()
		turtle1.goto(220,220)
		turtle1.goto(220,-220)
		turtle1.goto(-220,-220)
		turtle1.goto(-220,220)
		turtle1.pu()
		turtle1.hideturtle()
		turtle1.goto(0,0)
def snake(flag):
		#turtle1=turtle.Turtle()
		if(flag==True):
			#turtle1=turtle.Turtle()
			turtle.pu()
			turtle.speed(0)
			turtle.pensize(5)
			turtle.color("grey")
			turtle.pd()
			turtle.fd(100)
			#turtle1.clear()
			turtle.goto(100,0)
			#turtle.hideturtle()
		else:
			#turtle.hideturtle()
			turtle.clear()
def up():
		turtle.setheading(90)
		snake(False)
		turtle.pensize(5)
		turtle.speed(1)
		turtle.color("grey")
		turtle.pd()
		#turtle.lt(90)
		for i in range(0,5):
			snake(False)
			turtle.fd(100)
def right():
		if(turtle.heading()==180.0):
			pass
		else:
			turtle.setheading(90)
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.rt(90)
			turtle.fd(100)
			#print("right :",turtle.position())
def left():
		if(turtle.heading()==90.0):
			print("90 270")
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.lt(90)
			turtle.fd(100)
		elif(turtle.heading()==270.0):
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.rt(90)
			turtle.fd(100)
		elif(turtle.heading()==180.0):
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.fd(100)
		else:
			pass

def down():
		if(turtle.heading()==0.0):
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.rt(90)
			turtle.fd(100)
		elif(turtle.heading()==180.0):
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.lt(90)
			turtle.fd(100)
		elif(turtle.heading()==270.0):
			snake(False)
			turtle.pensize(5)
			turtle.speed(3)
			turtle.color("grey")
			turtle.pd()
			turtle.fd(100)
		else:
			pass
game_area()
snake(True)
turtle.onkey(up, "Up")
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(down,"Down")
turtle.listen()
turtle.mainloop()

