#from sys import argv
from src import api
from sys import argv
import json

def main():
    #input file
    input_fn = argv[1]
    
    #ouptut file
    try:
        output_file = argv[2]
    except Exception:
        output_file = "output"
    
    #read input argument
    with open(input_fn, "r") as fh:
        for line in fh:
            line = line.strip('\n')
            page_size, num_page = line.split(' ')
    page_size = int(page_size)        
    num_page = int(num_page)

    #get nycdata from sodapy and write to output file
    for i in range(num_page):
            output_data=api.get_data(page_size,i) 
            with open(output_file, 'a') as outfile:
                json.dump(output_data, outfile)
                outfile.write("\n")


    
if __name__ == '__main__':
    main()