"""
What are the lengths of the sequences in the file? What is the longest sequence and what is the shortest sequence?
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

lengths = [len(i) for i in sequences]

print(max(lengths), min(lengths))



