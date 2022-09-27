import csv


def ready_up():
    import csv
    rows = []
    path = "../file/esm_famil_data.csv"
    with open(path, "r+") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

    print(rows)


def add_participant(participant, answers):
    pass


def calculate_all():
    pass
