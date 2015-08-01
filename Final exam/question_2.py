"""
What are the lengths of the sequences in the file? What is the longest sequence and what is the shortest sequence?
"""

f = open("dna1.fasta", "r")
file = f.readlines()

seq_lengths = []
length = 0
for f in file:
    if not f.startswith('>'):
        length = length + len(f.replace(" ", ""))
    else:
        seq_lengths.append(length)
        length=0

# Add the last seq
seq_lengths.append(length)

seq_lengths = seq_lengths[1:]

print(seq_lengths, max(seq_lengths), min(seq_lengths))



