import os


def combet(typ1, typ2, path):
    files = list()

    for m in os.walk(path):
        files += [x for x in m[2]]
        sajjad_ext = list(filter(lambda x: x.endswith(typ2), files))
        salib_ext = list(filter(lambda x: x.endswith(typ1), files))

    if len(sajjad_ext) > len(salib_ext):
        return 'Win! Normally!'

    names = list(map(lambda a: a.split(".")[0],
                     filter(lambda x: not x.endswith(typ1) and not x.endswith(typ2), files)))
    for i in names:
        if names.count(i) > (len(salib_ext) - len(sajjad_ext)):
            return f"Win! you can win if you cheat on '{i}'!"

    K = list(map(lambda a: a.split(".")[0],
                 filter(lambda x: x.endswith(typ1), files)))
    for i in K:
        if 2 * K.count(i) > (len(salib_ext) - len(sajjad_ext)):
            return (f"Win! you can win if you cheat on '{i}'!")
    return "Lose! you can't win this game!"
