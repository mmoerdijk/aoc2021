# load data
import copy
# number of digits -> number
mapping = {2: 1, 3: 7, 4: 4, 7: 8}
"""
Segment numbers:
 66
5  1
5  1
 77
4  2
4  2
 33
"""
segments_to_value_map = {
    "123456": 0,
    "12": 1,
    "13467": 2,
    "12367": 3,
    "1257": 4,
    "23567": 5,
    "234567": 6,
    "126": 7,
    "1234567": 8,
    "123567": 9,
}

input_file = open("input.txt")

lines = []
count = [0] * 9
sum_output = 0
for line in input_file.readlines():
    # Parse input and output of lin
    input, output = line.split("|")
    input = input.strip().split(" ")
    output = output.strip().split(" ")

    # Question 1
    for ans in output:
        length = len(ans)
        # if the length is unique use it
        if length in mapping:
            count[mapping[length]] += 1

    # Question 2
    number_to_letter_mapping = [set()] * 9
    len_set = [[] for _ in range(9)]
    # make sets of all inputs and group them per length
    for ans in input:
        length = len(ans)
        len_set[length].append(set([a for a in ans]))
        # if the length is unique use it
        if length in mapping:
            number_to_letter_mapping[mapping[length]] = number_to_letter_mapping[mapping[length]].union(set([a for a in ans]))

    # Find all the segments for the letters
    segment_letter_mapping = {}
    # find segment 0
    segment_letter_mapping[6] = number_to_letter_mapping[7] - number_to_letter_mapping[1]
    # find number segment 4 only used by 2
    unique_segments = [s - number_to_letter_mapping[7] - number_to_letter_mapping[4] for s in len_set[5]]
    unique_segments_lengths_idx = [len(i) for i in unique_segments].index(2)
    segment_letter_mapping[4] = copy.deepcopy(unique_segments[unique_segments_lengths_idx])
    for idx, i in enumerate(len_set[5]):
        if len(unique_segments[idx]) != 2:
            segment_letter_mapping[4] -= i
    # find segment 3
    segment_letter_mapping[3] = unique_segments[unique_segments_lengths_idx] - segment_letter_mapping[4]
    # find segment 7
    segment_letter_mapping[7] = (
            copy.deepcopy(len_set[5][unique_segments_lengths_idx])
            - number_to_letter_mapping[7]
            - segment_letter_mapping[3]
            - segment_letter_mapping[4]
    )
    # find the other segments
    segment_letter_mapping[2] = number_to_letter_mapping[1] - len_set[5][unique_segments_lengths_idx]
    segment_letter_mapping[1] = number_to_letter_mapping[1] - segment_letter_mapping[2]
    segment_letter_mapping[5] = number_to_letter_mapping[4] - number_to_letter_mapping[7] - segment_letter_mapping[7]
    # Reverse the mapping
    letter_segment_mapping = {list(v)[0]: k for k, v in segment_letter_mapping.items()}
    # find the seperate numbers
    answer_components = []
    for ans in output:
        ans_in_segments = "".join(sorted([str(letter_segment_mapping[a]) for a in ans]))
        answer_components.append(segments_to_value_map[ans_in_segments])
    # and convert it to the output value
    sum_output += sum([10**n * d for n,d in enumerate(answer_components[::-1])])

print(f"Answer 1: {sum(count)}")
print(f"Answer 2: {sum_output}")

