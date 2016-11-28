import pywikibot
import csv
import numpy as np
from math import sqrt

fbTrainPath = "train.txt"
triplets = []
with open(fbTrainPath) as tsv:
	for line in csv.reader(tsv, delimiter="\t"):
		triplets.append(line)

# entities = set([triplet[0] for triplet in triplets] + [triplet[2] for triplet in triplets])
# relations = set([triplet[1] for triplet in triplets])
entitySet = set()
relationSet = set()
for triplet in triplets:
	entities.add(triplet[0])
	entities.add(triplet[2])
	relations.add(triplet[1])

epsilon = 0.1
def cost():



def learnTransE(k, batchSize, trainingSet, entities, labels, margin):
	labelEmbeddings = [np.random.uniform(low=-6/sqrt(k), high=6/sqrt(k), size=(k, 1)) for l in labels]
	labelNorm = np.linalg.norm(labelEmbeddings)
	labelEmbeddings = labelEmbeddings/labelNorm
	entityEmbeddings = [np.random.uniform(low=-6/sqrt(k), high=6/sqrt(k), size=(k, 1)) for e in entities]
	while True: # cost() > epsilon or num_iter < x
		entityNorm = np.linalg.norm(entityEmbeddings)
		entityEmbeddings = entityEmbeddings/entityNorm