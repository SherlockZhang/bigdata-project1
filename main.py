#from sys import argv
from src import api
from sys import argv
import json
from src.load_elasticsearch import load_elasticsearch

def main():
    #input file
    input_fn = 'input.txt'#argv[1]
    
    #ouptut file
    try:
        output_file = 'output2.json'#argv[2]
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
    output_data = []
    for i in range(num_page):
            temp_data=api.get_data(page_size,i) 
            output_data.extend(temp_data)
    with open(output_file, 'w') as outfile:
        json.dump(output_data, outfile)
        #outfile.write("\n")
        
    load_elasticsearch("output2.json", "nyc_index")

    #return output_data
    
if __name__ == '__main__':
    main()
    