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
vec_list = [[] for i in range(1,NUM_CLUSTERS+1)]
for i in range(1,NUM_CLUSTERS+1):
    vec_dims = 0
    openstr = '/home/chenyuchong/spider/cluster1000/'+'Cluster'+str(i)+'.txt'
    opensv = '/home/chenyuchong/spider/cluster1000/' + 'Cluster' + str(i) + '_vec.txt'
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
        for items in rdln:
            get_matrix = np.append(get_matrix,float(items))
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
    readvec = open(opensv,'r')

    while True:
        rdln = readvec.readline()
        if not rdln:
            break
        rdln = rdln[1:-1]
        rdln = rdln.split(',')
        emptylst = np.array([])
        for items in rdln:
            emptylst = np.append(emptylst,items)
        vec_list[i].append(emptylst)

print('finished loading')
while True:
    sentence = str(input())
    sentence = re.findall(r'[\u4e00-\u9fa5]',sentence)
    empty_str = ""
    for items in sentence:
        empty_str += items
    sentence = empty_str
    sentence = embedder.encode(sentence)
    cluster_choice = -1
    cluster_distance = 114514
    for i,items in enumerate(center_matrix):
        distance = np.linalg.norm(sentence-items)
        if cluster_choice == -1:
            cluster_choice = i
            cluster_distance = distance
        else:
            if cluster_distance > distance:
                cluster_distance = distance
                cluster_choice = i

    print(cluster_choice)
    ans_choice = -1
    ans_distance = 1919810
    for i,items in enumerate(ans_list[cluster_choice]):
        print(items)
        encoding = vec_list[cluster_choice][i]
        distance = np.linalg.norm(sentence-encoding)
        if ans_choice == -1:
            ans_choice = i
            ans_distance = distance
        else:
            if ans_distance > distance:
                ans_distance = distance
                ans_choice = i
    print(ans_list[cluster_choice][ans_choice])
    print('done')



