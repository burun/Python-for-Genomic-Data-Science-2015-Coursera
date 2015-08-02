"""
what is the length of the longest ORF in the file?
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

# Find orf 2
def find_orf_2(sequence):
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                mark = stop_indexs[j]+3
                break
    return orf


#  [len(i) for i in sequences]

n = 1
lengths = []
for i in sequences:
    orfs = find_orf_2(i)
    for j in orfs:
        lengths.append(len(j))

# orf_lengths = [len(i) for i in orf_2 if i]
print(max(lengths))

