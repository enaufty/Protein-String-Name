codon_table = {
    # Alanine
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Arginine
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    # Asparagine
    "AAU": "N", "AAC": "N",
    # Aspartic acid
    "GAU": "D", "GAC": "D",
    # Cysteine
    "UGU": "C", "UGC": "C",
    # Glutamine
    "CAA": "Q", "CAG": "Q",
    # Glutamic acid
    "GAA": "E", "GAG": "E",
    # Glycine
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    # Histidine
    "CAU": "H", "CAC": "H",
    # Isoleucine
    "AUU": "I", "AUC": "I", "AUA": "I",
    # Leucine
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    # Lysine
    "AAA": "K", "AAG": "K",
    # Methionine (Start)
    "AUG": "M",
    # Phenylalanine
    "UUU": "F", "UUC": "F",
    # Proline
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Serine
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    # Threonine
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    # Tryptophan
    "UGG": "W",
    # Tyrosine
    "UAU": "Y", "UAC": "Y",
    # Valine
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V"
}
stop = {"UAA": "Stop", "UAG": "Stop", "UGA": "Stop"}
codon_table.update(stop)


sequence = "GUUUAUUGGAUGGAAAUUUCUUUUCGUGAAGCUCAAUAUGCUUCUUUUUCUGCUUGGUGGUAUUAA"
start_index = sequence.find("AUG")
i = start_index
protein = ""
while i < len(sequence):
    codon = sequence[i:i + 3]
    aa = codon_table.get(codon, None)
    if len(codon) < 3:
        break
    if aa is None:
        print("Unknown:", codon)
        break
    if aa == "Stop":
        break
    protein += aa
    i += 3
print(f"Your protein is: {protein}")

