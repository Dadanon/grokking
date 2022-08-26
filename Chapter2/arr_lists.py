import string

letters = [letter for letter in string.ascii_uppercase]

people_content = [[letter for a in range(10)] for letter in letters]

print(people_content[2])
people_content[2][3] = "Civilla"
print(people_content[2])

print(sum(a for a in range(1, 12)))
