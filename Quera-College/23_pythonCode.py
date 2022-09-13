##سوال کد پایتون
import re

def solve(path):
    count = 0
    with open(path, "r") as f:  # after read file -> close file!
        for line in f:
            line = line.strip()
            if re.match('^#', line) or re.match(r'^\s*$', line):
                pass
            else:
                count += 1
    return count


print(solve("./text.info"))

# ------------------------------------------ todo پاسخ دیگران


# def solve(path):
#     counter = 0
#     with open(path) as f_in:
#         lines = [line.strip() for line in f_in if line.strip()]
#         for line in lines:
#             if not line.startswith("#"):
#                 counter +=1
#
#
#     return counter

