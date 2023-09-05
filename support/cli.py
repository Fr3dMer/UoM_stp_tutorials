"""************************************************************************************************
File          : cli.py
About         : Object for processing args passed in during script init
Author        : Freddie Mercer
*************************************************************************************************"""

import argparse

class myArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="My Command Line Tool")
        self.add_arguments()

    def add_arguments(self):
        # Define your command-line arguments here
        self.parser.add_argument('--ex1', type=str, help='Which exercise 1 problems would you like running?', required=False)
        self.parser.add_argument('--ex2', type=str, help='Which exercise 2 problems would you like running?', required=False)
        self.parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')

    def parse_args(self):
        # Parse the command-line arguments and return the result
        return self.parser.parse_args()

# Example usage:
if __name__ == "__main__":
    arg_parser = myArgumentParser()
    args = arg_parser.parse_args()

    # Access the parsed arguments
    input_file = args.input
    output_file = args.output
    verbose_mode = args.verbose

