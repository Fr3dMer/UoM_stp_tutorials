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
        
        
        
        # Conditions for each problem:
        self.ex2_1_dna_sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"

        
        
    def execute(self,logger):
        if (self.ex2_1 in self.clean_args):
            output = self.format_genbank(self.ex2_1_dna_sequence)
            message = self.ex2_1 + " Answer: " + str(output)
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
