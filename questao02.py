import multiprocessing
import time
import random

def legal(valor):
    id = valor[0]
    valores = valor[1]

    soma = 0

    print ("começando a operação", id)

    for i in range(5):
        soma = soma + valores[i]
        time.sleep (0.2)

    print ("linha", id, "- resultado da soma:", soma)
    print ("terminando a operação", id)

def main():
    id = 0

    valor1 = random.randint (1, 100)
    valor2 = random.randint (1, 100)
    valor3 = random.randint (1, 100)
    valor4 = random.randint (1, 100)
    valor5 = random.randint (1, 100)

    valores = [valor1, valor2, valor3, valor4, valor5]

    args = [0]*3

    for i in range(3):
        args[i] = [id+i, valores]

    with multiprocessing.Pool(processes=3) as pool:
        pool.map(legal, args)

if __name__ == "__main__":
    main ()
