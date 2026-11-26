import random
player_pool = []
computer_pool = []
bard = []
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
    tile_divider(pool)  
    return True

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
def tile_divider(pool):
    for i in range(9):
        player_pool.append(pool[0])
        pool.pop(0)
        computer_pool.append(pool[0])
        pool.pop(0)
       
# def is_valid_set(type,tiles):
#     if type == "computer":
#         if check_series(tiles):
#             return True
#         if check_set_computer(tiles):
#             return True
#         return False
#     if type == "player":
#         if check_series(tiles):
#             return True
        
# def check_set_computer(tiles):
#     kinds = [[],[],[],[]]
#     for tile in tiles:
#         if tile[1] == "R":
#             kinds[0].append(tile)
#         elif tile[1] == "B":
#             kinds[1].append(tile)  
#         elif tile[1] == "K":
#             kinds[2].append(tile)
#         elif tile[1] == "O":
#             kinds[3].append(tile)
#     print(kinds)  
#     sort_kinds = []
#     for i in [3,2,1,0]:
#         if len(kinds[i]) < 3:
#             kinds.pop(i)
#             continue
#         sort_kinds.append(sorted(kinds[i],key=lambda x: x[0]))
#     print(sort_kinds)
        
#     # kind_set = set(get_kind(tiles))
#     # result = []
#     for k in sort_kinds:
#         i = 1
#         count = 1
#         nums_tiles = get_nums(k)
#         for num in nums_tiles:
#             if num +i in nums_tiles:
#                 count +=1
#                 i += 1
#             else:
#                 break
#         if count >=3:
                
#         # count = 1
#         # while True:
#         #     min_num = min(nums_tiles)
#         #     if len(nums_tiles) < 3 or count >=3:
#         #         break
#         #     for i in range(len(tiles)):
#         #         if (min_num[0]) + 1 in nums_tiles:
#         #             count +=1
#         #             min_num +=1
#         #         else:
#         #             if count <3:
#         #                 nums_tiles.remove(min_num)
#         #                 count = 1
#         #             break
#         # if len(nums_tiles) >= 3:
#         #     return True
#         # return False           

def check_series(tiles):
    kinds_tiles = get_kind(tiles)
    nums_tiles = get_nums(tiles)
    num = nums_tiles.count(nums_tiles[0])
    kind = kinds_tiles.count(kinds_tiles[0])
    if num ==3 or num ==4:
        if kind >1:
            return False            
        return True
    return False

def get_kind(tiles):
    kinds= []
    for tile in tiles:
        kinds.append(tile[1])
    return kinds

def get_nums(tiles):
    nums= []
    for tile in tiles:
        nums.append(tile[0])
    return nums  
def play_set(hand, table, indexes):
    pass
# print(is_valid_set("computer",[(5, 'K'),(9, 'R'),(10, 'R'),(11, 'R')]))
# create_pool()  
# print(computer_pool)
# check_set_computer(computer_pool)