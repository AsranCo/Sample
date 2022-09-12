##ستون CSV

def csv_reader(path):
    import csv
    rows = []
    with open(path, "r+") as file, open("ans.csv", 'w') as writeFile:
        write = csv.writer(writeFile)
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

        for f in rows:
            b = 0
            for i in f:
                b = int(i) + b
            f.append(b)
            write.writerow(f)


# todo: پاسخ دیگران
# def csv_reader(path):
#     with open(path) as csv:
#         for row in csv.readlines():
#             yield row.rstrip()
#
# def process(path):
#     with open('ans.csv', 'w') as out:
#         for line in csv_reader(path):
#             ssum = sum(list(map(int, line.split(','))))
#             line = line + ',' + str(ssum)
#             out.write(line + '\n')
# -------------------------------------------------
# def process(path):
#     with open('ans.csv', 'w') as ans, open(path, 'r') as csv:
#         for line in csv.readlines():
#             row = list(map(int, line.split(',')))
#             r_sum = sum(row)
#             row.append(r_sum)
#             a_line = ",".join(list(map(str, row)))
#             ans.write(a_line + '\n')


csv_reader("./file.csv")
