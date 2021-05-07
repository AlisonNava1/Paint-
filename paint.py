"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
#Modificado por:
#Autor: Alison Daniela Nava Bravo
#Autor: Eduardo Aguilar Chías

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()  # levantar la tecla
    goto(start.x, start.y)
    down()  # bajar la tecla
    goto(end.x, end.y)

def square(start, end):
    """Esta función se encarga de dibujar un cuadrado"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    """Esta función se encarga de dibujar un circulo"""
    import turtle
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()        
    turtle.circle(end.x - start.x)
    end_fill()

def rectangle(start, end):
    """Esta función se encarga de dibujar un rectangulo"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x) 
        left(90) 
        forward(end.y - start.y)
        left(90)
               
    end_fill()
 
def triangle(start, end):
    """Esta función se encarga de dibujar un triángulo"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(1):
        forward(end.x - start.x) 
        left(120)  # Ángulo de los grados de las líneas del triángulo. 
        forward(end.x- start.x)

    end_fill()
          
def tap(x, y):
    """Se encarga de marcar el punto inicial para comenzar a dibujar la figura"""   
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None
        
def store(key, value):
    """Guarda valor en la clave de estado"""
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)

listen()  # Escucha la tecla 

onkey(undo, 'u')  # Deshace el último cambio

# Indica la tecla con la cual se cambia el color
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'),'Y')

# Indica la tecla con la cual generar cierta figura
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
