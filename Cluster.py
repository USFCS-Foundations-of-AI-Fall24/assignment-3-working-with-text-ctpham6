import random

from Document import *

class Cluster :
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid :
            self.centroid = centroid
        else :
            self.centroid = Document(true_class='pos')
        if members :
            self.members = members
        else :
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

    ## You do this.
    def calculate_centroid(self):
        # The centroid is a Document whose token counts are the average of all the token counts of its members
        centroid = 0
        for document in self.members :
            centroid += len(document.tokens)
        return centroid / len(self.members)


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    # initially assign data randomly.
    for document in data :
        random_cluster = random.choice(cluster_list)
        random_cluster.append(document)

    # compute initial cluster centroids
    for cluster in cluster_list :
        cluster.centroid = cluster.calculate_centroid()

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    

    #   compute the centroids of each cluster
    for cluster in cluster_list :
        cluster.centroid = cluster.calculate_centroid()

    return cluster_list