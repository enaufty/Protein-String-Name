codon_table = {
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",               # Ala
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",  # Arg
    "AAU": "N", "AAC": "N",                                      # Asn
    "GAU": "D", "GAC": "D",                                      # Asp
    "UGU": "C", "UGC": "C",                                      # Cys
    "CAA": "Q", "CAG": "Q",                                      # Gln
    "GAA": "E", "GAG": "E",                                      # Glu
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",              # Gly
    "CAU": "H", "CAC": "H",                                      # His
    "AUU": "I", "AUC": "I", "AUA": "I",                          # Ile
    "AUG": "M",                                                  # Met (Start)
    "UUU": "F", "UUC": "F",                                      # Phe
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",              # Pro
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",  # Ser
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",              # Thr
    "UGG": "W",                                                  # Trp
    "UAU": "Y", "UAC": "Y",                                      # Tyr
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V"}              # Val
stop = {"UAA": "Stop", "UAG": "Stop", "UGA": "Stop"}
codon_table.update(stop)

sequence = "CAUGUUACUCCUAUGGAAAUUUCUUUUCGUGAAGCUCAAUAUGCUUCUUUUUCUGCUUGGUGGUAUUAA"
start_index = sequence.find("AUG")
i = start_index
protein = ""
while i < len(sequence):
    codon = sequence[i:i + 3]
    aa = codon_table.get(codon, None)
    if aa is None:
        print("Unknown:", codon)
        break
    if aa == "Stop":
        break
    protein += aa
    i += 3
print(f"Your protein is: {protein}")
