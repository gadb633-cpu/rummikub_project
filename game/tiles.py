import random

def create_pool():
    pool = []
    count = 1
    number = 1
    colors = ["R","B","K","O"]
    color = 0
    for tile in range(104):
        pool.append((number,colors[color]))
        if count ==1:
            count +=1
            continue
        if count ==2:
            count = 1
            if number == 13:
                number = 1
                color +=1     
                continue
            number +=1
    Shuffling_tiles(pool)      
    return pool
def Shuffling_tiles(pool):
    for num in range(3000):
        num1 = random.randint(0,103)
        while True:
            num2 = random.randint(0,103)
            if num1 == num2:
                continue
            else:
                break
        index = pool[num1]
        pool[num1] = pool[num2]
        pool[num2] = index

