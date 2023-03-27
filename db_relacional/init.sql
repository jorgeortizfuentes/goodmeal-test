CREATE TABLE Usuario (
  id_usuario SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  correo VARCHAR(255),
  telefono VARCHAR(255),
  direccion VARCHAR(255)
);

CREATE TABLE Tienda (
  id_tienda SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  tipo_tienda VARCHAR(255),
  direccion VARCHAR(255)
);

CREATE TABLE Producto (
  id_producto SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  precio DECIMAL(10,2)
);

CREATE TABLE Compra (
  id_compra SERIAL PRIMARY KEY,
  id_usuario INTEGER REFERENCES Usuario(id_usuario),
  id_tienda INTEGER REFERENCES Tienda(id_tienda),
  fecha_compra DATE,
  tipo_pago VARCHAR(255),
  id_cupon INTEGER REFERENCES Cupon(id_cupon),
  monto_delivery DECIMAL(10,2),
  monto_total DECIMAL(10,2),
  estado VARCHAR(255)
);

CREATE TABLE Delivery (
  id_delivery SERIAL PRIMARY KEY,
  id_compra INTEGER REFERENCES Compra(id_compra),
  direccion VARCHAR(255),
  monto DECIMAL(10,2)
);

CREATE TABLE Cancelacion (
  id_cancelacion SERIAL PRIMARY KEY,
  id_compra INTEGER REFERENCES Compra(id_compra),
  motivo VARCHAR(255),
  fecha_cancelacion DATE
);

CREATE TABLE Cupon (
  id_cupon SERIAL PRIMARY KEY,
  codigo_cupon VARCHAR(255),
  tipo_descuento VARCHAR(255),
  valor_descuento DECIMAL(10,2),
  fecha_vencimiento DATE
);