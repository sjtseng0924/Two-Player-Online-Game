import time
import socket
def get_valid_number():
    while True:
        number = input("請輸入一個四位數且每個數字不重複的目標數字：")
        if len(number) == 4 and len(set(number)) == 4 and number.isdigit():
            return number
        else:
            print("無效的輸入！請確保輸入的是四位不重複的數字。")

def calculate_AB(target, guess):
    A = sum(1 for t, g in zip(target, guess) if t == g)
    B = sum(1 for g in guess if g in target) - A
    return A, B

def number_guessing(sock: socket.socket):
    # 輸入目標數字
    target_number = get_valid_number()

    while True:
        # 先猜測對方的數字
        my_guess = input("請猜測對方的四位數字：")
        sock.send(my_guess.encode())

        # 接收對方猜測我方數字
        opponent_guess = sock.recv(1024).decode()
        time.sleep(0.25)

        # 回應對方
        A, B = calculate_AB(target_number, opponent_guess)
        if A == 4:
            response = "正確"
            sock.send(response.encode())
            print("對方猜中了你的數字，你輸了！")
            print("------------------------")
            break
        elif A == 0 and B == 0:
            response = "你的猜測什麼都沒有!"
        else:
            response = f"{A}A{B}B"
        sock.send(response.encode())

        # 接收對方對我的回應
        response = sock.recv(1024).decode()
        print(f"你猜測的結果：{response}")
        print("------------------------")

        # 猜測正確結束遊戲
        if response == "正確":
            print("你猜中了對方的數字，恭喜你獲勝！")
            print("------------------------")
            break