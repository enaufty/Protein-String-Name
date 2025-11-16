# RNA to Protein Translator

This Python script translates an RNA sequence into its corresponding protein sequence using the standard codon table. It handles start codons, stop codons, and unknown codons gracefully.  

## Features
- Converts an RNA sequence (string of `A`, `U`, `C`, `G`) to a protein sequence (single-letter amino acid codes).  
- Recognizes the start codon `AUG` as the beginning of translation.  
- Stops translation when a stop codon (`UAA`, `UAG`, `UGA`) is encountered.  
- Detects and reports unknown codons.  

## How It Works
1. A codon table dictionary (`codon_table`) maps RNA triplets (codons) to their corresponding amino acids (single-letter codes).  
2. Stop codons are stored in a separate dictionary (`stop`) and merged with the main codon table.  
3. The RNA sequence `s` is read in chunks of 3 nucleotides.  
4. Each codon is translated to its amino acid.  
5. Translation continues until a stop codon is reached or an unknown codon is found.  
6. The resulting protein sequence is printed.
