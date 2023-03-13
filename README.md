# Productores_Y_Consumidores

El enlace al repositorio es el siguiente : [Productores_Y_Consumidores](https://github.com/migueliiin/Productores_Y_Consumidores.git)

# Explicacion del código

Basicamente lo que hace este código es crear dos hilos, uno que ejecuta el bucle del Productor y el otro que ejecuta el bucle del Consumidor.
Ambos bucles estan comunicados gracias al metodo task_done(), este metodo lo podemos encontrar en el bucle del consumidor, que básicamente lo que hace es enviar una señal al Productor cuando a "almacenado el elemento" que previamente fue producido por el mismo.

# Conclusión

Lo que logramos es ahorrar tiempo, no en etse caso, porque el metodo del Consumidor tiene la funcion time.sleep(1) que hace que el programa se pause por un segundo cada vez que el Consumidor "almacena elementos", pero durante ese tiempo, la señal ha llegado al Productor y el Productor genera datos nuevos en ese tiempo.