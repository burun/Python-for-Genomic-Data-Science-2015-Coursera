"""
How many records are in the file?
"""

f = open("dna1.fasta", "r")
file = f.read()
print(file.count('>'))
