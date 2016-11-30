#import pywikibot
import csv
import numpy as np
from math import sqrt
from collections import defaultdict

ENTITY_2_ID = {}
ID_2_ENTITY = {}
RELATION_2_ID = {}
ID_2_RELATION = {}
LEFT_E = {}
RIGHT_E = {}
#
LNUM = {}
RNUM = {}

def return_zero():
    return 0

class Train:

    def __init__(self):
        self.fb_l, self.fb_r, self.fb_h = [], [], []
        self.ok = {}

    def add(self, e1_id, e2_id, relation_id):
        self.fb_h.append(e1_id)
        self.fb_r.append(relation_id)
        self.fb_l.append(e2_id)
        if (e1_id, relation_id) not in self.ok:
            self.ok[(e1_id, relation_id)] = defaultdict(return_zero)
        self.ok[(e1_id, relation_id)][e2_id] = 1             

def prepare(train_obj):
    with open('./data/entity2id.txt','r') as e2id, open('./data/relation2id.txt', 'r') as r2id:
        for line in e2id:
            entity, entity_id = line.split('\t')
            ENTITY_2_ID[entity] = int(entity_id)
            ID_2_ENTITY[int(entity_id)] = entity
        for line in r2id:
            relation, relation_id = line.split('\t')
            RELATION_2_ID[relation] = int(relation_id)
            ID_2_RELATION[int(relation_id)] = relation
    with open('./data/train.txt', 'r') as train_file:
        for line in train_file:
            e1, e2, relation = line.split('\t')
            relation = relation[:-1] #remove newline
            if e1 not in ENTITY_2_ID or e2 not in ENTITY_2_ID:
                print('WARNING: %s not in ENTITY_2_ID'% (e1 if e1 not in ENTITY_2_ID else e2))
            if relation not in RELATION_2_ID:
                print('WARNING %s not in RELATION_2_ID' % relation)
                relation_num = len(RELATION_2_ID)
                RELATION_2_ID[relation] = relation_num
                ID_2_RELATION[relation_num] = relation
            def default_dict_factory_function():
                return 0
            if RELATION_2_ID[relation] not in LEFT_E:
                LEFT_E[RELATION_2_ID[relation]] = defaultdict(default_dict_factory_function)
            if RELATION_2_ID[relation] not in RIGHT_E:
                RIGHT_E[RELATION_2_ID[relation]] = defaultdict(default_dict_factory_function)
            LEFT_E[RELATION_2_ID[relation]][ENTITY_2_ID[e1]] += 1
            RIGHT_E[RELATION_2_ID[relation]][ENTITY_2_ID[e2]] += 1
            train_obj.add(ENTITY_2_ID[e1], ENTITY_2_ID[e2], RELATION_2_ID[relation])
    for i in range(0, len(RELATION_2_ID)):
        sum1, sum2 = len(LEFT_E[i]), sum(LEFT_E[i].values())
        LNUM[i] = float(sum2)/float(sum1)
        sum1, sum2 = len(RIGHT_E[i]), sum(RIGHT_E[i].values())
        RNUM[i] = float(sum2)/float(sum1)
            


def main():
    train_obj = Train()
    prepare(train_obj)
    


    #print("DATA READ IN")
    #entitySet = set()
    #relationSet = set()
    #for triplet in triplets:
	   #entities.add(triplet[0])
	   #entities.add(triplet[2])
	   #relations.add(triplet[1])
    #epsilon = 0.1

def cost():
    pass


def learnTransE(k, batchSize, trainingSet, entities, labels, margin):
	labelEmbeddings = [np.random.uniform(low=-6/sqrt(k), high=6/sqrt(k), size=(k, 1)) for l in labels]
	labelNorm = np.linalg.norm(labelEmbeddings)
	labelEmbeddings = labelEmbeddings/labelNorm
	entityEmbeddings = [np.random.uniform(low=-6/sqrt(k), high=6/sqrt(k), size=(k, 1)) for e in entities]
	while True: # cost() > epsilon or num_iter < x
		entityNorm = np.linalg.norm(entityEmbeddings)
		entityEmbeddings = entityEmbeddings/entityNorm



if __name__ == '__main__':
    main()
