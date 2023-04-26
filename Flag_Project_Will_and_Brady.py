#!/usr/bin/env python
# coding: utf-8

# In[1]:



import turtle
t = turtle.Turtle()
    

#every function makes the flag based on the size that you put into it while keeping the proportions of it. 
#this is done by making every drawn line based on the selected size multiplied by a proption.
def draw_stripes(size):
    t.up()
    t.forward(size)
    t.down()
    
    #makes the first 4 red stripes of the flag using a for loop
    for i in range(4):
        i = i+1
        t.color('red')
        t.begin_fill()
        t.backward(size)
        t.right(90)
    
        t.backward(size*3/55)
        t.right(90)
    
        t.backward(size)
        t.right(90)
    
        t.backward(size*3/55)
        t.up()
        t.backward(size*3/55)
        t.down()
        t.backward(size*3/55)
        t.right(90)
        t.end_fill()
    #makes the next 2 red stripes of the flag at a different length while setting up for the next stripe
    for i in range(2):
        t.begin_fill()
        t.backward(size*92/55)
        t.right(90)
    
        t.backward(size*3/55)
        t.right(90)
    
        t.backward(size*92/55)
        t.right(90)
    
        t.backward(size*3/55)
        t.up()
        t.backward(size*3/55)
        t.down()
        t.backward(size*3/55)
        t.right(90)
        t.end_fill()
    #makes the last stripe of the flag without setting up for the next stripe
    t.begin_fill()  
    
    t.backward(size*92/55)
    
    t.right(90)
    t.backward(size*3/55)
    
    t.right(90)
    t.backward(size*92/55)
    
    t.right(90)
    t.backward(size*3/55)
    
    t.right(180)
    t.end_fill()

#draws the blue background for the stars
def draw_star_background(size):
    t.color('blue')
    
    #adjusts turtle to the correct position
    t.up()
    t.backward(size*18/55)
    t.left(90)
    t.backward(size)
    
    #draws the background
    t.down()
    t.begin_fill()
    t.backward(size*37/55)
    t.right(90)
    t.backward(size*21/55)
    t.right(90)
    t.backward(size*37/55)
    t.right(90)
    t.backward(size*21/55)
    t.end_fill()
    
#outlines the flag in black
def draw_outline(size):
    
    #moves the turtle to the outside to draw an outline
    t.up()
    t.forward(size*21/55)
    t.color('black')
    t.left(90)
    
    #draws the outline of the flag
    t.down()
    t.forward(size*37/55)
    t.left(90)
    t.forward(size*39/55)
    t.left(90)
    t.forward(size*92/55)
    t.left(90)
    t.forward(size*39/55)
    t.left(90)
    t.forward(size)
    
    #resets the turtle to the previous position from the last function
    t.up()
    t.left(90)
    t.forward(size*21/55)
    t.right(180)

#draws all 50 stars of the flag
def draw_stars(size):
    t.up()
    #controls height of stars
    t.backward(size*2.2/55)
    t.left(90)
    #controls star horizontal
    t.backward(size*0.8/55)
    t.color('white')
    t.forward(size*33/55)
    #makes a grid of stars
    for i in range(5):
        t.end_fill()
        t.right(90)
        t.forward(size*4.3/55)
        t.right(90)
        t.forward(size*36.6/55)
        t.left(180)
        #makes a row of stars
        for i in range(6):
            t.end_fill()
            t.forward(size*6.1/55)
            t.begin_fill()
            #makes a star
            for i in range(5):
                t.down()
                t.forward(size*2.3/55)
                t.left(144)
                t.up()
    #fills in the last star of the for loop
    t.end_fill()
    
    #controls the height of stars
    t.backward(size*3.05/55)
    t.left(90)
    #controls the horizontal of stars
    t.forward(size*19.35/55)
    t.right(90)
    #makes the 2nd grid of stars
    for i in range(4):
        t.end_fill()
        t.right(90)
        t.forward(size*4.3/55)
        t.right(90)
        t.forward(size*30.5/55)
        t.left(180)
        #makes a row of stars
        for i in range(5):
            t.end_fill()
            t.forward(size*6.1/55)
            t.begin_fill()
            #makes a star
            for i in range(5):
                t.down()
                t.forward(size*2.3/55)
                t.left(144)
                t.up()
    #fills in the final star            
    t.end_fill()

#calls the 4 functions
def main():
    draw_stripes(400)
    draw_star_background(400)
    draw_outline(400)
    draw_stars(400)
    t.getscreen()
    turtle.done()
            





if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




