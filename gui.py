import tkinter as tk
from tkinter import messagebox
from fetch_sequence import fetch_dna_sequence  # Import function to fetch DNA sequence
from Bio.SeqUtils import gc_fraction  # Import GC content calculation from Biopython

class DNASequenceViewerApp:
    def __init__(self, root):
        """
        Initialize the DNA Sequence Viewer application.

        Parameters:
        - root (tk.Tk): Root window of the application.
        """
        self.root = root
        self.root.title("DNA Sequence Viewer")  # Set window title
        self.root.geometry("300x300")  # Set window size

        # Entry widget for accession number input
        self.accession_entry = tk.Entry(root, width=20)
        self.accession_entry.pack(pady=20)

        # Button to fetch sequence
        self.fetch_button = tk.Button(root, text="Fetch Sequence", command=self.fetch_sequence)
        self.fetch_button.pack()

        # Label to display sequence information
        self.info_label = tk.Label(root, text="", wraplength=300)
        self.info_label.pack(pady=20)

    def fetch_sequence(self):
        """
        Fetches a DNA sequence from NCBI based on the accession number entered by the user.
        """
        accession_number = self.accession_entry.get().strip()
        if accession_number:
            try:
                sequence = fetch_dna_sequence(accession_number)  # Fetch DNA sequence
                length = len(sequence)
                gc_content = gc-fraction(sequence)  # Calculate GC content
                message = f"Accession Number: {accession_number}\nLength: {length} bp\nGC Content: {gc_content:.2f}%"
                self.info_label.config(text=message)  # Display sequence information
            except Exception as e:
                messagebox.showerror("Error", str(e))  # Display error message
        else:
            messagebox.showwarning("Warning", "Please enter an accession number.")  # Prompt for accession number

if __name__ == "__main__":
    root = tk.Tk()  # Create Tkinter root window
    app = DNASequenceViewerApp(root)  # Initialize DNASequenceViewerApp
    root.mainloop()  # Start Tkinter event loop
