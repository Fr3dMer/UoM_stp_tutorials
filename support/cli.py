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
        self.parser.add_argument('--input', help='Input file path', required=True)
        self.parser.add_argument('--output', help='Output file path', required=True)
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

    # Perform actions based on the parsed arguments
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    if verbose_mode:
        print("Verbose mode enabled")