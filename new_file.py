
#function for reverse list of nucleatides
def reverse(s):
    return (s[::-1])
  
# funcion for to print out the complemets of the nucleotides of the sequence
def complement(s):
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'M': 'K', 'K': 'M', 'R': 'Y', 'Y': 'R', 'W': 'W', 'S': 'S', 'V': 'B', 'B': 'V', 'H': 'D', 'D': 'H', 'N': 'N', '-': '-' }
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)
  

def revcom(s):
  """ function for returnng the reverse complement of the sequences."""
    return complement(s[::-1])
  
  
reverse(basecomplement)
