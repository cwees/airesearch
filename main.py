# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from networkExtractor import processFile


def main():
    input = os.getcwd() + "\input\\"
    for file in os.listdir(input):
        processFile(input + file)
    print()
    print("finished processing all csv files!")

main()
