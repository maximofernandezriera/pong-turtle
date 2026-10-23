"""Pong mínimo con turtle — versión para clase (DAW / Think Python).

Dos jugadores:
  - Izquierdo: teclas W (subir) y S (bajar)
  - Derecho:   flechas Arriba / Abajo

Conceptos que practica: bucle principal, coordenadas, condicionales,
colisiones y funciones.
"""
import turtle

ANCHO, ALTO = 800, 600

# ---------- ventana ----------
pantalla = turtle.Screen()
pantalla.title("Pong básico")
pantalla.bgcolor("black")
pantalla.setup(width=ANCHO, height=ALTO)
pantalla.tracer(0)          # dibujamos a mano para que no parpadee

# ---------- marcador ----------
puntos_izq = 0
puntos_der = 0

marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.color("white")
marcador.goto(0, ALTO // 2 - 50)

def escribir_marcador():
    marcador.clear()
    marcador.write(f"{puntos_izq}   :   {puntos_der}",
                   align="center", font=("Courier", 24, "bold"))

# ---------- palas ----------
def crear_pala(x):
    pala = turtle.Turtle()
    pala.shape("square")
    pala.color("white")
    pala.shapesize(stretch_wid=5, stretch_len=1)  # 100x20 px
    pala.penup()
    pala.goto(x, 0)
    return pala

pala_izq = crear_pala(-ANCHO // 2 + 40)
pala_der = crear_pala(ANCHO // 2 - 40)

# ---------- pelota ----------
pelota = turtle.Turtle()
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.25          # velocidad: píxeles por fotograma
pelota.dy = 0.25

def reiniciar_pelota():
    pelota.goto(0, 0)
    pelota.dx = -pelota.dx   # saca el que acaba de recibir el punto

# ---------- controles ----------
def izq_arriba():
    if pala_izq.ycor() < ALTO // 2 - 60:
        pala_izq.sety(pala_izq.ycor() + 20)

def izq_abajo():
    if pala_izq.ycor() > -ALTO // 2 + 60:
        pala_izq.sety(pala_izq.ycor() - 20)

def der_arriba():
    if pala_der.ycor() < ALTO // 2 - 60:
        pala_der.sety(pala_der.ycor() + 20)

def der_abajo():
    if pala_der.ycor() > -ALTO // 2 + 60:
        pala_der.sety(pala_der.ycor() - 20)

pantalla.listen()
pantalla.onkey(izq_arriba, "w")
pantalla.onkey(izq_abajo, "s")
pantalla.onkey(der_arriba, "Up")
pantalla.onkey(der_abajo, "Down")

escribir_marcador()

# ---------- bucle principal ----------
while True:
    pantalla.update()

    # mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # rebote arriba / abajo
    if pelota.ycor() > ALTO // 2 - 10 or pelota.ycor() < -ALTO // 2 + 10:
        pelota.dy = -pelota.dy

    # punto para la derecha (la pelota sale por la izquierda)
    if pelota.xcor() < -ANCHO // 2:
        puntos_der += 1
        escribir_marcador()
        reiniciar_pelota()

    # punto para la izquierda (la pelota sale por la derecha)
    if pelota.xcor() > ANCHO // 2:
        puntos_izq += 1
        escribir_marcador()
        reiniciar_pelota()

    # rebote en las palas: está a su altura x y dentro de su rango y
    if pelota.xcor() > ANCHO // 2 - 60 and pelota.dx > 0:
        if abs(pelota.ycor() - pala_der.ycor()) < 50:
            pelota.dx = -pelota.dx

    if pelota.xcor() < -ANCHO // 2 + 60 and pelota.dx < 0:
        if abs(pelota.ycor() - pala_izq.ycor()) < 50:
            pelota.dx = -pelota.dx
