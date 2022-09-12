##سوال کد پایتون
import re


def solve(path):
    lines = []
    count = 0

    with open(path, "r") as f:  # after read file -> close file!
        while True:
            line = f.readline()
            if line == '':
                break  # end of file
            if line.strip("\n"):
                lines.append(line)

    for line in lines:
        line = line.strip()
        line = re.sub(r"^\s+|\s+$", "", line)
        if not line.startswith("#"):
            count += 1
        print(line)
    return count


print(solve("./text.info"))
