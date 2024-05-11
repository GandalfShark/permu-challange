"""
rules of challenge:
pick 3 numbers digits 1 -7
they represent police, fire department, and sanitation
all numbers must be different
the total of the 3 numbers must = 12
police number must be even
"""
valid_total = 12
# the total of the nums must = 12

possible_combinations = [n for n in range(111, 888)]
invalid_options = []


for combo in possible_combinations:
    # check the validity with a set of rules
    if int(str(combo)[0]) + int(str(combo)[1]) + int(str(combo)[2]) != valid_total:
        invalid_options.append(combo)

    if int(str(combo)[0]) % 2 != 0:
        invalid_options.append(combo)
        # police is first so must be even

    if int(str(combo)[0]) == int(str(combo)[1]) or int(str(combo)[0]) == int(str(combo)[2]):
        invalid_options.append(combo)

    if int(str(combo)[1]) == int(str(combo)[2]):
        invalid_options.append(combo)

    if '8' in str(combo):
        invalid_options.append(combo)


for bad in invalid_options:
    try:
        possible_combinations.remove(bad)
    except ValueError:
        continue

print("Possible permutations for Police, Fire, Sanitation")
print(possible_combinations)
