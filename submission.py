from Cluster import k_means
from Document import Document
import Cluster
import make_dataset
from make_dataset import create_docs

def print_cluster(cluster_to_print):
    print("Cluster of class: " + cluster_to_print.centroid.true_class)
    print("Contains " + str(len(cluster_to_print.members)) + " Documents")
    doc = 1
    for document in cluster_to_print.members:
        print("Document", doc, "of class " + str(document.true_class))
        for token in document.tokens:
            print("Token: [" + str(token) + "] of value", document.tokens[token])
        doc += 1
        print("__________________________________")

# Here is my submission for Project 3
# Lets create some documents. 5 positive documents and 5 negative documents of length 100 should do
data = create_docs(5, 5)
documents = []

for pos_word_set in data[0]:
    doc_to_add = Document()
    doc_to_add.add_tokens(pos_word_set)
    documents.append(doc_to_add)

for neg_word_set in data[1]:
    doc_to_add = Document()
    doc_to_add.add_tokens(neg_word_set)
    documents.append(doc_to_add)

# K-means will be called to make and group the Documents by clusters
# This returns a cluster list
# For every cluster's centroid, print out its tokens and values
for cluster in k_means(2, ['pos', 'neg'], documents):
    print_cluster(cluster)
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")