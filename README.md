# Evolutionary-Art
 The task is to create an image made of filled circles, visually similar to a given RGB source image (painting.png).
 
1 The Evolutionary Algorithm

The pseudocode for the algorithm is as follows:
Initialize population with <num_inds> individuals each having <num_genes> genes
While not all generations (<num_generations>) are computed:
Evaluate all the individuals
Select individuals
Do crossover on some individuals
Mutate some individuals

1.1 Individuals

Each individual has one chromosome. Each gene in a chromosome represents one circle to be drawn.
Each gene has at least 7 values:
• The center coordinates, (x, y)
• The radius, radius ∈ Z+
• The color (red, R ∈ Z, green, G ∈ Z, blue, B ∈ Z, alpha, A ∈ R) where (R, G, B) ∈ [0, 255]^3 and
A ∈ [0, 1]
The order of the tasks to perform circle drawing is important. The circles should be drawn in the
descending order of their radii. The first circle to be drawn is the one with the largest radius and the
last circle to be drawn is the one with the smallest radius. The genes should be sorted accordingly.
The center does not have to be within image boundaries. However, if a circle is not within the image (it
lies outside completely), the corresponding gene should be reinitialized randomly until it is.

1.2 Evaluation

In order to evaluate an individual, its corresponding image should be drawn first. Note that the chromosome order is important. The pseudocode is as follows:
Initialize <image> completely white with the same shape as the <source_image>.
For each gene in the chromosome:
overlay <- image
Draw the circle on overlay.
image <- overlay x alpha + image x (1-alpha)

1.3 Selection

<num elites> number of best individuals will advance to the next generation directly. The selection of
other individuals is done with tournament selection with size <tm size>.

1.4 Crossover

<num parents> number of individuals will be used for crossover. The parents are chosen among the best
individuals which do not advance to the next generation directly. Two parents will create two children.
Exchange of each gene is calculated individually with equal probability. The probabilities of child 1
having genei of parent 1 or parent 2 have equal probability, that is 0.5; child 2 gets the genei
from the
other parent which is not chosen for child 1, where 0 ⩽ i < <num genes>.


Table 1: Parameter configurations to be experimented.
        <num inds> 5 10 20 40 60
        <num genes> 15 30 50 80 120
        <tm size> 2 5 8 16
        <frac elites> 0.04 0.2 0.35
        <frac parents> 0.15 0.3 0.6 0.75
        <mutation prob> 0.1 0.2 0.4 0.75
        <mutation type> guided unguided
        
1.5 Mutation

The mutation is governed by <mutation prob>. While the generated random number is smaller than
<mutation prob> a random gene is selected to be mutated (same as in N Queen Problem in the lecture
notes). All individuals except the elites are subject to mutation.
There are two ways a gene can be mutated:
• Unguided
– Choose completely random values for x, y, radius, R, G, B, A.
• Guided
– Deviate the x, y, radius, R, G, B, A around their previous values.
∗ x– width/4 < x′ < x + width/4
∗ y– height/4 < y′ < y + height/4
∗ radius − 10 < radius′ < radius + 10
∗ R − 64 < R′ < R + 64
∗ G − 64 < G′ < G + 64
∗ B − 64 < B′ < B + 64
∗ A − 0.25 < A′ < A + 0.25
– The values should be corrected to a valid one in case they are not.

2 Experimental Work

You will experiment on several different hyperparameters. Namely,
• Number of individuals (<num inds>)
• Number of genes (<num genes>)
• Tournament size (<tm size>)
• Number of individuals advancing without change (<num elites>)
• Number of parents to be used in crossover (<num parents>)
• Mutation probability (<mutation prob>)
• Mutation type (guided or unguided)
To see the effect of each hyperparameter, run the algorithm for each value in a row given in Table
1 while using default values for the other hyperparemeters. The default values are bolded. Use <
num generations >= 10000.
For each hyperparameter, explain its effect and give the value which produces the best result. For each
experiment, you need to include:
• fitness plot from generation 1 to generation 10000
• fitness plot from generation 1000 to generation 10000
• the corresponding image of the best individual in the population at every 1000th generation.



