import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	tur.setheading(0)
        tur.pd()
        tur.circle(50)
        tur.pu()
        tur.left(90)
        tur.fd(120)
        tur.right(90)
        tur.fd(60)
    elif letter == "P":
	    pass		
    elif letter == "Q":
	tur.setheading(0)
        tur.pd()
        tur.circle(50)
        tur.pu()
        tur.left(45)
        tur.fd(30)
        tur.pd()
        tur.right(75)
        tur.fd(40)
        tur.pu()
        tur.left(120)
        tur.fd(140)
        tur.right(90)
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(40)
        tur.pu()
    elif letter == "U":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(50)
        tur.right(180)
        tur.fd(50)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
    elif letter == "V":
	    pass
    elif letter == "W":
	tur.setheading(0)
        tur.pd()
        tur.right(70)
        tur.fd(40)
        tur.left(150)
        tur.fd(20)
        tur.right(150)
        tur.fd(20)
        tur.left(150)
        tur.fd(40)
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
