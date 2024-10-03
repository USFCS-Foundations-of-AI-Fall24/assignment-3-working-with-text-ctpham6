import random

from nltk.data import retrieve

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

    def calculate_centroid(self):
        # The centroid is a Document whose token counts are the average of all the token counts of its members
        centroid = Document()
        union = []
        for document in self.members :
            union |= document.tokens.keys()

        for item in union :
            doc_count_to_average = 0
            token_sum = 0
            for document in self.members :
                if item in document.tokens.keys() :
                    doc_count_to_average += 1
                    token_sum += document.tokens[item]
            centroid.tokens[item] = token_sum / doc_count_to_average

        return centroid


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    # initially assign data randomly.
    for document in data :
        random_cluster = random.choice(cluster_list)
        random_cluster.members.append(document)

    # compute initial cluster centroids
    for cluster in cluster_list :
        cluster.centroid = cluster.calculate_centroid()

    done = False
    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    while not done :
        moved = False
        for cluster in cluster_list :
            for document in cluster.members :
                sim_to_compare = cosine_similarity(document, cluster.centroid)
                for cluster_candidate in cluster_list :
                    if cosine_similarity(document, cluster_candidate.centroid) > sim_to_compare:
                        cluster_candidate.members.append(document)
                        cluster.members.remove(document)
                        moved = True
        if not moved :
            done = True

    #   compute the centroids of each cluster
    for cluster in cluster_list :
        cluster.centroid = cluster.calculate_centroid()

    return cluster_list