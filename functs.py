import cv2
from matplotlib import pyplot as plt
from copy import deepcopy
from gene import Gene
import os
from indv import Individual
from math import floor
import random
class Population:
 def __init__(self, num_inds=20, num_genes=50, tm_size=5, frac_elites=0.2, 
frac_parents=0.6, mutation_prob=0.2,
 mutation_type="guided"):
 self.num_inds = num_inds
 self.num_genes = num_genes
 self.tm_size = tm_size
 self.frac_elites = frac_elites
 self.frac_parents = frac_parents
 self.mutation_prob = mutation_prob
 self.mutation_type = mutation_type
 self.elite_list = []
 self.winner_list = []
 self.offspring_list = []
 self.poplist = [Individual(num_genes=num_genes) for i in range(0, 
num_inds)]
 self.remains_list = []
 def eval_pop(self):
 for ind in self.poplist:
 ind.eval_ind()
 def mut_pop(self):
 for ind in self.remains_list:
 ind.mut_ind(mutation_prob=self.mutation_prob, 
mutation_type=self.mutation_type)
 temp = self.elite_list + self.remains_list
 self.poplist = deepcopy(temp)
 def sel(self):
 self.poplist = sorted(self.poplist, key=lambda x: x.fitness, 
reverse=True)
 for i in range(floor(self.num_inds * self.frac_elites)):
 temp = deepcopy(self.poplist[i])
 self.elite_list.append(temp)
 for i in range(floor(self.num_inds * self.frac_parents)):
 self.winner_list.append(self.pop_tmsel())
 for i in range(len(self.elite_list)):
 self.poplist.pop(len(self.poplist) - 1)
 return self.elite_list[0]
 # in lecture notes
 def pop_tmsel(self):
 x = random.randrange(0, len(self.poplist))
 best = self.poplist[x]
 x = self.tm_size
 while x > 0:
 x = x - 1
 temp_x = random.randrange(0, len(self.poplist))
 ind = self.poplist[temp_x]
 if ind.fitness > best.fitness:
 best = ind
 x = temp_x
 self.poplist.pop(x)
 return best
 def crossover(self):
 self.offspring_list.clear()
 self.remains_list.clear()
 while len(self.winner_list):
 if len(self.winner_list) == 1:
 self.offspring_list.append(self.winner_list.pop(0))
 else:
 parent1 = self.winner_list.pop(random.randrange(0, 
len(self.winner_list)))
 parent2 = self.winner_list.pop(random.randrange(0, 
len(self.winner_list)))
 children1 = Individual(self.num_genes)
 children2 = Individual(self.num_genes)
 for j in range(0, self.num_genes):
 if random.random() < 0.5:
 children1.chromosome[j] = parent1.chromosome[j]
children2.chromosome[j] = parent2.chromosome[j]
 else:
 children1.chromosome[j] = parent2.chromosome[j]
children2.chromosome[j] = parent1.chromosome[j]
 self.offspring_list.append(children1)
 self.offspring_list.append(children2)
 self.remains_list = self.poplist + self.offspring_list
