# ACI_Assignment_1_Genetic_Alogorithm

**Problem Statement**

Implement a Genetic Algorithm to maximize the following function:
f(x)=x^2
where: 0≤x≤31
Represent z using a 5-bit binary chromosome.

**Requirements**

a. Your implementation must include:

b. Binary chromosome encoding

c. Population initialization

d. Fitness evaluation

e. Roulette wheel selection

f. Single-point crossover

g. Bit-flip mutation

h. Elitism

i. Termination after fixed generations

**Tasks**

a. Generate an initial population of 10 chromosomes.

b. Decode chromosomes into decimal values.

c. Compute fitness values.

d. Perform selection using roulette wheel selection.

e. Apply crossover with probability Pc=0.8

f. Apply mutation with probability Pm=0.01

g. Run the algorithm for 50 generations.

h. Plot:

Best fitness vs generation

Average fitness vs generation

**Expected Deliverables**

a. Python source code

b. Graphs

c. Short report explaining:

I. GA workflow

II. Role of mutation and crossover

III. Observations from results

**Sample Input:**

Population Size = 10

Chromosome Length = 5 bits

Fitness Function: f(x) = x^2

Parameters:

Pc = 0.8

Pm = 0.01

Generations = 50

Initial Population:

10101

00111

11100

01010

10011

01101

11001

00011

11111

00101

**Sample Output**

Generations 0

------------------------------------------------
|Chromosome |Decimal(x) |Fitness f(x)=x^2|
|-----------|-----------|----------------|
|10101 |21 |441|

|00111 |7| 49|

|11100 |28| 784|

|01010 |10| 100|

|10011 |19| 361|

|01101 |13| 169|

|11001 |25| 625|

|00011 |3| 9|

|11111 |31| 961|

|00101 |5| 25|

Best Chromosome: 11111

Best Fitness: 961

Average Fitness: 352.4

------------------------------------------------
After 50 Generations

------------------------------------------------
Best Chromosome: 11111

Decoded Value (x): 31

Maximum Fitness: 961

Final Population Sample:

11111

11110

11111

11101

11111

11111

11110

11111

11101

11111

**Observations:**

- Population converged toward the optimal value x = 31.
- Roulette wheel selection favored high-fitness chromosomes.
- Mutation occasionally introduced diversity.
- Elitism preserved the best solution across generations.

**Graphs Generated:**
1. Best Fitness vs Generation
2. Average Fitness vs Generation
