#!/bin/python3
import random
from turtle import *

speed(80)
penup()
goto(-140,140)
pendown()
for c in range(1,14):
  write(c)
  pendown()
  right(90)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  
  pendown()
  backward(10)
  penup()
  backward(10)
  pendown()
  backward(10)
  penup()
  backward(10)
  pendown()
  backward(10)
  penup()
  backward(10)
  pendown()
  backward(10)
  penup()
  backward(10)
 
  left(90)
  penup()
  forward(20)
a = Turtle()
a.color('red')
a.shape('turtle')
a.penup()
a.goto(-140,120)
a.pendown()
b = Turtle()
b.color('yellow')
b.shape('turtle')
b.penup()
b.goto(-140,100)
b.pendown()
c = Turtle()
c.color('green')
c.shape('turtle')
c.penup()
c.goto(-140,80)
c.pendown()
for step in range(100):  
  a.forward(random.randint(1, 4))
  b.forward(random.randint(1, 4))
  c.forward(random.randint(1, 4))
