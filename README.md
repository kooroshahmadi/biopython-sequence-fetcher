#### Project Overview:

**DNA Sequence Viewer**

This project consists of two Python scripts that work together to create a simple application for fetching and displaying information about DNA sequences from the NCBI database (GenBank).

#### Files:

- **gui.py**: Contains the Tkinter GUI application (`DNASequenceViewerApp`) that allows users to enter a GenBank accession number and fetch corresponding DNA sequence information.
- **fetch_sequence.py**: Defines a function (`fetch_dna_sequence`) that uses Biopython's `Entrez` module to fetch DNA sequences from the NCBI database based on the provided accession number.

#### How to Use:

1. **Setup**:
   - Ensure Python 3.x is installed on your system.
   - Install necessary libraries:
     ```bash
     pip install biopython
     ```

2. **Running the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `gui.py` and `fetch_sequence.py`.
   - Run the application:
     ```bash
     python gui.py
     ```
   - The GUI window will appear. Enter a valid GenBank accession number in the entry field and click "Fetch Sequence". Information about the DNA sequence (length and GC content) will be displayed.

3. **Notes**:
   - **Accession Number**: Ensure you have a valid GenBank accession number to fetch the corresponding DNA sequence.
   - **Email Address**: Update the `fetch_dna_sequence` script with your email address for NCBI Entrez (`Entrez.email`).

#### Example:

- Enter accession number `NC_000913` (for Escherichia coli K-12 MG1655 genome).
- Click "Fetch Sequence".
- Information displayed: Accession Number, Sequence Length (in base pairs), and GC Content (%).

### Conclusion:

This README file provides an overview of the project, explains how to use the provided scripts, and includes an example to demonstrate their functionality. Adjust the instructions and examples as needed based on your specific use case or additional features you may implement.
