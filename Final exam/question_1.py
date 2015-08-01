"""
How many records are in the file?
"""

f = open("dna.example.fasta", "r")
all = f.read()
print(all.count('>'))
