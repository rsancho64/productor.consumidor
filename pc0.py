#! /usr/bin/python3

def productor():
    answ = 22
    print(f" productor: {answ}" )
    return answ

def consumidor(item):
    print(f"consumidor: {item}" )

if __name__ == "__main__":

    algo = productor()
    consumidor(algo)




    