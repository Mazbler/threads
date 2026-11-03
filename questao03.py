import threading
import random
import time

def corrida(param):
    id = param[0]
    distancia_maxima = param[1]

    distancia = 0

    print ("sapo", id, "começou a corrida")

    while distancia < distancia_maxima:
        salto = random.randint(1, 5)
        distancia = distancia + salto

        if distancia > distancia_maxima:
            distancia = distancia_maxima

        print ("sapo", id, "pulou", salto, "cm de distancia percorrida:", distancia, "cm")

        time.sleep(0.2)

    print ("sapo", id, "chegou ao final da corrida")

def main():
    distancia_maxima = 50

    args = [0]*5

    threads = [0]*5

    for i in range(5):
        args[i] = [i+1, distancia_maxima]

    for i in range(5):
        threads[i] = threading.Thread(target=corrida, args=(args[i],))
        threads[i].start()

    for i in range(5):
        threads[i].join()

    print ("corrida terminada")

main()
