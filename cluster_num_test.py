import gensim
from sentence_transformers import SentenceTransformer, util
import re
from sklearn.cluster import KMeans
import matplotlib
import torch
import numpy
device = torch.device("cpu")
embedder = SentenceTransformer('/home/chenyuchong/NLP-Series-sentence-embeddings/output/sts-sbert-macbert-64-2022-03-05_10-23-37',device=device)
file = open('content.txt', encoding='utf-16')

fstr = []
sentence = []
while True:
    rd = file.readline()
    if not rd:
        break
    sentence.append(rd)
flen = len(fstr)

OMP_NUM_THREADS=3 #解除内存限制

word_embedding = {}

sentences = []
words = {}
count = 1
sentences_map = {}
for items in sentence:
    items = re.findall(r'[\u4e00-\u9fa5]',items)
    str1 = ''
    for itemss in items:
        str1 += itemss
    sentences.append(str1)
    sentences_map[str1] = count
    count += 1
corpus_embeddings = embedder.encode(sentences)
lenc = len(corpus_embeddings)
print('encoded')
num_clusters = [300,500,700,900,1000]
for num_cluster in num_clusters:
    clustering_model = KMeans(n_clusters=num_cluster)
    clustering_model.fit(corpus_embeddings)
    print('fit')
    cluster_assignment = clustering_model.labels_
    cluster_centre = clustering_model.cluster_centers_
    clustered_sentences = [[] for i in range(num_cluster)]
    overall_distance = 0.
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        clustered_sentences[cluster_id].append(sentences[sentence_id])

    print('done')

    for i, cluster in enumerate(clustered_sentences):
        strf="cluster"+str(num_cluster)+"//Cluster"+str(i+1)+".txt"
        writing = open(strf,'w+',encoding='utf-16')
        writing.write(str(cluster_centre[i]))
        writing.write('\n')
        cluster = str(cluster)
        writing.write(cluster)
        writing.close()
    distance = 0.
    for i in range(0,lenc):
        distance+=numpy.linalg.norm(corpus_embeddings[i]-cluster_centre[cluster_assignment[i]])
    writing=open('result.txt','a')
    writing.write(str(num_cluster)+" distance:"+str(distance)+'\n')
    writing.close()