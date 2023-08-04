from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt

protein_sequence = "*" 

# * insert your protein here, or, you load your FASTA file
# such as :
# protein_sequence = SeqIO.read("your_file.fasta", fasta).seq

protein_analysis = ProteinAnalysis(protein_sequence)

sequence_lenght = len(protein_sequence)
print(f"length of the sequence : {sequence_lenght} Aminno Acid")

molecular_weight_kda = protein_analysis.molecular_weight() / 1000
print(f"molecular weight : {molecular_weight_kda:.2f} kDa")

pI = protein_analysis.isoelectric_point()
print(f"isolectric point (pI) : {pI:.2f}")

percentage_aa = protein_analysis.get_amino_acids_percent()
print(f"percentage of amino acids in the sequence : ")
for aa, percentage in percentage_aa.items():
    print(f"{aa}: {percentage:.2f}%")

plt.bar(percentage_aa.keys(), percentage_aa.values())
plt.xlabel("Amino Acid")
plt.ylabel("(%)")
plt.title("Quantity of amino acid in the protein")
plt.show()
