def create_codon_dict(file_path):
  file = open(file_path, "r")
  rows = file.readlines()
  file.close()

  codons_and_amino_dict = {}
  split_row = []
  for row in rows:
    split_row = row.strip().split('\t')
    codon = split_row[0]
    amino_acid = split_row[2]
    codons_and_amino_dict[codon] = amino_acid

  return codons_and_amino_dict
