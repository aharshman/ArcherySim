# -*- coding: utf-8 -*-
"""
Alexander Harshman
"""

from graphics import *
from math import *

def main():
    
# Setting Variables
    NPlayers = 2
    TotalPoints = 0
    x = 210
    Winner = 0
    PlayerNumber = 1
    
# Making the window
    win = GraphWin("Archery Game",400,400)
    win.setBackground('lightblue')
        
# Making a loop
    while True:
        
# Making the Intro
        Introt = Text(Point(200, 200), 'Archery Clicker')
        Introt.setFace('courier')
        Introt.setSize(18)
        Introt.setStyle('bold italic')
        Introt.draw(win)
        
# Making Alpha Text
        Alpha = Text(Point(371, 395), 'Alpha: -1.0.1')
        Alpha.setSize(7)
        Alpha.draw(win)
        time.sleep(2)
        
# Undrawing Intro
        Introt.undraw()
        
# How many players will be playing
        Introt2 = Text(Point(200, 180), 'How many people are playing?')
        Introt2.setFace('courier')
        Introt2.setSize(18)
        Introt2.setStyle('bold italic')
        Introt2.draw(win)
        Pentry = Entry(Point(200, 220), 2)
        Pentry.setFill('light pink')
        Pentry.draw(win)
        Pentry.setText('0')
        win.getMouse()
        NPlayers = int(Pentry.getText())
        Introt2.undraw()
        Pentry.undraw()
        
# Making the Loop
        # Making Arrow shooting and display loops
        for n in range (NPlayers):

    # Begin shooting Arrows
            Introt3 = Text(Point(200, 200), 'Click to Shoot Arrows')
            Introt3.setFace('courier')
            Introt3.setSize(20)
            Introt3.setStyle('bold italic')
            Introt3.draw(win)
            time.sleep(2)
            Introt3.undraw()
    
    # Making the Bullseye
            
        # Making the Circles
            center  = Point(200,200)
            rad     = 25
            circ1   = Circle(center, rad)
            circ2   = Circle(center, 2*rad)
            circ3   = Circle(center, 3*rad)
            circ4   = Circle(center, 4*rad)
            circ5   = Circle(center, 5*rad)
        
        # Coloring the Circles
            circ1.setFill('pink')
            circ2.setFill('blue')
            circ3.setFill('red')
            circ4.setFill('orange')
            circ5.setFill('purple')
        
        # Drawing the Circles
            circ5.draw(win)
            circ4.draw(win)
            circ3.draw(win)
            circ2.draw(win)
            circ1.draw(win)
            
        # Making Scoring Area
            PlayerOne = Text(Point(100,25), 'Player ' + str(PlayerNumber)+ ' Score: ')
            PlayerOne.setStyle('bold italic')
            PlayerOne.setFace('courier')
            PlayerOne.setSize(15)
            PlayerOne.draw(win)
            
        # Showing how many arrows the shooter has left
            Arrow1 = Circle(Point(185, 340), 5)
            Arrow1.setFill('black')
            Arrow2 = Circle(Point(200, 340), 5)
            Arrow2.setFill('black')
            Arrow3 = Circle(Point(215, 340), 5)
            Arrow3.setFill('black')
           
            Arrow1.draw(win)
            Arrow2.draw(win)
            Arrow3.draw(win)
            
        # Resetting the points
            points = 0
            x = 210
            TotalPoints = 0
            
    # Shot One
        
        # Making and drawing point 1
            shot1 = win.getMouse()
            shot1.draw(win)
            shotX1 = shot1.getX()
            shotY1 = shot1.getY()
                
        # Finding the distance between the center and the shot
            r = sqrt(((shotX1 - 200)**2) + (shotY1 - 200)**2)
                
        # Calculating Points Based on distance from the center
            if r <= 25:
                points = 50
            elif 25 < r <= 50:
                points = 40
            elif 50 < r <= 75:
                points = 30
            elif 75 < r <= 100:
                points = 20
            elif 100 < r <= 125:
                points = 10
            else:
                points = 0
                    
        # Adding up the points and displaying each arrow's score
            TotalPoints = points + TotalPoints
            pointsd1 = Text(Point(x, 25), str(points) + ', ')
            pointsd1.setStyle('bold italic')
            pointsd1.setFace('courier')
            pointsd1.setSize(15)
            pointsd1.draw(win)
            x = x + 35
            
        # Losing One arrow
            Arrow1.setFill('light blue')
            
    # Second Shot
        
        # Making and drawing points
            shot2 = win.getMouse()
            shot2.draw(win)
            shot2X = shot2.getX()
            shot2Y = shot2.getY()
                
        # Finding the distance between the center and the shot
            D = sqrt(((shot2X - 200)**2)+ (shot2Y - 200)**2)
                
        # Calculating Points Based on distance from the center
            if D <= 25:
                points = 50
            elif 25 < D <= 50:
                points = 40
            elif 50 < D <= 75:
                points = 30
            elif 75 < D <= 100:
                points = 20
            elif 100 < D <= 125:
                points = 10
            else:
                points = 0
                    
        # Adding up the points and displaying each arrow's score
            TotalPoints = points + TotalPoints
            pointsd2 = Text(Point(x, 25), str(points) + ',')
            pointsd2.setStyle('bold italic')
            pointsd2.setFace('courier')
            pointsd2.setSize(15)
            pointsd2.draw(win)
            x = x + 35
            
        # Losing One arrow
            Arrow2.setFill('light blue')
            
    # Shot Three
        
        # Making and drawing points
            shot3 = win.getMouse()
            shot3.draw(win)
            shot3X = shot3.getX()
            shot3Y = shot3.getY()
                
        # Finding the distance between the center and the shot
            r = sqrt(((shot3X - 200)**2)+ (shot3Y - 200)**2)
                
        # Calculating Points Based on distance from the center
            if r <= 25:
                points = 50
            elif 25 < r <= 50:
                points = 40
            elif 50 < r <= 75:
                points = 30
            elif 75 < r <= 100:
                points = 20
            elif 100 < r <= 125:
                points = 10
            else:
                points = 0
                    
        # Adding up the points and displaying each arrow's score
            TotalPoints = points + TotalPoints
            pointsd3 = Text(Point(x, 25), str(points))
            pointsd3.setStyle('bold italic')
            pointsd3.setFace('courier')
            pointsd3.setSize(15)
            pointsd3.draw(win)
            
        # Losing One arrow
            Arrow3.setFill('light blue')
            
        # Pause so user can see individual shot scores
            time.sleep(2)
                
        # Displaying the total score for that round
            
            # Clearing the screen
            circ5.undraw()
            circ4.undraw()
            circ3.undraw()
            circ2.undraw()
            circ1.undraw()
            pointsd1.undraw()
            pointsd2.undraw()
            pointsd3.undraw()
            PlayerOne.undraw()
            shot1.undraw()
            shot2.undraw()
            shot3.undraw()
            Arrow1.undraw()
            Arrow2.undraw()
            Arrow3.undraw()
            
            # Total score Display
            FScore = Text(Point(200, 180), 'The Final Score for Player ' + str(PlayerNumber) + ' is:')
            FScore2 = Text(Point(200, 220), str(TotalPoints))
            FScore.setStyle('bold italic')
            FScore.setFace('courier')
            FScore.setSize(13)
            FScore2.setStyle('bold italic')
            FScore2.setFace('courier')
            FScore2.setSize(32)
            FScore.draw(win)
            FScore2.draw(win)
            time.sleep(3)
            FScore.undraw()
            FScore2.undraw()
            PlayerNumber = PlayerNumber + 1
            
            
        # Reassign Variables
            sub = TotalPoints
            
        # Determining the highest score
            if TotalPoints > Winner:
                Winner = sub
                PWinner = PlayerNumber
        PWinner = PWinner - 1
                
    # Winner Screen
        Con = Image(Point(200, 200), 'Winner.gif')
        W = Text(Point(200, 180), 'Player ' + str(PWinner) + ' wins with a score of:')
        Winn = Text(Point(200, 220), str(Winner))
        W.setStyle('bold italic')
        W.setFace('courier')
        W.setSize(11)
        Winn.setStyle('bold italic')
        Winn.setFace('courier')
        Winn.setSize(32)
        Con.draw(win)
        W.draw(win)
        Winn.draw(win)
        
    # Pause
        time.sleep(5)
            
    # Break
        break
    
# Close Window
    win.close()
    
main()