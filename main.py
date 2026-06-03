import random

class Chromosome():
    def __init__(self):
        self.population=[]

    def initialize_population(self,pop_size=10, chromosome_length=5):        
        for _ in range(pop_size):
            chromosome = ''.join(random.choice(['0', '1'])for _ in range(chromosome_length))
            self.population.append(chromosome)        

    def encode(self,decimal_value):
        return format(decimal_value, '05b')    

    def decode_population(self,population):
        return [int(chromosome, 2) for chromosome in population]

    def calculate_fitness(self,decoded_values):    
        return [x**2 for x in decoded_values]

if __name__=='__main__':
    POPULATION_SIZE = 10
    CHROMOSOME_LENGTH = 5

    chromosomes=Chromosome()
    chromosomes.initialize_population(POPULATION_SIZE,CHROMOSOME_LENGTH)

    print("Initial Population:")
    for chromosome in chromosomes.population:
        print(chromosome)        