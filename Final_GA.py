
import random
import socket
import datetime
import matplotlib.pyplot as plt

# ========== Population Data Structure ==========

class Population:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def insert(self, chrom):
        """Insert a chromosome if capacity allows."""
        if len(self.items) >= self.max_size:
            print("Error: population is full, cannot insert chromosome.")
            return False
        self.items.append(chrom)
        return True

    def delete(self, index):
        """Delete chromosome at index, with bounds/empty checks."""
        if not self.items:
            print("Error: population is empty, cannot delete chromosome.")
            return False
        if index < 0 or index >= len(self.items):
            print("Error: invalid index, cannot delete chromosome.")
            return False
        del self.items[index]
        return True

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        return self.items[idx]

    def __setitem__(self, idx, value):
        self.items[idx] = value

    def as_list(self):
        return self.items


# ========== Encoding / Decoding ==========

def encode(decimal_value, chromosome_length=5):
    return format(decimal_value, f'0{chromosome_length}b')

def decode(chromosome):
    return int(chromosome, 2)

def fitness(x):
    return x**2


# ========== Population Initialization ==========

def random_initialization():
    pop_size1=10
    chrom_length1=5
    pc1=0.8
    pm1=0.01
    generations1=50
    population = Population(pop_size1)
    
    for _ in range(pop_size1):
        chromosome = ''.join(random.choice(['0', '1']) for _ in range(chrom_length1))
        population.insert(chromosome)
        
    return pop_size1, chrom_length1, pc1, pm1, generations1, population

def initialize_population(filename='inputPS16.txt'):    
    
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    params = {}
    initial_population = []

    i = 0
    # Read parameter lines until "Initial Population:"
    while i < len(lines):
        line = lines[i]
        if line.lower().startswith('initial population'):
            i += 1
            break
        if '=' in line:
            key, value = line.split('=', 1)
            params[key.strip().lower()] = value.strip()
        i += 1

    # Basic parameter validation
    try:
        pop_size = int(params['population size'])
        chrom_length = int(params['chromosome length'])
        pc = float(params.get('pc', '0.8'))
        pm = float(params.get('pm', '0.01'))
        generations = int(params.get('generations', '50'))
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid or missing parameter in input file: {e}")

    if pop_size <= 0 or chrom_length <= 0 or generations <= 0:
        raise ValueError("Population size, chromosome length, and generations must be positive.")
    if not (0.0 < pc <= 1.0) or not (0.0 <= pm <= 1.0):
        raise ValueError("Pc must be in (0,1], Pm must be in [0,1].")

    # Read initial population into list
    for j in range(pop_size):
        if i + j >= len(lines):
            raise ValueError("Not enough chromosomes in initial population section.")
        chrom = lines[i + j]
        if len(chrom) != chrom_length or any(c not in '01' for c in chrom):
            raise ValueError(f"Invalid chromosome '{chrom}' in input file.")
        initial_population.append(chrom)

    # Build Population object and demonstrate insert capacity check
    population = Population(max_size=pop_size)
    for chrom in initial_population:
        inserted = population.insert(chrom)
        if not inserted:
            # This should not happen if input is correct
            print("Warning: chromosome not inserted due to capacity limit.")
    
    return pop_size, chrom_length, pc, pm, generations, population

# ========== Evaluation ==========

def evaluate_population(population: Population):
    """
    Returns (fitness_values, best_ch, best_fit, avg_fit, decoded_values).
    """
    chroms = population.as_list()
    decoded = [decode(ch) for ch in chroms]
    fitness_values = [fitness(x) for x in decoded]
    total_fitness = sum(fitness_values)

    best_index = max(range(len(chroms)), key=lambda i: fitness_values[i])
    best_chromosome = chroms[best_index]
    best_fitness = fitness_values[best_index]
    avg_fitness = total_fitness / len(chroms) if chroms else 0.0

    return fitness_values, best_chromosome, best_fitness, avg_fitness, decoded


# ========== Selection ==========

def roulette_wheel_selection(population: Population, fitness_values):
    """
    Roulette wheel selection on Population.
    """
    chroms = population.as_list()
    total_fitness = sum(fitness_values)
    if total_fitness == 0 or len(chroms) == 0:
        print("Warning: total fitness is zero or population empty, selecting random chromosome.")
        return random.choice(chroms)

    r = random.uniform(0, total_fitness)
    cumulative = 0.0
    for chrom, fit in zip(chroms, fitness_values):
        cumulative += fit
        if cumulative >= r:
            return chrom
    return chroms[-1]

def select_mating_pool(population: Population, fitness_values):
    chroms = population.as_list()
    return [roulette_wheel_selection(population, fitness_values)
            for _ in range(len(chroms))]


# ========== Crossover ==========

def single_point_crossover(parent1: str, parent2: str, pc: float):
    if random.random() < pc:
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1, parent2

def apply_crossover(mating_pool, pc):
    new_population = []
    for i in range(0, len(mating_pool), 2):
        parent1 = mating_pool[i]
        parent2 = mating_pool[(i + 1) % len(mating_pool)]
        child1, child2 = single_point_crossover(parent1, parent2, pc)
        new_population.extend([child1, child2])
    return new_population[:len(mating_pool)]

# ========== Mutation ==========

def mutate_chromosome(chromosome: str, pm: float) -> str:
    bits = list(chromosome)
    for i in range(len(bits)):
        if random.random() < pm:
            bits[i] = '1' if bits[i] == '0' else '0'
    return ''.join(bits)

def apply_mutation(population_list, pm):
    return [mutate_chromosome(ch, pm) for ch in population_list]

# ========== Elitism ==========

def apply_elitism(old_population: Population, old_fitness_values, new_population_list):
    """
    Carry over the best chromosome from old_population into new_population_list.
    Uses Population.delete() to illustrate delete behavior.
    """
    old_chroms = old_population.as_list()
    if not old_chroms:
        print("Warning: old population empty, elitism skipped.")
        return Population(max_size=len(new_population_list))

    # Identify elite
    best_index = max(range(len(old_chroms)), key=lambda i: old_fitness_values[i])
    elite = old_chroms[best_index]

    # Create new Population from offspring
    new_pop = Population(max_size=len(new_population_list))
    for ch in new_population_list:
        new_pop.insert(ch)

    # Evaluate new population to find worst
    new_fitness_values, _, _, _, _ = evaluate_population(new_pop)
    worst_index = min(range(len(new_pop)), key=lambda i: new_fitness_values[i])

    # Delete worst using delete() with checks
    deleted = new_pop.delete(worst_index)
    if not deleted:
        print("Warning: could not delete worst chromosome during elitism.")

    # Try to insert elite, respecting capacity
    inserted = new_pop.insert(elite)
    if not inserted:
        print("Warning: could not insert elite chromosome due to full capacity.")

    return new_pop


# ========== Plotting ==========

def plot_fitness_separate(best_history, avg_history):
    generations = list(range(len(best_history)))

    # Plot 1: Best fitness vs generation
    plt.figure(figsize=(8, 4))
    plt.plot(generations, best_history, label='Best Fitness', color='blue')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Best Fitness vs Generation')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 2: Average fitness vs generation
    plt.figure(figsize=(8, 4))
    plt.plot(generations, avg_history, label='Average Fitness', color='orange')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness vs Generation')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ========== GA Driver ==========

def run_ga(pop_size1=10,chromosome_length1=5,pc1=0.8,pm1=0.01,generations1=50,seed=42):

    pop_size=10
    chromosome_length=5
    pc=0.8
    pm=0.01
    generations=50
    
    try:
        pop_size,chromosome_length,pc,pm,generations,population = initialize_population(pop_size1,chromosome_length1,pc1,pm1,generations1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        pop_size,chromosome_length,pc,pm,generations,population = random_initialization(pop_size1)
    
    random.seed(seed)
    
    with open('output_GA.txt', 'w') as out:
        
        def log(line=""):
            print(line)  
            print(line, file=out)      
            
        best_history = []
        avg_history = []

        # Generation 0
        fitness_values, best_ch, best_fit, avg_fit, decoded = evaluate_population(population)
        best_history.append(best_fit)
        avg_history.append(avg_fit)
        
        log("Generation 0")
        log("-" * 60)
        log(f"{'Chromosome':>10} {'Decimal(x)':>12} {'Fitness f(x)=x^2':>18}")
        log("-" * 60)
        for ch, x, f in zip(population.as_list(), decoded, fitness_values):
            log(f"{ch:>10} {x:>12} {f:>18}")
        log("-" * 60)
        log(f"Best Chromosome: {best_ch}")
        log(f"Best Fitness: {best_fit}")
        log(f"Average Fitness: {avg_fit:.2f}")
        log("-" * 60)

        for _ in range(generations):                
            mating_pool = select_mating_pool(population,fitness_values)
            offspring = apply_crossover(mating_pool,pc)
            offspring = apply_mutation(offspring,pm)
            population = apply_elitism(population,fitness_values,offspring)

            fitness_values, best_ch, best_fit, avg_fit, decoded = evaluate_population(population)
            best_history.append(best_fit)
            avg_history.append(avg_fit)

        # Final info
        log("")
        log(f"After {generations} Generations")
        log("-" * 60)
        log(f"Best Chromosome: {best_ch}")
        x_best = decode(best_ch)
        log(f"Decoded Value (x): {x_best}")
        log(f"Maximum Fitness: {best_fit}")
        log("")
        log("Final Population Sample:")
        for ch in population.as_list():
            log(ch)            
            
    plot_fitness_separate(best_history, avg_history)
    return population

if __name__ == "__main__":
    print("Execution Timestamp:", datetime.datetime.now())
    print("Virtual Machine ID / Hostname:", socket.gethostname())
    run_ga(10,5,0.8,0.01,50,42)
