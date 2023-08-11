import cv2
from copy import deepcopy
from gene import Gene
import numpy as np
import random
def white_img():
 img_white = np.ones((180, 180, 3), np.uint8)
 img_white[:] = 255
 return deepcopy(img_white)
class Individual:
 def __init__(self, num_genes=50):
 self.fitness = None
 self.num_genes = num_genes
 chromosome = []
 for index in range(num_genes):
 gene_var = Gene()
 gene_var.values()
 chromosome.append(gene_var)
 self.chromosome = chromosome
 #evaluate fitness
 def eval_ind(self):
 img = white_img()
 img_source = cv2.imread("painting.png")
 for gene in self.chromosome:
 overlay = deepcopy(img)
 cv2.circle(overlay, (gene.x, gene.y), gene.radius, (gene.B, 
gene.G, gene.R), thickness=-1)
 cv2.addWeighted(overlay, gene.A, img, 1 - gene.A, 0.0, img)
 self.fitness = -np.sum(np.square(img_source - img))
 #mutation in individuals
 def mut_ind(self, mutation_prob=0.2, mutation_type="guided"):
 while random.random() < mutation_prob:
 gen = random.randint(0, self.num_genes - 1)
 self.chromosome[gen].mutgene(mutation_type)
 self.fitness = None
 #get image
 def lastimg(self):
 img = white_img()
 self.chromosome.sort(key=lambda x: x.radius, reverse=True)
 for gene in self.chromosome:
 overlay = deepcopy(img)
 cv2.circle(overlay, (gene.x, gene.y), gene.radius, (gene.B, 
gene.G, gene.R), thickness=-1)
 cv2.addWeighted(overlay, gene.A, img, 1 - gene.A, 0.0, img)
 return img
