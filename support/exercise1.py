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
        
        # Usefull var
        self.ex1_1 = "ex1.1"
        self.ex1_2 = "ex1.2"
        self.ex1_3 = "ex1.3"
        self.ex1_4 = "ex1.4"
        
        
        
        # Conditions for each problem:
        self.ex1_1_a = 5
        self.ex1_1_b = 6
        
        self.ex1_2_input_string = "TheUniversityOfManchesterFacultyofBiologyMedicineAndHealth"
        self.ex1_2_pair1 = (3,13)
        self.ex1_2_pair2 = (15,25)
        
        self.ex1_3_a = 50 
        self.ex1_3_b = 100
        
        
    def execute(self,logger):
        if (self.ex1_1 in self.clean_args):
            output = self.calculate_hypotenuse_square(self.ex1_1_a,self.ex1_1_b)
            message = self.ex1_1 + " Answer: " + str(output)
            logger.log(message)
            
        if (self.ex1_2 in self.clean_args):
            output = self.extract_slices(self.ex1_2_input_string,self.ex1_2_pair1,self.ex1_2_pair2)
            message = self.ex1_2 + " Answer: " + str(output)
            logger.log(message)

        if (self.ex1_3 in self.clean_args):
            output = self.sum_odd_integers(self.ex1_3_a,self.ex1_3_b)
            message = self.ex1_3 + " Answer: " + str(output)
            logger.log(message)



    # Solving the actual problems themselves 
    def calculate_hypotenuse_square(self,a, b):
        hypotenuse_square = (a**2) + (b**2)
        return hypotenuse_square
    
    def extract_slices(self, input_string, pair1, pair2):
        start1, end1 = pair1
        start2, end2 = pair2
    
        # Ensure the pairs are in ascending order
        if start1 > start2:
            start1, end1, start2, end2 = start2, end2, start1, end1
    
        # Extract the slices based on the number pairs
        slice1 = input_string[start1:end1]
        slice2 = input_string[start2:end2]
    
        return slice1 + slice2

    def sum_odd_integers(self,a, b):
        total = 0
        for num in range(a, b + 1):
            if num % 2 != 0:  # Check if the number is odd
                total += num
        return total