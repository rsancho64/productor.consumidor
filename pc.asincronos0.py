#! /usr/bin/python3

import random
import time
import asyncio

algo = None

async def productor():

    global algo

    while True:
        answ = random.randint(1,6)
        
        snaptime = random.randint(0,10)
        print(f" siestatime: {snaptime}" )
        time.sleep(snaptime)    

        print(f"  productor: {answ}" )
        algo = answ

async def consumidor():

    global algo

    while True:
        print(f" consumidor: {algo}" )

if __name__ == "__main__":

    productor()
    consumidor()





    