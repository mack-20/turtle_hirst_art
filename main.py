import turtle
from random import choices
#Needed this code to extract the colors from the jpg file
#import colorgram
# color_list = colorgram.extract('hirst_art.jpg',40)
# new_color_list = []

# for color in color_list:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color_list.append((r,g,b))

# print(new_color_list)

turtle.colormode(255)

hex_bgcolor = "#{:02X}{:02X}{:02X}".format(218, 226, 222)

screen = turtle.Screen()
screen.title("Hirst Art")
screen.bgcolor(hex_bgcolor)
screen.setup(width=1200,height=800)

message = "Hirst Art by Turtle!"
benny = turtle.Turtle("turtle")
benny.penup()
benny.hideturtle()
benny.setposition(-100,-200)
benny.speed(1)


colors = [(253, 251, 247), (253, 249, 252), (232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42), (216, 90, 52), (173, 178, 231), (235, 170, 164), (8, 244, 224), (248, 9, 44)]

dots_printed = 0
for _ in range(len(colors)):
  if dots_printed % 5 == 0:
    turtle_position = list(benny.position())
    #Increase y-coordinate by 40 units
    benny.setposition(0,turtle_position[1]+40)
    
  benny.dot(20,choice(colors))
  dots_printed += 1
  benny.forward(40)


#Print message
turtle_position = list(benny.position())
benny.setposition(80,turtle_position[1]+60)
benny.write(arg=message,move=True,align='center',font=('Arial',10,'normal'))
benny.setposition(90,turtle_position[1]+40)
benny.showturtle()


screen.exitonclick()