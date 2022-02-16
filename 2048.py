import random


print("\nMerhaba! Python İle Yaptığım 2048 Oyununa Hoşgeldin.")
print("Nasıl Oynayacağını Sana Oyun İçinde Anlattım. İyi Oyunlar.\n")

# Create the game grid
# The game should work for square grid of any size though
grid = [['.', '2', '.', '.'],
        ['.', '4', '.', '2'],
        ['.', '.', '.', '.'],
        ['2', '.', '2', '4']]

direction = {'L': 0, 'B': 1, 'R': 2, 'T': 3, 'X': 4}


print("\n")
for i in range(len(grid)):
    res = "\t\t"
    for j in range(len(grid[i])):
        for _ in range(5 - len(grid[i][j])): res += " "
        res += grid[i][j] + " "
    print(res)
    print("\n")

loseStatus = 0
totalScore = 0 # Score of the user
while True:
    tmp = input("\nSol için L'ye, sağ için R'ye, üst için T'ye, alt için B'ye Basın.\n X'e Basarak Oyunu Bitirebilirsin.\n")
    if tmp in ["R", "r", "L", "l", "T", "t", "B", "b", "X", "x"]:
        dir = direction[tmp.upper()]
        if dir == 4:
            print("\nFinal Skoru: " + str(totalScore))
            break
        else:
            for i in range(dir): grid = list(map(list, zip(*grid[::-1])))
            for i in range(len(grid)):
                temp = []
                for j in grid[i]:
                    if j != '.':
                        temp.append(j)
                temp += ['.'] * grid[i].count('.')
                for j in range(len(temp) - 1):
                    if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.':
                        temp[j] = str(2 * int(temp[j]))
                        totalScore += int(temp[j])
                        temp[j + 1] = '.'
                grid[i] = []
                for j in temp:
                    if j != '.':
                        grid[i].append(j)
                grid[i] += ['.'] * temp.count('.')
            for i in range(4 - dir): grid = list(map(list, zip(*grid[::-1])))

            num = random.randint(1, 2) * 2
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            loseStatus = 0
            isFound = False
            if grid[x][y] != '.':
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j] == '.':
                            x = i
                            y = j
                            loseStatus = 0
                            isFound = True
                if not isFound:
                    x = -1
                    y = -1
                    loseStatus = 1

            if not loseStatus: grid[x][y] = str(num)

            print("\n")
            for i in range(len(grid)):
                res = "\t\t"
                for j in range(len(grid[i])):
                    for _ in range(5 - len(grid[i][j])): res += " "
                    res += grid[i][j] + " "
                print(res)
                print("\n")

            if loseStatus:
                print("\nOyun Bitti!")
                print("Final Skoru: " + str(totalScore))
                break
            print("\nŞuanki skor: " + str(totalScore))
    else:
        print("\nNe Yapmaya Çalışıyorsun Dostum!? Bu Tuşları Kullanman Lazım (L, R, T, B).")
