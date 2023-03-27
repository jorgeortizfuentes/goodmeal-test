# Test técnico - Data Engineer

En el equipo de GoodMeal queremos evaluar tus capacidades en modelamiento de datos y manejo de ingeniería de datos y ETL con Python. (Si quieres usar otro lenguaje, por favor coméntalo).
Para esto decidimos crear la siguiente prueba en la cual se evaluará tu lógica de abstracción del negocio a los datos y la creación de scripts para ETL.
Test
En GoodMeal, somos un marketplace de excedentes, tenemos una gran variedad tiendas de todo tipo (restaurantes, comida rápida, pastelerías, etc), todas estas tiendas tienen diferentes tipos de funcionamiento (GoodBag, es un tipo de producto que es una bolsa sorpresa):

- Mono GoodBag: donde venden un solo tipo de producto del tipo GoodBag 
- Multi GoodBag: donde pueden vender diferentes tipos de productos del tipo GoodBag.
- Multi Producto: donde venden cualquier tipo de producto.

El modelo de negocio funciona de la siguiente manera:
- Un usuario puede comprar N cantidad de productos de una sola tienda. - Un usuario puede comprar ingresando su tarjeta de crédito o débito y/o pagar con webpay (servicio de pago externo), y también puede pagar con cupones (hasta 50% descuento) y usar GoodMeal Coins (GMC), que puede comprar con anticipación (1 GMC = $1)
- Un usuario, además, puede agregar delivery a su compra, lo cual aumenta el valor final. 
- Algunos pagos con webpay, pueden ser cancelados.
- Considerar las direcciones relacionadas (tiendas, personas, delivery, etc)

Tu deber es:

1. Crear un modelo relacional que pueda soportar la lógica de negocio anterior.
2. Crear un modelo BI en estrella o snowflake para analítica de datos, para analizar la información de GoodMeal y el dinero que se obtiene.
3. Realizar diversas consultas sql, que podamos probar en un Jupyter notebook. (Debes dockerizar tu proyecto)

- ¿Cómo podemos saber cuántos usuarios nuevos tenemos semana a semana y mes por mes?
- Cuanto es el tiempo de vida de los usuarios? (considerando que compran al menos 4 veces a la semana)
- ¿Cómo podemos obtener los que menos vida tienen? ¿Y los que más? - ¿Cuántas tiendas distintas, han comprado los usuarios? ¿Cómo podemos tener un ranking de tiendas?
- ¿Qué métricas crees tú que puedan servir, para medir el impacto económico del modelo?

4. Crea un proceso de ETL en python o el lenguaje que creas conveniente con el objetivo de migrar los datos del modelo relacional que creaste anteriormente hasta el modelo estrella o snowflake que también creaste previamente. Queremos que nos demuestres tus habilidades como data cleaning y uso de pandas.

5. Generar un dashboard muy visual, para responder las preguntas del punto 3. 6. 

Para los datos, puedes generar datos aleatorios, considera lo siguiente: 
   a. Al menos un 70% de compras realizadas
   b. Volumen de unos 6 meses (para sacar datos representativos)
   c. Considera que el aumento de usuarios es del 10% mes a mes (parte con 5K)

  Nota: Puedes asumir que el datawarehouse donde está alojado el modelo de BI, puede ser cualquier base de datos columnar que manejes. (Recomendación Postgresql, puedes usar lo que consideres adecuado, incluyendo SQLite, si no son muchos datos)

Formato de entrega

- Enviar enlace a github o gitlab con el proyecto, Jupyter notebooks pueden funcionar sin problemas en github o gitlab.
- Enviar url del proyecto, para visualizar el dashboard.
  ○ Si no tienes un servidor para levantar tu proyecto, para que podamos probarlo, puedes usar alguna de las siguientes alternativas gratuitas
  ■ Render.com (recomendado)
  ■ Qoddi.com
  ■ netifly.com
  Evaluación
  Puntos a tener en cuenta, al momento de evaluar:
- Debes cumplir los puntos definidos en el apartado de test.
- Debes cumplir el formato de entrega.
- Para el repositorio:
  ○ Importante que venga con un readme, para entender el proyecto y poder levantarlo y probarlo. Recuerda usar docker.
  ○ Leeremos la historia de tus commits, con el fin de entender tu forma de trabajar y ver como llegaste a una solución. Usa comentarios que permitan entender qué hiciste.
  ○ Usa buenas prácticas de código y comentarios donde sea debido.
