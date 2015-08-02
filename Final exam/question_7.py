"""
What is the length of the longest ORF that appears in the sequence with the identifier gi|142022655|gb|EQ086233.1|97?
"""

f = open("dna1.fasta", "r")
file = f.readlines()

# Find the sequence with the identifier gi|142022655|gb|EQ086233.1|97
seq = ""
identifier = 0
for i in range(0, len(file)):
    if "gi|142022655|gb|EQ086233.1|97" in file[i]:
        identifier = i

for f in file[identifier+1:]:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        break


# Find orf 1
def find_orf_1(sequence):
    # Find all ATG indexs
    start_position = 0
    start_indexs = []
    stop_indexs = []
    for i in range(0, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(0, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

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
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

# Find orf 3
def find_orf_3(sequence):
    # Find all ATG indexs
    start_position = 2
    start_indexs = []
    stop_indexs = []
    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(2, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf



lengths = []
orfs = find_orf_1(seq) + find_orf_2(seq) + find_orf_3(seq)
for j in orfs:
    lengths.append(len(j))

print(max(lengths))


