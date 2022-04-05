import numpy as np

std_arr = np.array([])
num_arr = np.array([])
done = False

while not done:
    try:
        a, b = input("이름 번호 : ").split()
        if int(b) < 100 or int(b) > 999:
            print("숫자는 100~999 범위입니다")
            continue
        std_arr = np.append(std_arr, [a])
        num_arr = np.append(num_arr, [int(b)])
    except ValueError:
        done = True

print("====================================================================")
print(std_arr)
print(num_arr)
print("====================================================================")

prof_num = int(input())

arr = abs(num_arr - prof_num)

winner = std_arr[np.argmin(arr)]
loser = std_arr[np.argmax(arr)]

print("우승자 : ", winner)
print("꼴지 : ", loser)
