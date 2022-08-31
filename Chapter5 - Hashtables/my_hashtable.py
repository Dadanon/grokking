keys = []
values = []

table = []


def add_to_table(key, value):
    keys.append(key)
    values.append(value)
    table.append([key, value])


add_to_table("milk", 15)
print(table)


