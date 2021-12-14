from collections import Counter

# Load data
input_file = open("input.txt")
poly, openration_raw = input_file.read().split("==")

poly = [c for c in poly if c not in ["", "\n"]]
pairs = {}
for i in range(len(poly) - 1):

    if f"{poly[i]}{poly[i+1]}" not in pairs:
        pairs[f"{poly[i]}{poly[i + 1]}"] = 0

    pairs[f"{poly[i]}{poly[i+1]}"] += 1

letters = Counter(poly)

op = []
for o in openration_raw.split("\n"):
    if o not in ["", "\n"]:
        op += [o.split(" -> ")]


def apply_operations(n_steps):

    for step in range(n_steps):
        additions = []
        for o in op:
            if o[0] in pairs and pairs[o[0]] > 0:
                additions += [(o, pairs[o[0]])]
                if o[1] not in letters:
                    letters[o[1]] = 0
                letters[o[1]] += pairs[o[0]]

        # make new pairs
        for a, number in additions:
            # remove one pair as we split it up
            pairs[a[0]] = max(pairs[a[0]] - number, 0)
            new_pairs = [f"{a[0][0]}{a[1]}", f"{a[1]}{a[0][1]}"]
            for new in new_pairs:
                if new not in pairs:
                    pairs[new] = 0
                pairs[new] += number

    return max(letters.values()) - min(letters.values())


print(f"Answer 1: {apply_operations(10)} ")
print(f"Answer 2: {apply_operations(30)} ")

# Answer 1: 2851
# Answer 2: 10002813279337

