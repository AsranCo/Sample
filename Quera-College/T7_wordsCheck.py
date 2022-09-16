import re


def words_check(text):
    result_dict = {}
    for f in (text.split()):
        x = re.sub('[^a-zA-Z0-9 \n.]', '', f).title()
        count = 1
        if len(x) == len(f) or len(x) * 2 > len(f):
            if x in result_dict:
                count = result_dict[x] + 1
            result_dict[x] = count

    return (result_dict)


# print(words_check("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
print(words_check("hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a A!A Abc!!!"))
