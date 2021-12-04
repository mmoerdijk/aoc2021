input = open("input.txt").readlines()
diag = [[int(i) for i in l[:-1]] for l in input]
num_items = len(diag)
gamma_rate = int("".join(["1" if sum(l[i] for l in diag) >= num_items / 2 else "0" for i in range(len(diag[0]))]), 2)
epsilon_rate = int("".join(["0" if sum(l[i] for l in diag) >= num_items / 2 else "1" for i in range(len(diag[0]))]), 2)
print(f"Answer 1 : {gamma_rate * epsilon_rate}")


diag_oxy = diag
for i in range(len(diag[0])):
    most_common_bit = [1 if sum(l[i] for l in diag_oxy) >= len(diag_oxy) / 2 else 0 for i in range(len(diag[0]))][i]
    diag_oxy = [l for l in diag_oxy if l[i] == most_common_bit]
    if len(diag_oxy) == 1:
        break
oxy = int("".join([str(i) for i in diag_oxy[0]]), 2)

diag_co2 = diag
for i in range(len(diag[0])):
    most_common_bit = [1 if sum(l[i] for l in diag_co2) >= len(diag_co2) / 2 else 0 for i in range(len(diag[0]))][i]
    diag_co2 = [l for l in diag_co2 if l[i] != most_common_bit]
    if len(diag_co2) == 1:
        break

co2 = int("".join([str(i) for i in diag_co2[0]]), 2)

print(f"Answer 2 : {oxy * co2}")
