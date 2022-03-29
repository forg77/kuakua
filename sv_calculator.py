from sentence_transformers import SentenceTransformer, util
import re
from sklearn.cluster import KMeans
import matplotlib
import numpy as np
import torch
device = torch.device("cpu")
embedder = SentenceTransformer('/home/chenyuchong/NLP-Series-sentence-embeddings/output/sts-sbert-macbert-64-2022-03-05_10-23-37',device=device)

NUM_CLUSTERS = 1000
MATRIX_LINES = 192

center_matrix = []
ans_list = []
for i in range(1,NUM_CLUSTERS+1):
    vec_dims = 0
    openstr = '/home/chenyuchong/spider/cluster1000/'+'Cluster'+str(i)+'.txt'
    #print(openstr)
    reading = open(openstr,'r',encoding='utf-16')
    get_matrix = np.array([])
    for j in range(1,MATRIX_LINES+1):
        rdln = reading.readline()
        if rdln[0] == '[':
            rdln = rdln[1:]
        if rdln[-2] == ']':
            rdln = rdln[:-2]
        rdln = rdln.split()
        vec_dims += len(rdln)

        if vec_dims == 768:
            break
    center_matrix.append(get_matrix)
    tosolve = ""
    while True:
        rdln = reading.readline()
        if not rdln:
            break
        tosolve += rdln
    tosolve = tosolve[1:-1]
    tosolve = tosolve.split(',')
    ans_list.append(tosolve)
    reading.close()
    opensv = '/home/chenyuchong/spider/cluster1000/'+'Cluster'+str(i)+'_vec.txt'
    writing = open(opensv,'w')
    for items in tosolve:
        svector = embedder.encode(items)
        svector = str(svector)
        writing.write(svector)
        writing.write('\n')
