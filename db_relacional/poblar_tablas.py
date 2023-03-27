import random
import string
import datetime
import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env para la configuración de la conexión a la base de datos. 
load_dotenv('.env')

# Obtener el valor de las variables de entorno
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = "localhost"

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

# Generación de datos aleatorios
nombres = ['Marcianeke', 'Pailita', 'Epidemia', 'Juanin', 'Tulio', 'Patana', 'Juan', 'Pedro', 'María', 'Andrea', 'Luis', 'Lucas', 'Ana', 'Laura', 'Carlos', 'David', 'Sofía', 'Valentina', 'Camila', 'Miguel', 'Javiera', 'Antonio', 'Francisco', 'Jorge', 'Fernando', 'Javier', 'Mariana', 'Daniela', 'Cristóbal', 'Felipe', 'Diego', 'Pablo', 'Agustín', 'Martín', 'Santiago', 'Matías', 'Isabella', 'Isidora', 'Constanza', 'Renato', 'Benjamín', 'Emilia', 'Valentino', 'Tomás', 'Bastián', 'Alexis', 'Alexandra', 'Alexa', 'Alejandro', 'Alejandra', 'Alonso', 'Alondra', 'Alfredo', 'Alfonso', 'Alma', 'Alvaro', 'Amanda', 'Amelia', 'Américo', 'América', 'Ana María', 'Ana Sofía', 'Andrés', 'Ángel', 'Ángela', 'Antonia', 'Antonio', 'Ariel', 'Ariana', 'Arturo', 'Astrid', 'Augusto', 'Bautista', 'Benito', 'Benjamín', 'Bianca', 'Boris', 'Brayan', 'Brayam', 'Brayan']
apellidos = ['Pérez', 'González', 'García', 'Martínez', 'Hernández', 'López', 'Díaz', 'Sanchez', 'Vásquez', 'Fernández', 'Ortiz', 'Ramírez', 'Cruz', 'Álvarez', 'Torres', 'Reyes', 'Romero', 'Flores', 'Castillo', 'Rojas', 'Gómez', 'Mendoza', 'Morales', 'Castro', 'Chávez', 'Gutiérrez', 'Ruiz', 'Vega', 'Soto', 'Aguilar', 'Jiménez', 'Silva', 'León', 'Campos', 'Montes', 'Carrillo', 'Moreno', 'Herrera', 'Avila', 'Barrera', 'Méndez', 'Rivas', 'Acosta', 'Fuentes', 'Galván', 'Núñez', 'Salazar', 'Medina', 'Cortés', 'Pacheco', 'Valdez', 'Ávila', 'Valencia', 'Maldonado', 'Bautista', 'Bonilla', 'Galindo', 'Escobar', 'Santana', 'Serrano', 'Zamora', 'Cervantes', 'Castañeda', 'Lara', 'Cabrera', 'Lozano', 'Rosales', 'Juárez', 'Miranda', 'Peralta', 'Cisneros', 'Benítez', 'Herrero', 'Saucedo', 'Solís', 'Carmona', 'Orozco', 'Villanueva', 'Villarreal', 'Peña', 'Ochoa', 'Rangel', 'Guzmán', 'Ponce', 'Corona', 'Aguiar', 'Cárdenas', 'Barrera', 'Gallardo', 'Salinas', 'Pineda', 'Rico', 'Arroyo', 'Cano', 'Esquivel', 'Quiroz', 'Delgado', 'Osorio', 'Luna', 'Marín', 'Téllez', 'Uribe', 'Zavala', 'Calderón', 'Vera', 'Sandoval', 'Sosa', 'Guzmán', 'Leyva', 'Montiel', 'Montoya', 'Vargas', 'Guzmán', 'Vallejo', 'Álvarez', 'Ríos', 'Báez', 'Becerra', 'Rocha', 'Larios', 'Miramontes', 'Bernal', 'Gallardo', 'Aranda', 'Bravo', 'Morán', 'Trejo', 'Barajas', 'Esparza', 'Grijalva', 'Hernández', 'López', 'Márquez', 'Olivera', 'Quiñones', 'Soria', 'Zaragoza', 'Bustamante', 'Nava', 'Sandoval', 'Castañón', 'Fajardo', 'Guevara', 'Laguna', 'Leyva', 'Linares', 'Méndez', 'Juárez', 'Pérez', 'Porras', 'Villegas', 'Alvarado', 'Barrera', 'García', 'Mendoza', 'Reyes', 'Robles', 'Vázquez', 'Carrillo', 'Chávez', 'Cruz', 'Gómez', 'Hernández', 'Jiménez', 'Montes', 'Navarro', 'Pacheco', 'Rojas', 'Sanchez', 'Vega', 'Zambrano', 'Ávila', 'Cortés', 'Díaz', 'Estrada', 'Flores', 'Galván', 'Herrera', 'Ibarra', 'Jaramillo', 'Kuri', 'Leal', 'Madrigal', 'Navarro', 'Ortega', 'Pérez', 'Quezada', 'Ramos', 'Sánchez', 'Tovar', 'Urbina', 'Valdés', 'Yáñez', 'Zamudio', 'Alonso', 'Briones', 'Castro', 'Dávila', 'Enríquez', 'Franco', 'González', 'Huerta', 'Izquierdo', 'Jiménez', 'Kuri', 'López', 'Mendoza', 'Nieto', 'Ortiz', 'Pinedo', 'Quintero', 'Ríos', 'Santillán', 'Téllez', 'Urías', 'Villalobos', 'Zamudio', 'Aguilera', 'Borrego', 'Córdova', 'Díaz', 'Esparza', 'Fuentes', 'García', 'Hernández', 'Izquierdo', 'Jaramillo', 'Kuri', 'López', 'Mendoza', 'Nieto', 'Ortiz', 'Pinedo', 'Quintero', 'Ríos', 'Santillán', 'Téllez', 'Urías', 'Villalobos', 'Zamudio', 'Aguilera', 'Borrego', 'Córdova', 'Díaz', 'Esparza', 'Fuentes', 'García', 'Hernández', 'Izquierdo', 'Jaramillo', 'Kuri', 'López', 'Mendoza', 'Nieto', 'Ortiz', 'Pinedo', 'Quintero', 'Ríos', 'Santillán', 'Téllez', 'Urías', 'Villalobos', 'Zamudio', 'Aguilera', 'Borrego', 'Córdova', 'Díaz', 'Esparza', 'Fuentes', 'García', 'Hernández', 'Izquierdo', 'Jaramillo', 'Kuri', 'López', 'Mendoza', 'Nieto', 'Ortiz', 'Pinedo', 'Quintero', 'Ríos', 'Santillán', 'Téllez', 'Urías', 'Villalobos']
correos = ["@gmail.com", "@hotmail.com", "@live.com", "@outlook.com", "@yahoo.com"]
usuarios = []
for i in range(5000):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos) + ' ' + random.choice(apellidos)
    correo = random.choice(correos)
    usuario = nombre.lower() + '.' + apellido.lower().replace(" ", ".") + str(i) + correo
    usuarios.append((nombre + ' ' + apellido, usuario))

# Generar lista de tiendas
tiendas = [('Panadería Colo Colo', 'Mono GoodBag'), ('Sandwicheria El Pelao', 'Multi GoodBag'), ('Bar Sinson', 'Multi Producto'), ('Juan Maestro', 'Mono GoodBag'), ('Churretes', 'Mono GoodBag'), ('Comida rica', 'Multi Producto'), ('Mac Donald Trump', 'Mono GoodBag'), ('Pastelería Tronchatoro', 'Mono GoodBag'), ('Pastelería Tu Nene Malo', 'Multi GoodBag'), ('El Pescador', 'Multi Producto')]

# Generar lista de productos
productos = [('Pizza', 4990), ('Sandwich', 3990), ('Fruta', 2990), ('Galletas', 5490), ('Pasteles', 7990), ('Churros', 3990), ('Donuts', 4990), ('Almuerzo', 5990), ('Sushi', 9990), ('Frituras', 6990)]

# Generar lista de cupones
cupones = [('CUPON1', 'porcentaje', 20, datetime.date(2022, 12, 31)), ('CUPON2', 'monto', 5000, datetime.date(2022, 12, 31)), ('CUPON3', 'porcentaje', 10, datetime.date(2022, 12, 31)), ('CUPON4', 'monto', 2000, datetime.date(2022, 12, 31)), ('CUPON5', 'porcentaje', 15, datetime.date(2022, 12, 31))]

# Generar compras aleatorias
now = datetime.datetime.now()
for i in range(30000):
    # Generar datos aleatorios para la compra
    usuario = random.choice(usuarios)
    tienda = random.choice(tiendas)
    producto = random.choice(productos)
    fecha_compra = now - datetime.timedelta(days=random.randint(0, 180))
    tipo_pago = random.choice(['credito', 'debito', 'webpay', 'gmc'])
    id_cupon = random.choice([None, random.randint(1,5)])
    monto_delivery = random.choice([0, 990, 1990])
    monto_total = producto[2] + monto_delivery
    estado = random.choice(['realizada', 'cancelada'])

    # Insertar datos en la tabla Compra
    cursor.execute("INSERT INTO Compra (id_usuario, id_tienda, fecha_compra, tipo_pago, id_cupon, monto_delivery, monto_total, estado) VALUES ((SELECT id_usuario FROM Usuario WHERE correo = %s), (SELECT id_tienda FROM Tienda WHERE nombre = %s), %s, %s, %s, %s, %s, %s)", (usuario[1], tienda[0], fecha_compra, tipo_pago, id_cupon, monto_delivery, monto_total, estado))

    # Si la compra fue realizada, insertar datos en las tablas Delivery y Cancelación
    if estado == 'realizada':
        id_compra = cursor.lastrowid
        direccion = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
        monto = monto_delivery
        cursor.execute("INSERT INTO Delivery (id_compra, direccion, monto) VALUES (%s, %s, %s)", (id_compra, direccion, monto))
        if tipo_pago == 'webpay' and random.choice([True, False]):
            motivo = random.choice(['Error en el pago', 'No se realizó el cargo', 'Problemas con el banco'])
            fecha_cancelacion = fecha_compra + datetime.timedelta(days=random.randint(1, 7))
            cursor.execute("INSERT INTO Cancelacion (id_compra, motivo, fecha_cancelacion) VALUES (%s, %s, %s)", (id_compra, motivo, fecha_cancelacion))

conn.commit()
cursor.close()
conn.close()