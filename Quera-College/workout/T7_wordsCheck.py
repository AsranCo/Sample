import re


def words_check(text):
    result_dict = {}
    for f in (text.split()):

        x = re.sub('[^a-zA-Z0-9 \n.]', '', f).title()
        # print(x, f)
        # print(len(x) * 2 ,len(f) ,len(x))
        count = 1
        if len(x) == len(f) or len(x) * 2 > len(f):
            if x in result_dict:
                count = result_dict[x] + 1
            result_dict[x] = count
    result_dict= {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[0])}
    return (result_dict)


# print(words_check("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
print(words_check("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))

{'A': 2, 'For': 1, 'Friends': 1, 'Hello': 1, 'Is': 1, 'My': 1, 'Test': 1, 'This': 1, 'Your': 1}
{'A': 2, 'For': 1, 'Friends': 1, 'Hello': 1, 'Is': 1, 'My': 1, 'Test': 1, 'This': 1, 'Your': 1}
