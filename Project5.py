#Matthew Lanci
#Project 5

from graphics import *
from calc_functions import *
from button import Button
win = GraphWin('Calculator', 500, 500)
win.setCoords(0, 0, 8, 6)

buttons = dict()
buttons['M+'] = Rectangle(Point(0, 0), Point(1, 1))
buttons['0'] = Rectangle(Point(1, 0), Point(3, 1))
buttons['.'] = Rectangle(Point(3, 0), Point(4, 1))
buttons['='] = Rectangle(Point(4, 0), Point(5, 1))
buttons['cos'] = Rectangle(Point(5, 0), Point(6, 1))
buttons['tan'] = Rectangle(Point(6, 0), Point(7, 1))
buttons['arccsne'] = Rectangle(Point(7, 0), Point(8, 1))


buttons['M-'] = Rectangle(Point(0, 1), Point(1, 2))
buttons['1'] = Rectangle(Point(1, 1), Point(2, 2))
buttons['2'] = Rectangle(Point(2, 1), Point(3, 2))
buttons['3'] = Rectangle(Point(3, 1), Point(4, 2))
buttons['+'] = Rectangle(Point(4, 1), Point(5, 2))
buttons['sin'] = Rectangle(Point(5, 1), Point(6, 2))
buttons['x^y'] = Rectangle(Point(6, 1), Point(7, 2))
buttons['arctne'] = Rectangle(Point(7, 1), Point(8, 2))
        
buttons['MR'] = Rectangle(Point(0, 2), Point(1, 3))
buttons['4'] = Rectangle(Point(1, 2), Point(2, 3))
buttons['5'] = Rectangle(Point(2, 2), Point(3, 3))
buttons['6'] = Rectangle(Point(3, 2), Point(4, 3))
buttons['-'] = Rectangle(Point(4, 2), Point(5, 3))
buttons['/x'] = Rectangle(Point(5, 2), Point(6, 3))
buttons['10^x'] = Rectangle(Point(6, 2), Point(7, 3))
buttons['ln'] = Rectangle(Point(7, 2), Point(8, 3))

buttons['MC'] = Rectangle(Point(0, 3), Point(1, 4))
buttons['7'] = Rectangle(Point(1, 3), Point(2, 4))
buttons['8'] = Rectangle(Point(2, 3), Point(3, 4))
buttons['9'] = Rectangle(Point(3, 3), Point(4, 4))
buttons['*'] = Rectangle(Point(4, 3), Point(5, 4))
buttons['^2'] = Rectangle(Point(5, 3), Point(6, 4))
buttons['log'] = Rectangle(Point(6, 3), Point(7, 4))
buttons[')'] = Rectangle (Point(7, 3), Point(8, 4))

buttons['MS'] = Rectangle(Point(0, 4), Point(1, 5))
buttons['AC'] = Rectangle(Point(1, 4), Point(2, 5))
buttons['+/-'] = Rectangle(Point(2, 4), Point(3, 5))
buttons['%'] = Rectangle(Point(3, 4), Point(4, 5))
buttons['/'] = Rectangle(Point(4, 4), Point(5, 5))
buttons['√'] = Rectangle(Point(5, 4), Point(6, 5))
buttons['arcsne'] = Rectangle(Point(6, 4), Point(7, 5))
buttons['('] = Rectangle(Point(7, 4), Point(8, 5))


# Add buttons to window with text
for symbol, btn in buttons.items():
    btn.setOutline('orange')
    btn.setFill('grey')
    win.addItem(btn)
    text = Text(btn.getCenter(), symbol)
    text.setSize(15)
    win.addItem(text)

display = Text(Point(4.0, 5.8),'')
display2 = Text(Point(4.0, 5.5), '')
display2.setSize(34)
display.setSize(15)
win.addItem(display)
win.addItem(display2)

win.redraw()



##Returns the symbl that was clicked
def clicked(click):
    cx, cy = click.getX(), click.getY()
    for symbol, btn in buttons.items():
        if btn.getP1().getX() < cx < btn.getP2().getX() and \
           btn.getP1().getY() < cy < btn.getP2().getY():
           return symbol
    return ''

from calc_functions import *
##dirty = False
mem = '0'
answer = ''
while win.isOpen():
    click = win.getMouse()
    symbol = clicked(click)
    if symbol == 'AC':
        display2.setText('')
        display.setText('')

    elif symbol == 'M+' or symbol == 'M-' or symbol == 'MR' or symbol == 'MC'\
    or symbol == 'MS':
        if symbol == 'M+':
            mem = memplus(display.getText(), mem)
        elif symbol == 'M-':
            mem = memsubtract(display.getText(), mem)
        elif symbol == 'MR':
            display.setText(mem)
        elif symbol == 'MC':
            mem = '0'
        elif symbol == 'MS':
            mem = display.getText()

    elif symbol == '=':
        display2.setText(str(determine(display.getText())))
               
    else:
        if symbol == '^2':
            symbol = '**'
        display.setText(display.getText() + symbol)
        try:
            result = str(determine(display.getText()))
            display2.setText(result)
        except ValueError: pass
