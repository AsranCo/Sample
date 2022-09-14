##بمب بازی
def creat_game(m, k, b):
    map = []
    for x in range(m):
        map.append([])
        for y in range(k):
            map[x].append(0)
    for l in b:
        map[l[0] - 1][l[1] - 1] = "*"
    return map


def show_game(cre):
    for row in cre:
        show = ""
        for col in row:
            show += str(col) + " "
        print(show)


def calc_mine(m, k, map_game):
    for i in range(m):
        for j in range(k):
            if map_game[i][j] == 0:
                count_bomb = 0
                try:
                    if map_game[i][j - 1] == "*" and j != 0: count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i + 1][j - 1] == "*" and not j == 0: count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i + 1][j + 1] == "*": count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i][j + 1] == "*": count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i - 1][j] == "*" and not i == 0: count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i + 1][j] == "*": count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i - 1][j - 1] == "*" and j != 0 and i != 0: count_bomb += 1
                except:
                    pass
                try:
                    if map_game[i - 1][j + 1] == "*" and not i == 0: count_bomb += 1
                except:
                    pass
                map_game[i][j] = count_bomb
    return map_game


m, k = map(int, input().split())
b = int(input())
mine_list = []
for i in range(b):
    row, col = map(int, input().split())
    mine_list.append([row, col])
map_game = creat_game(m, k, mine_list)
final_game = calc_mine(m, k, map_game)
show_game(final_game)

# 4 3
# 5
# 1 1
# 1 3
# 3 2
# 4 2
# 4 3
