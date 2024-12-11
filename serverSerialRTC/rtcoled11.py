########## Código para pantalla SSD1306 ######

from machine import Timer, I2C, Pin
import ssd1306  # Cambia a la biblioteca SSD1306
import time

count = 0

# Configuración del I2C para la pantalla OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)  # Ajusta los pines según tu conexión
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Inicializa la pantalla OLED

# Función para actualizar la pantalla
def update_display():
    oled.fill(0)  # Limpia la pantalla
    oled.text('Conteo:', 0, 0)  # Muestra el texto "Conteo:"
    oled.text(str(count), 0, 10)  # Muestra el valor del conteo
    oled.show()  # Actualiza la pantalla

def counter(timer):
    global count
    count += 1
    print(count)
    update_display()  # Actualiza la pantalla con el nuevo conteo

timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=counter)

# El conteo se mostrará en la pantalla OLED indefinidamente
update_display()  # Muestra el conteo inicial
while True:
    time.sleep(1)  # Mantiene el programa en ejecución
