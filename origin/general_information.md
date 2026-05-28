# general information
    ## prerequisites
        check manual in the game

    ## Built-in Functions
        ### can_harvest()

        ### can_move(direction)
            检查无人机是否可以向指定 direction 移动。

            如果无人机可以移动，则返回 True，否则返回 False。

        ### change_hat(hat)
            change_hat(Hats.Brown_Hat)
            change_hat(Hats.Gray_Hat)
            change_hat(Hats.Green_Hat)
            change_hat(Hats.Purple_Hat)

        ### clear()

        ### do_a_flip()

        ### get_entity_type()
            判断无人机下方实体的类型。
        
        ### get_ground_type()
            判断无人机下方地块的类型。

            if get_ground_type() != Grounds.Soil:
                till()
        
        ### get_pos_x()
            获取无人机当前的 x 坐标。
            x, y = get_pos_x(), get_pos_y()

            get_pos_y()
            获取无人机当前的 y 坐标。

        ### get_water()
            获取无人机下方地块的当前含水量。
            if get_water() < 0.5:
                use_item(Items.Water
        
        ### get_world_size()
            获取农场的当前大小。

        ### harvest()

        ### measure()

        ### move(direction)
            move() # North, East, South, West

        ### num_items(item)
            查询你当前拥有多少 item。
            if num_items(Items.Fertilizer) > 0:
                use_item(Items.Fertilizer)

        ### num_unlocked(thing)
            用于检查某个解锁项、实体、地块、物品或帽子是否已经解锁。

            #### for maze rendering
                plant(Entities.Bush)
                n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
                use_item(Items.Weird_Substance, n_substance)

        ### pet_the_piggy()

        ### plant()
            plant(Entities.Bush) # 这会在无人机下方的地块上种植 1 丛灌木。

        ### print(*args)
            用烟雾将所有 args 打印在无人机上方的空中。此操作不受速度升级影响。
            可以一次打印多个值

        ### quick_print(*args)
            像 print(*args) 一样打印一个值，但它不会停下来将其写到空中，所以只能在输出页面上找到。

        ### range(start = 0, end, step = 1)
            生成一个数字序列，从 start 开始，在到达 end 之前结束（所以不包括 end），步长为 step。

        ### str(object)
            返回 object 的字符串表示形式。

        ### till()
            调用 till() 会将地块变成土壤。再次调用 till() 会将其变回草地。

        ### use_item(item, n=1)
            尝试使用指定的 item n 次。只能用于某些物品，包括 Items.Water、Items.Fertilizer。








        ### abs()
        ### can_harvest()
        ### can_move()
        ### change_hat()
        ### clear()
        ### dict()
        ### do_a_flip()
        ### get_companion()
        ### get_cost()
        ### get_entity_type()
        ### get_ground_type()
        ### get_pos_x()
        ### get_pos_y()
        ### get_tick_count()
        ### get_time()
        ### get_water()
        ### get_world_size()
        ### harvest()
        ### len()
        ### list()
        ### max()
        ### measure()
        ### min()
        ### move()
        ### num_items()
        ### num_unlocked()
        ### pet_the_piggy()
        ### plant()
        ### print()
        ### quick_print()
        ### random()
        ### range()
        ### set()
        ### str()
        ### swap()
        ### till()
        ### unlock()
        ### use_item()





    ## items

    ## entities

    ## land





















