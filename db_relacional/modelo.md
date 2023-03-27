# Modelo relacional:

- Tabla Usuario: id_usuario (PK), nombre, correo, teléfono, dirección.
- Tabla Tienda: id_tienda (PK), nombre, tipo_tienda (Mono GoodBag, Multi GoodBag, Multi Producto), dirección.
- Tabla Producto: id_producto (PK), nombre, precio.
- Tabla Compra: id_compra (PK), id_usuario (FK), id_tienda (FK), fecha_compra, tipo_pago (credito, debito, webpay, gmc), id_cupon (FK), monto_delivery, monto_total, estado (realizada, cancelada).
- Tabla Delivery: id_delivery (PK), id_compra (FK), dirección, monto.
- Tabla Cancelación: id_cancelación (PK), id_compra (FK), motivo, fecha_cancelación.
- Tabla Cupon: id_cupon (PK), codigo_cupon, tipo_descuento (porcentaje, monto fijo), valor_descuento, fecha_vencimiento.
