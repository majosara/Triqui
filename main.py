import graficas
from turtle import*

speed(11)

#El número de turnos durante todo el juego
turno = 9 
jugador1 = True
jugador2 = False
puntaje1 = 0
puntaje2 = 0

#Variables de graficas
fontsize= 100
scala=1.2
cuadrante=fontsize*1.2

#casillas jugador 1
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

#casillas jugador 2
a1 = 0
b1 = 0
c1 = 0
d1 = 0
e1 = 0
f1 = 0
g1 = 0
h1 = 0
i1 = 0

def getPos(x,y):
    """ La funcion recibe las coordenadas x,y
    Comprueba el turno del jugador y llama a la función dibujarX o dibujarO dependiendo del jugador de turno
    En caso de haber jugado todos los turnos, se reinicia el juego.
    """
    global turno
    if turno % 2 == 1 and jugador1 == True and jugador2 == False:
        dibujarX(x,y)

    if turno % 2 == 0 and jugador2 == True and jugador1 == False:
        dibujarO(x,y)

    if turno == 0:
        clearscreen()
        main()

def main():
    """
    la función reincia el juego, a excepcion del puntaje sumado hasta el momento, en el caso de empate o de haber ganado
    """
    global turno, jugador1, jugador2, puntaje1, puntaje2, a, b, c, d, e, f, g, h, i, a1, b1, c1, d1, e1, f1, g1, h1, i1
    graficas.graf_tricky(cuadrante)
    puntajes()
    onscreenclick(getPos)
    a, b, c, d, e, f, g, h, i, a1, b1, c1, d1, e1, f1, g1, h1, i1 = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    turno = 9
    jugador1 = True
    jugador2 = False
    mainloop()
    
def puntajes():
    """
    La función pinta en pantalla el tablero de puntaje
    """
    global puntaje1, puntaje2
    goto(-150,-100)
    pendown()
    write("player 1= " + str(puntaje1), font=('Arial',30,'normal'))
    penup()
    goto(-150,-150)
    pendown()
    write("player 2= " + str(puntaje2), font=('Arial',30,'normal'))

def dibujarX(x,y):
    """
    La función recibe las coordenadas x,y 
    Comprueba el cuadrante en el que el jugador hizo click, escribe la X y cambia de turno
    """
    global turno, jugador1, jugador2, puntaje1, puntaje2, a, b, c, d, e, f, g, h, i, a1, b1, c1, d1, e1, f1, g1, h1, i1, cuadrante
    pencolor("violet")
    if x > 0 and x < cuadrante:
        if y > 0 and y < cuadrante and a == 0 and a1 == 0:
            penup()
            goto(cuadrante/2, 0-15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            a = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > cuadrante and y < 2*cuadrante and d == 0 and d1 == 0:
            penup()
            goto (cuadrante/2, cuadrante - 15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            d = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > 2*cuadrante and y < 3*cuadrante and g == 0 and g1 == 0:
            penup()
            goto (cuadrante/2, 2 * cuadrante - 15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            g = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
    elif x > cuadrante and x < 2*cuadrante:
        if y > 0 and y < cuadrante and b == 0 and b1 == 0:
            penup()
            goto(cuadrante+cuadrante/2, 0-15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            b = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > cuadrante and y < 2*cuadrante and e == 0 and e1 == 0:
            penup()
            goto (cuadrante+cuadrante/2, cuadrante - 15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            e = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > 2*cuadrante and y < 3*cuadrante and h == 0 and h1 == 0:
            penup()
            goto (cuadrante+cuadrante/2, 2 * cuadrante - 15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            h = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
    elif x > 2 * cuadrante and x < 3 * cuadrante:
        if y > 0 and y < cuadrante and c == 0 and c1 == 0:
            penup()
            goto(cuadrante+cuadrante+cuadrante/2, -15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            c = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        if y > cuadrante and y < 2*cuadrante and f == 0 and f1 == 0:
            penup()
            goto (cuadrante+cuadrante+cuadrante/2, cuadrante - 15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            f = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > 2*cuadrante and y < 3*cuadrante and i == 0 and i1 == 0:
            penup()
            goto (cuadrante+cuadrante+cuadrante/2, 2 * cuadrante - 15)
            write('X', align = 'center', font= ('Arial', fontsize, 'normal'))
            i = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
            
def dibujarO(x,y):
    """
    La función recibe las coordenadas x,y 
    Comprueba el cuadrante en el que el jugador hizo click, escribe la X y cambia de turno
    """
    global turno, jugador1, jugador2, puntaje1, puntaje2, a, b, c, d, e, f, g, h, i, a1, b1, c1, d1, e1, f1, g1, h1, i1, cuadrante
    pencolor("green")
    if x > 0 and x < cuadrante:
        if y > 0 and y < cuadrante and a == 0 and a1 == 0:
            penup()
            goto(cuadrante/2, 0-15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            a1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > cuadrante and y < 2*cuadrante and d == 0 and d1 == 0:
            penup()
            goto (cuadrante/2, cuadrante - 15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            d1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > 2*cuadrante and y < 3*cuadrante and g == 0 and g1 == 0:
            penup()
            goto (cuadrante/2, 2 * cuadrante - 15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            g1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 1
        else:
            print("elija otra casilla")
    elif x > cuadrante and x < 2 * cuadrante:
        if y > 0 and y < cuadrante and b == 0 and b1 == 0:
            penup()
            goto(cuadrante+cuadrante/2, -15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            b1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > cuadrante and y < 2*cuadrante and e == 0 and e1 == 0:
            penup()
            goto (cuadrante+cuadrante/2, cuadrante - 15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            e1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > 2*cuadrante and y < 3*cuadrante and h == 0 and h1 == 0:
            penup()
            goto (cuadrante+cuadrante/2, 2 * cuadrante - 15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            h1 = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
    elif x > 2 * cuadrante and x < 3 * cuadrante:
        if y > 0 and y < cuadrante and c == 0 and c1 == 0:
            penup()
            goto(cuadrante+cuadrante+cuadrante/2, -15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            c1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 
        else:
            print("elija otra casilla")
        if y > cuadrante and y < 2*cuadrante and f == 0 and f1 == 0:
            penup()
            goto (cuadrante+cuadrante+cuadrante/2, cuadrante - 15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            f1 = 1
            jugador1 = False
            jugador2 = True
            turno -= 1
        else:
            print("elija otra casilla")
        if y > 2*cuadrante and y < 3*cuadrante and i == 0 and i1 == 0:
            penup()
            goto (cuadrante+cuadrante+cuadrante/2, 2 * cuadrante - 15)
            write('O', align = 'center', font= ('Arial', fontsize, 'normal'))
            i1 = 1
            jugador2 = False
            jugador1 = True
            turno -= 1
        else:
            print("elija otra casilla")

def ganador():
    """
    La funcion compara las casillas adyacentes y sus valores en todas las posibles formas de ganar para ambos jugadores
    """
    global a, b, c, d, e, f, g, h, i, a1, b1, c1, d1, e1, f1, g1, h1, i1, puntaje1, puntaje2
    if e == 1:
        if a == 1 and i == 1:
            puntaje1 += 1
            turno = 0
        elif b == 1 and h == 1:
            puntaje1 += 1
            turno = 0
        elif c == 1 and g == 1:
            puntaje1 += 1
            turno = 0
        elif d == 1 and f == 1:
            puntaje1 += 1
            turno = 0
    if g == 1:
        if a == 1 and d == 1:
            puntaje1 += 1
            turno = 0
        elif h == 1 and i == 1:
            puntaje1 += 1
            turno = 0
    if c == 1:
        if b == 1 and a == 1:
            puntaje1 += 1
            turno = 0
        elif f == 1 and i == 1:
            puntaje1 += 1
            turno = 0
    if e1 == 1:
        if a1 == 1 and i1 == 1:
            puntaje2 += 1
            turno = 0
        elif b1 == 1 and h1 == 1:
            puntaje2 += 1
            turno = 0
        elif c1 == 1 and g1 == 1:
            puntaje2 += 1
            turno = 0
        elif d1 == 1 and f1 == 1:
            puntaje2 += 1
            turno = 0
    if g1 == 1:
        if a1 == 1 and d1 == 1:
            puntaje2 += 1
            turno = 0
        elif h1 == 1 and i1 == 1:
            puntaje2 += 1
            turno = 0
    if c1 == 1:
        if b1 == 1 and a1 == 1:
            puntaje2 += 1
            turno = 0
        elif f1 == 1 and i1 == 1:
            puntaje2 += 1
            turno = 0
            

main()
