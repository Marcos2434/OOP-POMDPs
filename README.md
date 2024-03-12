
# Run

Grant execution permissions for the quick launch (Linux / Macos):

```
chmod +x start.sh
```

Then run, 

```
./start.sh
```


Changes to OOP

- file creation directory
- commented out the command line creation





# OOP (Optimal Observability Problem)

This work provides a method that given a POMDP how should one change the POMDP's observation capabilities within a fixed budget such that its (minimal) expected reward remains below a given threshold.

# Features
* Produce the code to calculate the desired POMDP for the line, grid, and maze POMDP benchmarks, based on the input size of the model, threshold, strategies (deterministic or randomized), and in some cases some fixed observations.
* Produce a sequence of fixed observations that served as an input to the given model.
* Includes the models used to fill out the tables of Section 4.

# Implementation
All the scripts are written in Python. The produced scripts are in Python and PRISM input code.

# Usage / Example (Z3)
The folders contain the models used for the experiments. The Python scripts contained in the folders deterministic_strategies and randomised_strategies can be run using the command: 

```
python3 script.py

```
We used the following command for the time: 

```
time python3 script.py

```
We included only the scripts for the optimal threshold. The rest can be produced using the scripts: create*Model*.py and create*Model*Fixed.py
or by changing the line of the code under the comment 

### We want to check if the minimal expected cost is below some threshold <=threshold

to the desired threshold.

The script create*Model*.py produces the models of the POP and the script create*Model*Fixed.py produces the models of the SSP.

The scripts can be run as follows:
```
python3 createLine.py 5 2 2 '<= 1.5' 0 

```
Where this input is (size, target, budget, threshold, det), if det=0 we produce the code for randomized strategies if det=1 for the deterministic ones. One can define fixed sensors as follows:

```
python3 createLineFixed.py 5 2 2 '<= 1.5' 0 ' 0 0 | 1 1 | 3 3 | 4 4' (size, target, budget, threshold, det, fixed sensors)

```

The first arguments are the same as before. The last one indicates the fixed sensors. In this case '0 0 | 1 1' means state 0 emits observation

0 and state 1 emits observation 1 etc. To produce the input for the fixed sensors we include a python script predefined.py that can be run to produce the above sequence (1 unique observation

pee state. This can be run as follows for the line and the grid: 

```
python3 predefined.py 5

```
For the maze:

```
python3 predefined.py 3 5

```

The argument is the size of the corresponding model. The script produces a file with the desired sequence. Note that each model has a predefined file in the corresponding folder. Example Grid:

```
python3 createGrid.py 3 8 2 'Q(9,4)' 1 (size of one side, target, budget, threshold, det)

```

```
python3 createGridFixed.py 3 8 2 '<= Q(9,4)' 1 ' 0 0 | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7' (size of one side, target, budget, threshold, det, fixedObservables)

```
Example Maze:

```
python3 createMaze.py 3 5 9 4 '<= Q(39,10)' 1 (size of the rows, size of the columns, target, budget, threshold, det)

```

```
python3 createMazeFixed.py 3 5 9 6 '<= Q(39,10)' 0 ' 0 0 | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 | 8 8 | 9 9 | 10 10' (size of the rows, size of the columns, target, budget, threshold, det, fixedObservables)

```
# Usage / Example (PRISM)

The folder prism_deterministic_strategies contains the PRISM models used for the experiments. The models can be run as follows:

```
./prism -pf 'Rmin=? [F 'target']' model.sm -exact

```
We used the following command for the time: 

```
time ./prism -pf 'Rmin=? [F 'target']' model.sm -exact

```
Other models can be created using the scripts: create*Model*.py and create*Model*Fixed.py included in each folder -line, grid, maze. As before create*Model*.py creates models for POP, while create*Model*Fixed.py creates models for SSP. One can again use the predefined.py script to create the sequence of fixed sensors. Example of using the scripts:

```
python3 createLine.py 5 2 2 (size, target, budget)

```

```
python3 createLineFixed.py 5 2 2 '0 0 | 1 1 | 3 3 | 4 4' (size, target, budget, fixed sensors)

```
For the grid, scripts have the same usage as the line. As before the size is given for one side (size = 3 means 9 states).

Example Maze

```
python3 createMaze.py 3 5 9 4 (size of the rows, size of the columns, target, budget)

```



