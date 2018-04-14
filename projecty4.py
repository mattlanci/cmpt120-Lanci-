#Matthew Lanci
#CMPT120
#Project 4


 import graphics
 import math
 from graphics import *
 @@ -26,6 +24,30 @@ def buttonMaker(valX1,valY1,valX2,valY2,color,num,win):
     buttonNum.draw(win)
     text.draw(win)
 
def insideChecker(num,win,displayString,secnum,operation):
    screenClean(win)
    displayString = displayString + num
    text = beforeText(displayString)
    text.draw(win)
    if operation ==True:
        if secnum==False:
            displayString = num
        secnum=True
    return displayString,secnum

def opDoer(win,para,sym,displayString,operation,opsign,hiddenString1):
    screenClean(win)
    if para==True:
        displayString= displayString+ sym
    else:
        hiddenString1 = displayString
        displayString = sym
        operation = True
        opsign = 1
    text = beforeText(displayString)
    text.draw(win)
    return displayString,operation,opsign,hiddenString1    

 def screenClean(win):
     scr1 = Point(60, 60)
     scr2 = Point(380, 120)
 @@ -159,6 +181,7 @@ def main():
     science =buttonMaker(380,460,440,520,'red','SM',win)
 
     displayString = ''
    hiddenString1=''
     operation = False
     opsign = 0
     secnum = False
 @@ -167,144 +190,38 @@ def main():
     while 1==1:
         clicked = win.getMouse()
         if inside(clicked, num7, 60,140,120,200):
            screenClean(win)
            displayString = displayString + '7'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '7'
                secnum=True
            displayString,secnum=insideChecker('7',win,displayString,secnum,operation)
         if inside(clicked, num8, 140,140,200,200):
            screenClean(win)
            displayString = displayString +'8'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '8'
                secnum=True
            displayString,secnum=insideChecker('8',win,displayString,secnum,operation)
         if inside(clicked, num9, 220,140,280,200):
            screenClean(win)
            displayString = displayString +'9'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '9'
                secnum=True
            displayString,secnum=insideChecker('9',win,displayString,secnum,operation)
         if inside(clicked, num4, 60,220,120,280):
            screenClean(win)
            displayString = displayString +'4'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '4'
                secnum=True
            displayString,secnum=insideChecker('4',win,displayString,secnum,operation)
         if inside(clicked, num5, 140,220,200,280):
             -            screenClean(win)
            displayString = displayString +'5'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '5'
                secnum=True
            displayString,secnum=insideChecker('5',win,displayString,secnum,operation)
         if inside(clicked, num6, 220,220,280,280):
            screenClean(win)
            displayString = displayString +'6'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '6'
                secnum=True
            displayString,secnum=insideChecker('6',win,displayString,secnum,operation)
         if inside(clicked, num3, 220,300,280,360):
            screenClean(win)
            displayString = displayString +'3'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '3'
                secnum=True
            displayString,secnum=insideChecker('3',win,displayString,secnum,operation)
         if inside(clicked, num2, 140,300,200,360):
            screenClean(win)
            displayString = displayString +'2'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '2'
                secnum=True
            displayString,secnum=insideChecker('2',win,displayString,secnum,operation)
         if inside(clicked, num1, 60,300,120,360):
            screenClean(win)
            displayString = displayString +'1'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '1'
                secnum=True
            displayString,secnum=insideChecker('1',win,displayString,secnum,operation)
         if inside(clicked, num0, 140,380,200,440):
            screenClean(win)
            displayString = displayString +'0'
            text = beforeText(displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '0'
                secnum=True
            displayString,secnum=insideChecker('0',win,displayString,secnum,operation)
         if inside(clicked, numdec, 220,380,280,440):
             screenClean(win)
             displayString = displayString +'.'
             text = beforeText(displayString)
             text.draw(win)
         if inside(clicked, add, 300,140,360,200)and operation==False:
            screenClean(win)
            if para==True:
                displayString= displayString+ '+'
            else:
                hiddenString1 = displayString
                displayString = '+'
                operation = True
                opsign = 1
            text = beforeText(displayString)
            text.draw(win)
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'+',displayString,operation,opsign,hiddenString1)
         if inside(clicked, sub, 300,220,360,280)and operation==False:
            screenClean(win)
            if para==True:
                displayString= displayString+ '-'
            else:
                hiddenString1 = displayString
                displayString = '-'
                operation = True
                opsign = 2
            text = beforeText(displayString)
            text.draw(win)
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'-',displayString,operation,opsign,hiddenString1)
         if inside(clicked, mult, 300,300,360,360)and operation==False:
            screenClean(win)
            if para==True:
                displayString= displayString+ 'x'
            else:
                hiddenString1 = displayString
                displayString = 'x'
                operation = True
                opsign = 3 text = beforeText(displayString)
            text.draw(win)
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'x',displayString,operation,opsign,hiddenString1)
         if inside(clicked, div, 300,380,360,440)and operation==False:-            screenClean(win)
            if para==True:
                displayString= displayString+ '/'
            else:
                hiddenString1 = displayString
                displayString = '/'
                operation = True
                opsign = 4
            text = beforeText(displayString)
            text.draw(win)
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'/',displayString,operation,opsign,hiddenString1)
         if inside(clicked, sign, 220,460,280,520)and operation==False:
             screenClean(win)
             displayString= str(0-float(displayString))
