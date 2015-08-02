"""
What is the starting position of the longest ORF in reading frame 3 in any of the sequences?
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
    return start_position


#  [len(i) for i in sequences]

n = 1
lengths = []
for i in sequences:
    print("["+str(n)+"]")
    orfs = find_orf_3(i)
    print(orfs)
    n += 1


