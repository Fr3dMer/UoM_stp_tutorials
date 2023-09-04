"""************************************************************************************************
File          : exercise1.py
About         : Funcs to solve firs set of exercises
Author        : Freddie Mercer
*************************************************************************************************"""

import re

class exercise1:
    def __init__(self,args):
        # Defensive clean and spliting of args
        clean_args = re.sub('[ \t\n\r]',"",args)    
        clean_args = clean_args.lower()
        self.clean_args = clean_args.split(',')
        
        # Conditions for each problem:
        self.ex1_1_a = 10
        self.ex1_1_b = 6
        
        
        
    def execute(self,logger):
        if ("ex1.1" in self.clean_args):
            output = self.calculate_hypotenuse_square(self.ex1_1_a,self.ex1_1_b)
            message = "1.1: " + str(output)
            logger.log(message)

    def calculate_hypotenuse_square(self,a, b):
        hypotenuse_square = a**2 + b**2
        return hypotenuse_square