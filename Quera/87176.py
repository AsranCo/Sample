################################
# from source import game
###############################
def game(number):
    x = []
    for f in str(number):
        x.append(f)
    x.sort()
    return (int(x[-1]) - int(x[0]))


print(game(input()))
