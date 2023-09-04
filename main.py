"""************************************************************************************************
File          : main.py
About         : Entry point into the program to tie everything together
Author        : Freddie Mercer
    
*************************************************************************************************"""

import support.log as log_obj
import support.cli as cli
import support.exercise1 as ex1


# Main entry into programme, scaffold for logic 
def main():
    
    # Create a logger object
    logger = log_obj.myLogger()
    #logger.log("This is a log message.")

    # Process args 
    arg_parser = cli.myArgumentParser()
    args = arg_parser.parse_args()
    
    
    # Construct exercise 1 object and execute associated problems  
    if (args.ex1):
        exer1 = ex1.exercise1(args.ex1)
        exer1.execute(logger)

    # Construct exercise 2 object and execute associated problems 


    # Construct exercise 3 object and execute associated problems 


    # Construct exercise 4 object and execute associated problems 


    # Exit main
    return True


if __name__ == "__main__":
    main()