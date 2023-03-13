# Productores_Y_Consumidores

El enlace al repositorio es el siguiente : [Productores_Y_Consumidores](https://github.com/migueliiin/Productores_Y_Consumidores.git)

# Explicacion del código

Basicamente lo que hace este código es crear dos hilos, uno que ejecuta el bucle del Productor y el otro que ejecuta el bucle del Consumidor.
Ambos bucles estan comunicados gracias al metodo task_done(), este metodo lo podemos encontrar en el bucle del consumidor, que básicamente lo que hace es enviar una señal al Productor cuando a "almacenado el elemento" que previamente fue producido por el Constructor.