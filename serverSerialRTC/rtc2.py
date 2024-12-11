from machine import Pin
import machine

count = 0

# Configura el pin del botón
button_pin = Pin(14, Pin.IN, Pin.PULL_UP)  # Cambia el número de pin según tu configuración

def button_pressed(pin):
    global count
    # Modifica count cuando se presiona el botón
    count += 1  # Cambia el valor que deseas agregar a count
    print(count)  # Imprime el nuevo valor de count

# Configura la interrupción para el botón
button_pin.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

# Mantiene el programa en ejecución
while True:
    pass  # Puedes agregar otras funcionalidades aquí si lo deseas
