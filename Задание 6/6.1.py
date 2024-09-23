from turtle import *
tracer(0)
s = 30
left()
pendown()
for i in range(5):
    fd(s)
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*s,y*s)
        dot()
done()