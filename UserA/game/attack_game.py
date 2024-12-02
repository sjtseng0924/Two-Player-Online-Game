import time
import random
import socket
def attack_game(sock: socket.socket):
    player_health = 100
    opponent_health = 100

    while player_health > 0 and opponent_health > 0:
        # 提供玩家選項
        print("選擇你的行動：")
        print("1. 攻擊敵人")
        print("2. 提升血量")
        print("3. 抽取道具並使用")
        choice = input("請輸入你選擇的編號（1-3）：")

        if choice == '1':
            # 玩家選擇攻擊
            item_chance = random.random()
            if item_chance < 0.5:
                damage = 20
            else:
                damage = 40
            message = f"ATTACK:{damage}"
            sock.send(message.encode())
            print(f"你攻擊對方 {damage} 點血量")
            opponent_health -= damage
        elif choice == '2':
            # 玩家選擇治療
            item_chance = random.random()
            if item_chance < 0.5:
                heal = 20
            else:
                heal = 40
            player_health += heal
            print(f"你恢復 {heal} 點血量")
            message = f"HEAL:{heal}"
            sock.send(message.encode())
        elif choice == '3':
            # 玩家抽取道具
            item_chance = random.random()
            if item_chance < 0.5:
                print("可惜了，你沒抽到道具")
                message = "ITEM:NONE"
            elif item_chance < 0.75:
                damage = 70
                opponent_health -= damage
                print(f"你抽到寶劍，攻擊對方造成 {damage} 點傷害")
                message = f"ITEM:ATTACK:{damage}"
            else:
                heal = 50
                player_health += heal
                print(f"你抽到大補包，恢復了 {heal} 點血量")
                message = f"ITEM:HEAL:{heal}"
            sock.send(message.encode())
        else:
            print("無效的選擇，請選擇 1 到 3")
            continue

        # 接收對方行動
        response = sock.recv(1024).decode()
        time.sleep(0.25)
        if response.startswith("ATTACK:"):
            damage = int(response.split(":")[1])
            player_health -= damage
            print(f"對方攻擊你 {damage} 點血量")
        elif response.startswith("HEAL:"):
            heal = int(response.split(":")[1])
            opponent_health += heal
            print(f"對方恢復了 {heal} 點血量")
        elif response.startswith("ITEM:ATTACK:"):
            damage = int(response.split(":")[2])
            player_health -= damage
            print(f"對方抽到寶劍對你造成 {damage} 點傷害")
        elif response.startswith("ITEM:HEAL:"):
            heal = int(response.split(":")[2])
            opponent_health += heal
            print(f"對方抽到大補包恢復了 {heal} 點血量")
        elif response == "ITEM:NONE":
            print("太棒了，對方沒抽到道具")

        # 印出當前血量
        print(f"你的血量：{player_health}")
        print(f"對方的血量：{opponent_health}")
        print("---------------")

    if player_health <= 0:
        print("你被擊敗了！")
    elif opponent_health <= 0:
        print("你擊敗了對方！")