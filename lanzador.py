from queue import Queue
from threading import Thread
import time

# Crear cola

q = Queue(10)

def producer():

    """Productor"""

    count = 1 #mostrador
    while True:
        q.join() # Espera a task_done () para enviar una señal
        q.put(count)
        print(f"Está produciendo el elemento {count}")
        count+=1

def customer():

    """Consumidor"""

    count = 1
    while True:
        baozi = q.get()
        print(f"El consumidor está almacenando el elemento {count}")
        count+=1
        q.task_done() # Envía una señal después de comer
        time.sleep(1)

def main():
    t1 = Thread(target=producer)
    t2 = Thread(target=customer)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()