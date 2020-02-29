This project uses sodapy api to download NYC parking violations data. And it also contains the docker file to build the docker container to use the python code.

The main.py call the api function to download data. To run the main.py, just type:

python main.py input.txt output.txt

in command line window.

input.txt is the input file, which contains two parameters. One is the page size, and one is the num of page. It can be set as:
2 3

Here 2 is the page size and 3 is the num of page.

src directory contains the api python code.

output.txt file saves the downloaded data.