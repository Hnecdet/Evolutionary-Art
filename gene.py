import numpy as np
import cv2
import matplotlib.pyplot as plt
import random
from math import floor
from copy import deepcopy
import time
def within_img(x, y, radius):
 if x < 0:
 if y < 0:
 if x + radius >= 0 and y + radius >= 0:
 return True
 elif 0 <= y <= 180:
 if x + radius >= 0:
 return True
 else:
 if x + radius >= 0 and y - radius <= 180:
 return True
 elif 0 <= x <= 180:
 if y < 0:
 if y + radius >= 0:
 return True
 elif 0 <= y <= 180:
 return True
 else:
 if y - radius <= 180:
 return True
 else:
 if y < 0:
 if x - radius >= 180 and y + radius >= 0:
 return True
 elif 0 <= y <= 180:
 if x - radius >= 180:
 return True
 else:
 if x - radius >= 180 and y - radius <= 180:
 return True
 return False
class Gene:
 def __init__(self, x=1, y=3, radius=4, B=1, G=1, R=4, A=0.2):
 self.x = random.randint(-30, 210)
 self.y = random.randint(-30, 210)
 self.radius = random.randint(1, 60)
 # if not in the image
 while not within_img(self.x, self.y, self.radius):
 self.x = random.randint(-30, 210)
 self.y = random.randint(-30, 210)
 self.radius = random.randint(1, 60)
 self.B = random.randint(0, 255)
 self.G = random.randint(0, 255)
 self.R = random.randint(0, 255)
 self.A = random.random()
 def values(self):
 self.x = random.randint(-30, 210)
 self.y = random.randint(-30, 210)
 self.radius = random.randint(1, 60)
 # if not in the image
 while not within_img(self.x, self.y, self.radius):
 self.x = random.randint(-30, 210)
 self.y = random.randint(-30, 210)
 self.radius = random.randint(1, 60)
 self.B = random.randint(0, 255)
 self.G = random.randint(0, 255)
 self.R = random.randint(0, 255)
 self.A = random.random()
 #mutation in genes
 def mutgene(self, mutation_type="guided"):
 if mutation_type == "guided":
 self.x += random.randint(int(-0.25 * abs(self.x)), int(0.25 * 
abs(self.x)))
 self.y += random.randint(int(-0.25 * abs(self.y)), int(0.25 * 
abs(self.y)))
 self.radius = random.randint(max(0, self.radius - 10), max(0, 
self.radius + 10))
 self.R = random.randint(max(0, self.R - 64), min(255, self.R + 
64))
 self.G = random.randint(max(0, self.G - 64), min(255, self.G + 
64))
 self.B = random.randint(max(0, self.B - 64), min(255, self.B + 
64))
 self.A += random.uniform(max(0, self.A - 0.25), min(1, self.A + 
0.25))
 return self
 elif mutation_type == "unguided":
 self.values()
