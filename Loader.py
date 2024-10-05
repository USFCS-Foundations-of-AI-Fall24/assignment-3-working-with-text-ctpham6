## Code for loading training sets and creating documents.
import string
from turtledemo.clock import datum

from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])
def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        ## deal with filters here
        for f in filters:
            words = [word for word in words if f(word)]

        ## deal with transforms here

        d.add_tokens(words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

def not_stopword(token) :
    return token not in ['a','an','the']

def not_cat(token) :
    return token is not 'cat'


# transforms - convert a token into a new format

# you do this.
def remove_trailing_punct(token) :
    pass

# and this
def convert_to_lowercase(token) :
    pass



## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes) :

    # hlist will be the homogeneity for each cluster.
    hlist = []

    largest_class = list_of_classes[0]
    count = 1
    i = 1
    while i < len(list_of_classes) :
        if largest_class == list_of_classes[i]:
            count += 1
        else:
            if count == 1:
                largest_class = list_of_classes[i]
            else:
                count -= 1

    i = 0
    for cluster in list_of_clusters :
        biggest_class_count = 0
        for document in cluster.members:
            if document.true_class == largest_class:
                biggest_class_count += 1
        hlist[i] = biggest_class_count / len(cluster.members)
        i += 1

    return hlist

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])

def compute_completeness(list_of_clusters, list_of_classes) :

    # clist will be the completeness for each cluster.
    clist = []

    clist_index = 0
    for cluster in list_of_clusters :
        dom_class_count = 0
        dominant_class = cluster.true_class
        for document in cluster.members:
            if document.true_class == dominant_class:
                dom_class_count += 1
        clist[clist_index] = dom_class_count / len(cluster.members)
        clist_index += 1

    return clist

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(10,10)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])





