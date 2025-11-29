def create_codon_dict(file_path):
    pass # Replace the pass with your code


dict = {}
split_row = []
for row in rows:
  split_row = row.strip().split('\t')
  codon = split_row[0]
  amino_acid = split_row[2]
  dict[codon] = amino_acid
  
print(dict)
