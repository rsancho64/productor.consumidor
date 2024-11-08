#! /usr/bin/python3

"""inspirado por el gran Oscar"""

import random
import time
import asyncio

algo = None

async def productor():

    global algo
    
    while True:

        snaptime = random.randint(0, 10)
        print(f" productor: me voy a dormir: {snaptime} s.")        
        await asyncio.sleep(snaptime)  

        answ = random.randint(1, 6)
        print(f" productor: {answ}")
        algo = answ

async def consumidor():

    global algo

    while True:

        snaptime = random.randint(0, 10)            
        print(f"consumidor: me voy a dormir: {snaptime} s.")        
        await asyncio.sleep(snaptime)  

        if algo is not None:
            print(f"consumidor: {algo}")


async def main():

    await asyncio.gather(
        productor(),
        consumidor()
    )

if __name__ == "__main__":
    
    asyncio.run(main())