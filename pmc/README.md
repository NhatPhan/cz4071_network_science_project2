Parallel Maximum Clique (PMC)
=====================================

### Setup
Compile the parallel maximum clique library.  

		$ make

*PMC* has been tested on Ubuntu linux (10.10 tested) and Mac OSX (Lion tested) with gcc-mp-4.7 and gcc-mp-4.5.4
   
   
### Run

All the datasets are inside `data` folder. 

To run PMC algorithm for amazon dataset with one thread:

		./pmc -f data/amazon.mtx -a 0 -t 1
	
To run for other datasets only need to change the file name in the command
		
