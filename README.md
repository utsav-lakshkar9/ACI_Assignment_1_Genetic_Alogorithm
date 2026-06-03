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
Chromosome Decimal(x) Fitness f(x)=x^2

------------------------------------------------

10101 21 441
00111 7 49
11100 28 784
01010 10 100
10011 19 361
01101 13 169
11001 25 625
00011 3 9
11111 31 961
00101 5 25
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
**Deliverables:**
● PDF document designPSXX_<group id>.pdf detailing your solution.
● [Group id] _Contribution.xlsx mentioning the contribution of each student in terms of percentage of work done. Columns must be “Student Registration Number”, “Name”, “Percentage of contribution out of 100%”. If a student did not contribute at all, it will be 0%, if all contributed then 100% for all.
● inputPSXX.txt file used for testing
● outputPSXX.txt file generated while testing
● .py file containing the python code. Create a single notebook. Do not fragment your code into multiple files
● Zip all of the above files including the design document in a folder with the name:
○ [Group id] _A1_PSXX_XXXXXXXXXX.zip and submit the zipped file.
○ Group Id should be given as Gxxx where xxx is your group number. For example, if your group is 26, then you will enter G026 as your group id.
Instructions:
● It is compulsory to make use of the data structure(s) / algorithms mentioned in the problem statement.
● Ensure that all data structure insert and delete operations throw appropriate messages when their capacity is empty or full. Also ensure basic error handling is implemented.
● For the purposes of testing, you may implement some functions to print the data structures or other test data. But all such functions must be commented before submission.
● Make sure that your read, understand, and follow all the instructions
● Ensure that the input, prompt and output file guidelines are adhered to. Deviations from the mentioned formats will not be entertained.
● The input, prompt and output samples shown here are only a representation of the syntax to be used. Actual files used to evaluate the submissions will be different. Hence, do not hard code any values into the code.
● Please note that the design document must include:
○ One alternate way of modeling the problem with the performance implications.
○ Writing a good technical report and well documented code is an art. Your report cannot exceed 4 pages. Your code must be modular and quite well documented.
○ You may ask queries in this dedicated discussion section. Beware that only hints will be provided and queries asked in other channels like MS Teams, emails, Taxila inbox will not be responded to.
Deadline
1. The strict deadline for submission of the assignment is 8th June 2026 11:55 PM IST (Monday).
2. The deadline has been set considering extra days from the regular duration in order to accommodate any challenges you might face. No further extensions will be entertained.
3. Late submissions will be evaluated as below. Submissions made between:
a. 8th June 2026 11:56PM to 9th June 2026 11:55PM → Deduct 2M for late submission and evaluation for 10 marks.
b. 9th June 2026 11:56PM to 10th June 2026 11:55PM → Deduct 6M for late submission and evaluation for 6marks.
c. Beyond 10th June 2026 11:55PM → No evaluations, 0 marks will be awarded.
How to submit
● This is a group assignment.
● Each group has to make one submission (only one, no resubmission) of solutions.
● Each group should zip all the deliverables in one zip file and name the zipped file as [Group id] _A1_PSXX_XXXXXXXXXX.zip and submit the zipped file.
● Group Id should be given as Gxxx where xxx is your group number. For example, if your group is 26, then you will enter G026 as your group id.
● Assignments should be submitted via Taxila > Assignment section. Assignments submitted via other means like email etc. will not be graded.
Evaluation
● The assignment carries 12 Marks.
● Grading will depend on:
● Fully executable code with all functionality working as expected
○ Well-structured and commented code
○ Accuracy of the design document.
○ Every bug in the functionality will have negative marking.
○ Marks will be deducted if your program fails to read the input file used for evaluation due to change / deviation from the required syntax.
● We encourage students to take the upcoming assignments and examinations seriously and submit only original work. Please note that plagiarism in assignments will be taken seriously. Refer to the detailed policy here.
● Source code files which contain compilation errors will get at most 25% of the value of that question.
Readings Artificial Intelligence: A Modern Approach Textbook by Peter Norvig and Stuart J. Russell, 4th Edition.
