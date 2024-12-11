###### CÓDIGO PARA PANTALLA OLED SH1006 ####

from machine import Pin, I2C
import sh1106
import time

count = 0

# Configura el I2C para la pantalla OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Cambia los pines según tu configuración
oled = sh1106.SH1106_I2C(128, 64, i2c)  # Ajusta el tamaño de la pantalla según tu modelo

# Configura el pin del botón
button_pin = Pin(14, Pin.IN, Pin.PULL_UP)  # Cambia el número de pin según tu configuración

def button_pressed(pin):
    global count
    # Modifica count cuando se presiona el botón
    count += 1  # Cambia el valor que deseas agregar a count
    print(count)  # Imprime el nuevo valor de count
    update_display()  # Actualiza la pantalla OLED

def update_display():
    oled.fill(0)  # Limpia la pantalla
    oled.text('Count:', 0, 0)  # Muestra el texto "Count:"
    oled.text(str(count), 0, 20)  # Muestra el valor de count
    oled.show()  # Actualiza la pantalla

# Configura la interrupción para el botón
button_pin.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

# Inicializa la pantalla OLED
update_display()  # Muestra el conteo inicial

# Mantiene el programa en ejecución
while True:
    time.sleep(1)  # Puedes agregar otras funcionalidades aquí si lo deseas
