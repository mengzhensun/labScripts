# labScripts
## cleanResults.py
clean the ddG data from hex code
together with two files:
mutation.edge (contains the hex code with mutation)
results.txt (from command "grep "ddG =" *log > results.txt)

## searchCompleted.py
use name with format mutation_XXXXXX and command qacct to search the completed jobs, and then use date to filt(name is trucated, thus duplicate)

## foldx calculation
running commands: 
python autoddG.py 3SGB (#num of mutations) (#of build running times) (#of repair times) (chain name) 
