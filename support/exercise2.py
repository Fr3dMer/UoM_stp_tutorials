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

        
        
    def execute(self,logger):
        if (self.ex2_1 in self.clean_args):
            output = self.calculate_hypotenuse_square(self.ex1_1_a,self.ex1_1_b)
            message = self.ex2_1 + " Answer: " + str(output)
            logger.log(message)
            
        if (self.ex2_2 in self.clean_args):
            output = self.extract_slices(self.ex1_2_input_string,self.ex1_2_pair1,self.ex1_2_pair2)
            message = self.ex2_2 + " Answer: " + str(output)
            logger.log(message)

        if (self.ex2_3 in self.clean_args):
            output = self.sum_odd_integers(self.ex1_3_a,self.ex1_3_b)
            message = self.ex2_3 + " Answer: " + str(output)
            logger.log(message)

        if (self.ex2_4 in self.clean_args):
            output = self.print_dna_in_blocks(self.ex1_4_sequence,self.ex1_4_block_size)
            message = self.ex2_4 + " Answer: " + str(output)
            logger.log(message)
        
        if (self.ex2_5 in self.clean_args):
            output = self.transcribe_dna_to_rna(self.ex1_5_dna_sequence)
            message = self.ex2_5 + " Answer: " + str(output)
            logger.log(message)

    # Solving the actual problems themselves 
