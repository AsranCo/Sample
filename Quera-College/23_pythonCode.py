##سوال کد پایتون
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
        if not line.startswith("#"):
            count += 1
    return count


print(solve("Quera-College/text.info"))
