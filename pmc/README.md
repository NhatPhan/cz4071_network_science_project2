Parallel Maximum Clique (PMC)
=====================================

### Setup
First, you'll need to compile the parallel maximum clique library.  

		$ make

*PMC* has been tested on Ubuntu linux (10.10 tested) and Mac OSX (Lion tested) with gcc-mp-4.7 and gcc-mp-4.5.4
   
### Compute Maximum Clique

All the datasets are inside `data` folder. To run PMC algorithm for dataset `X` with one thread:

		./pmc -f `data/X` -a 0 -t 1
		
Example:

		./pmc -f data/amazon.mtx -a 0 -t 1
		
