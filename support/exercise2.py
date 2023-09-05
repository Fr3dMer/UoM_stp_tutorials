"""************************************************************************************************
File          : exercise2.py
About         : Funcs to solve second set of exercises
Author        : Freddie Mercer
*************************************************************************************************"""

import re

class exercise2:
    def __init__(self,args):
        # Defensive clean and spliting of args
        clean_args = re.sub('[ \t\n\r]',"",args)    
        clean_args = clean_args.lower()
        self.clean_args = clean_args.split(',')
        
        # Usefull var
        self.ex2_1 = "ex2.1"
        self.ex2_2 = "ex2.2"
        self.ex2_3 = "ex2.3"
        self.ex2_4 = "ex2.4"
        self.ex2_5 = "ex2.5"
        self.ex2_6 = "ex2.6"
        
        
        
        # Conditions for each problem:
        self.ex2_1_dna_sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"

        self.ex2_2_sequence = "AGGAGTAAGCCCTTGCAACTGGAAATACACCCATTG"
        
        self.ex2_3_sequence = "aggagtaagcccttgcaactggaaatacacccattg"
        
        self.ex2_4_sequence = "aggagtaagcccttgcaactggaaatacacccattg"
        
        self.ex2_5_sequence = "aggagtaagcccttgcaactggaaatacacccattg"
        
        self.ex2_6_sequence = "aggagtaagcccttgcaactggaaatacacccattg"
        
    def execute(self,logger):
        if (self.ex2_1 in self.clean_args):
            output = self.format_genbank(self.ex2_1_dna_sequence)
            message = self.ex2_1 + " Answer: " + str(output)
            logger.log(message)
        
        if (self.ex2_2 in self.clean_args):
            output = self.translate_dna_to_amino_acids(self.ex2_2_sequence)
            message = self.ex2_2 + " Answer: " + str(output)
            logger.log(message)
        
        if (self.ex2_3 in self.clean_args):
            output = self.reverse_complement(self.ex2_3_sequence)
            message = self.ex2_3 + " Answer: " + str(output)
            logger.log(message)
        
        if (self.ex2_4 in self.clean_args):
            output = self.translation_reversal(self.ex2_4_sequence)
            message = self.ex2_4 + " Answer: " + str(output)
            logger.log(message)
        
        if (self.ex2_5 in self.clean_args):
            output = self.count_nucleotides(self.ex2_5_sequence)
            message = self.ex2_5 + " Answer: " + str(output)
            logger.log(message)
            
        if (self.ex2_6 in self.clean_args):
            output = self.calculate_gc_content(self.ex2_6_sequence)
            message = self.ex2_6 + " Answer: " + str(output)
            logger.log(message)
            

    # Solving the actual problems themselves 
    def format_genbank(self,dna_sequence, accession_number=None, source=None, organism=None, description=None):
        genbank_format = f"\nLOCUS       {accession_number}  {len(dna_sequence)} bp\n"
    

        dna_sequence = dna_sequence.lower()

    
        if description:
            genbank_format += f"DEFINITION  {description}\n"
    
        if source:
            genbank_format += f"SOURCE      {source}\n"
    
        if organism:
            genbank_format += f"  ORGANISM  {organism}\n"
    
        # Add features and sequence data sections if needed (not implemented in this example).
    
        genbank_format += f"ORIGIN\n"
        
    
        # Split the DNA sequence into lines of 60 characters each, as per GenBank format.
        for i in range(0, len(dna_sequence), 60):
            
            # ChatGPT fell down here and I had to add the bellow code to split blocks into 10
            genbank_format += f"{i + 1:9} "
            
            spliceA = i                
            spliceB = i + 10
            
            for x in range(6):
                
                genbank_format += f"{dna_sequence[spliceA:spliceB]} "
                
                spliceA += 10
                spliceB += 10

                
                
            genbank_format += "\n"
    
        genbank_format += "//\n"
    
        return genbank_format

    
    def translate_dna_to_amino_acids(self,dna_sequence):
        # Define the translation table as a dictionary
        genetic_code = {
            'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
            'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
            'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
            'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
            'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
            'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
            'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
            'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }

        amino_acid_sequence = []
        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i:i + 3]
            amino_acid = genetic_code.get(codon, 'X')  # 'X' for unknown or stop codons
            amino_acid_sequence.append(amino_acid)

        return ''.join(amino_acid_sequence)



    def reverse_complement(self,dna_sequence):
        
        dna_sequence = dna_sequence.lower()
        
        complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
        reverse_comp_seq = []

        for base in reversed(dna_sequence):
            if base in complement:
                reverse_comp_seq.append(complement[base])
            else:
                # Handle gaps or incorrect base letters
                reverse_comp_seq.append(base)

        return ''.join(reverse_comp_seq)


    def translation_reversal(self,dna_sequence):
        
        dna_sequence = dna_sequence.upper()
        
        forward_frame1 = self.translate_dna_to_amino_acids(dna_sequence)
        forward_frame2 = self.translate_dna_to_amino_acids(dna_sequence[1:])
        forward_frame3 = self.translate_dna_to_amino_acids(dna_sequence[2:])

        reverse_complement = self.reverse_complement(dna_sequence)
        reverse_complement = reverse_complement.upper()
        reverse_frame1 = self.translate_dna_to_amino_acids(reverse_complement)
        reverse_frame2 = self.translate_dna_to_amino_acids(reverse_complement[1:])
        reverse_frame3 = self.translate_dna_to_amino_acids(reverse_complement[2:])
        
        return "\nForward\n1 "+ forward_frame1 + "\n2 " + forward_frame2 + "\n3 " + forward_frame3 + "\nReverse\n1 " + reverse_frame1 +"\n2 "+ reverse_frame2 +"\n3 " + reverse_frame3

    def count_nucleotides(self,sequence):
        # Initialize dictionaries to store counts
        single_nucleotide_counts = {'a': 0, 't': 0, 'c': 0, 'g': 0}
        di_nucleotide_counts = {}
        tri_nucleotide_counts = {}

        # Iterate over the sequence to count nucleotides
        for i in range(len(sequence)):
            # Count single nucleotides
            nucleotide = sequence[i]
            single_nucleotide_counts[nucleotide] += 1

            # Count di-nucleotides (two adjacent nucleotides)
            if i < len(sequence) - 1:
                di_nucleotide = sequence[i:i+2]
                if di_nucleotide in di_nucleotide_counts:
                    di_nucleotide_counts[di_nucleotide] += 1
                else:
                    di_nucleotide_counts[di_nucleotide] = 1

            # Count tri-nucleotides (three adjacent nucleotides)
            if i < len(sequence) - 2:
                tri_nucleotide = sequence[i:i+3]
                if tri_nucleotide in tri_nucleotide_counts:
                    tri_nucleotide_counts[tri_nucleotide] += 1
                else:
                    tri_nucleotide_counts[tri_nucleotide] = 1

        return single_nucleotide_counts, di_nucleotide_counts, tri_nucleotide_counts


    def calculate_gc_content(self,sequence):
        # Count the number of G and C bases in the sequence
        gc_count = sequence.count('g') + sequence.count('c')

        # Calculate the total number of bases in the sequence
        total_bases = len(sequence)

        # Calculate the GC content as a percentage
        gc_content_percentage = (gc_count / total_bases) * 100

        return gc_content_percentage