from Bio import SeqIO
from Bio import Entrez

def fetch_dna_sequence(accession_number):
    """
    Fetches a DNA sequence from NCBI GenBank database using Biopython's Entrez module.

    Parameters:
    - accession_number (str): Accession number of the DNA sequence.

    Returns:
    - str: DNA sequence as a string.
    """
    Entrez.email = "kooroshahmadi1379@gmail.com"  # Provide your email address
    handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return str(record.seq)  # Return DNA sequence as a string
