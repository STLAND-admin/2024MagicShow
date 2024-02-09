import numpy as np


def HappyNewYear(name: str= "Happy New Year!" ,wherefrom: str= "nowhere", gender: str= "helicopter"):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    
    # 随机生成四张牌
    init_array = np.random.randint(1, 14, size=(4) )
    print("初始牌：")
    print(init_array)


    # 撕开并且同方向放置 
    sikai_array = init_array 
    init_array = np.concatenate((init_array, sikai_array)) 
    print("撕开牌并同方向放置：")
    print(init_array)


    # 根据名字长度 调整顺序
    nameLen = len(name) % len(init_array)
    # 将 nameLen 张牌调整到最后
    rolled_array = np.roll(init_array, -nameLen)
    print("调整顺序：")
    print(rolled_array)


    # 将 前三张 取出 并放入 数组中任意位置
    first_three = rolled_array[:3]
    insert_pos = np.random.randint(1, len(rolled_array) - 3) # 必须插入中间
    rolled_array = np.insert(rolled_array[3:], insert_pos, first_three)
    print(f"取出前三张：{first_three}并放入任意位置：{insert_pos}")
    print(rolled_array)


    # 拿出最上面的卡片 
    the_card = rolled_array[0]
    print(f"拿出最上面的卡片---------------------------------------------------------------------------{the_card}")
    rolled_array = rolled_array[1:]
    print(f"剩余牌：{rolled_array}")


    # 南方人 1 张 北方人 2 张 不确定 3 张
    # 与 上一步一样 取出并随即放入
    if "南" in wherefrom:
        pick_num = 1
    elif "北" in wherefrom:
        pick_num = 2
    else:
        pick_num = 3
    picked_array = rolled_array[:pick_num]
    insert_pos = np.random.randint(1, len(rolled_array) - pick_num)
    rolled_array = np.insert(rolled_array[pick_num:], insert_pos, picked_array)
    print("南方人 1 张 北方人 2 张 不确定 3 张")
    print(f"取出{pick_num}张：{picked_array}并放入任意位置：{insert_pos}")
    print(rolled_array)


    # 男生 1 张 女生 2 张 
    # 丢弃
    if "男" in gender:
        drop_num = 1
    elif "女" in gender:
        drop_num = 2
    else:
        drop_num = np.random.randint(1, 3)

    dropped_array = rolled_array[:drop_num]
    rolled_array = rolled_array[drop_num:]

    print("男生 1 张 女生 2 张")
    print(f"丢弃{drop_num}张：{dropped_array}")
    print(f"剩余牌：{rolled_array}")
    # 见证奇迹的时刻
    magic_array = np.roll(rolled_array, -7) 
    print("接下来就是--")
    print("见证奇迹的时刻：")
    print(magic_array)

    # 好运留下来，烦恼丢出去
    flag = True
    while len(magic_array) > 1:
        # put first card from magic_array to the end of magic_array 
        # and drop first card from magic_array
        # till magic_array has only one card
        if flag:
            haoyun_card = magic_array[0]
            magic_array = np.concatenate((magic_array[1:], [haoyun_card]))
            print(f"好运 {haoyun_card} 留下来{magic_array}")
            flag = False
        else:
            fannao_card = magic_array[0]
            magic_array = magic_array[1:]
            print(f"烦恼丢出去{fannao_card}")
            flag = True

    last_card = magic_array[0]
    print(f"最后一张牌：{last_card}")
    print(f"之前取出的牌：{the_card}")
    if name != "Happy New Year!":
        print(f" {name} 祝你新年快乐，身体健康，万事如意！!")

if __name__ == '__main__':
    HappyNewYear("STLAND-admin","南方人","男生")
