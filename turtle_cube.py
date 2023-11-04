import turtle as t
import colorsys as c
t.speed('fastest')
t.bgcolor('black')
t.pencolor(c.hsv_to_rgb(0.2,0.8,1))
for j in range (99):
	for i in range(4):
		t.fd(150-j*1.5)
		t.lt(90)
for j in range (50):
	for i in range(4):
		if i==0:
			t.pencolor(c.hsv_to_rgb(0.5,0.8,1))
		elif i==1:
			t.pencolor(c.hsv_to_rgb(1,1,1))
		elif i==2:
			t.pencolor(c.hsv_to_rgb(0.5,1,1))
		else:
			t.pencolor(c.hsv_to_rgb(1,0.8,1))
		t.fd(150)
		t.lt(90)
	t.rt(135)
	t.penup()
	t.fd(1)
	t.pendown()
	t.lt(135)
for j in range (75):
	t.pencolor(c.hsv_to_rgb(0.2,1,1))
	for i in range(4):
		t.fd(150-j*2)
		t.lt(90)
t.lt(90)
t.exitonclick()
