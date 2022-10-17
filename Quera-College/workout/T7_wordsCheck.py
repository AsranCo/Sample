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
    result_dict = {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[0])}
    return (result_dict)


# ----------------------------------------------------------------
# from collections import defaultdict
#
# def check_good_word(word):
#     good_word = list(filter(lambda letter: letter.isalpha(), word))
#     return "".join(good_word).capitalize() if len(good_word) > len(word) / 2 else ""
#
# def words_check(text):
#     result = defaultdict(int)
#     for word in text.split():
#         if good_word:=check_good_word(word):
#             result[good_word] += 1
#     return dict(sorted(result.items(), key=lambda item: item[0]))


print(words_check("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
