'''This is the argument parser class'''
import argparse

class ArgumentParser:
    
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Amazon Web Services using AWS-SDK")
        self.parser.add_subparsers(help='commands')

        #create argument init
        self.parser.add_argument('init', help='Initialize the module')

    def parse_args(self):
        return self.parser.parse_args()