from graphics import * #Importing external libraies / random function
import random

# Read in and print out the data in the data file
datafile = open("data.txt",'r') #Importing external data file
bigData = datafile.readlines() 

window = GraphWin("Visualisation", 700,700) #Setting window size

for line in bigData: 
	print(line) #Initialization to print bigData as shapes
	ball = Circle(Point(random.randint(1, 700),random.randint(1, 700)), float(line)) #Setting where the shapes will be drawn in the visulization
	ball.setFill(color_rgb(random.randint(60,128),128,128)) #Setting colours
	ball.draw(window) #Drawing



# Waits until the mouse is clicked before closing the window
window.getMouse()