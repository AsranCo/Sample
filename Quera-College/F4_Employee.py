##کارمند زیادی
count_person = int(input())
name_dict = {}

for i in range(count_person):
    name, family = map(str, input().split())
    count_name = 1
    if name in name_dict:
        count_name = name_dict[name] + 1

    name_dict[name] = count_name
print(max(name_dict.values()))
