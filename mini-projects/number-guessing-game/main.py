import random

# 컴퓨터가 1부터 100 사이의 숫자를 하나 정합니다.
answer = random.randint(1, 100)

# 사용자가 몇 번 시도했는지 저장할 변수입니다.
attempts = 0

print("1부터 100 사이의 숫자를 맞혀보세요!")

while True:
    # 사용자의 입력을 받습니다.
    user_input = input("숫자를 입력하세요: ").strip()

    # 빈칸이나 숫자가 아닌 값이면 다시 입력받습니다.
    try:
        guess = int(user_input)
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue

    # 범위를 벗어난 숫자면 다시 입력받습니다.
    if guess < 1 or guess > 100:
        print("1부터 100 사이의 숫자를 입력해주세요.")
        continue

    # 입력이 정상적인 경우에만 시도 횟수를 늘립니다.
    attempts += 1

    # 정답과 비교합니다.
    if guess < answer:
        print("Up!")
    elif guess > answer:
        print("Down!")
    else:
        print(f"정답입니다! 총 {attempts}번 만에 맞혔어요.")
        break
