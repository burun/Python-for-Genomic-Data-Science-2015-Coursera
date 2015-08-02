"""
Find the most frequently occurring repeat of length 6 in all sequences. How many times does it occur in all?
"""

f = open("dna1.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    length = len(sequence)
    repeats = []
    for i in range(length):
        repeats.append(sequence[i:i + 6])
    return repeats

all_six_repearts = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        all_six_repearts.append(j)

def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(all_six_repearts))
print(all_six_repearts.count(most_common(all_six_repearts)))
