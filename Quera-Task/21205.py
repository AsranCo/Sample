def check_registration_rules(**register):
    dic = []

    for name, password in register.items():
        if len(password) >= 6 and len(name) >= 4 and name != "quera" and name != "codecup" and not str(
                password).isnumeric():
            dic.append(name)

    return dic
