import math

err_score_mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
closing_err_score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
close_to_open_map = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

open_to_close_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

input_file = open("input.txt")
all_input = []
syntax_error = []
scores = []
for line in input_file.readlines():

    open_chars = []
    close_chars = []
    found = False
    for char in line[:-1]:

        if char in ["(", "[", "{", "<"]:
            open_chars.append(char)

        if char in [")", "]", "}", ">"]:
            close_chars.append(char)
            # closing while not open
            if close_to_open_map[char] not in open_chars:
                syntax_error.append(char)
                found = True
                break

            idx = open_chars[::-1].index(close_to_open_map[char])
            # Not closing the right on
            if open_chars[-1] != close_to_open_map[char]:
                syntax_error.append(char)
                found = True
                break

            # if ok remove char from open chars
            del open_chars[len(open_chars) - idx - 1]

    # if not complete make complete
    if not found:
        tmp_score = 0
        for o in open_chars[::-1]:
            tmp_score *= 5
            tmp_score += closing_err_score_map[open_to_close_map[o]]
        scores.append(tmp_score)


print(f"Answer 1: {sum([err_score_mapping[e] for e in syntax_error])}")
print(f"Answer 2: {sorted(scores)[math.floor(len(scores) / 2)]}")
