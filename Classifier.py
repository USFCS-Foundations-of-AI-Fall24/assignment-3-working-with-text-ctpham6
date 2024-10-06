from Cluster import *
from Document import *
from make_dataset import create_docs
from submission import doc_to_add


def classify(clusters, item) :
    dist = 10000
    best = None
    for c in clusters :
        d = cosine_similarity(c.centroid, item)
        if d < dist :
            dist = d
            best = c
    return best.centroid.true_class


def five_fold_cross_validation(nwords, nelements) :
    pass
    ## generate nelements documents of each type (pos and neg), with nwords words in each doc.
    documents = []
    word_sets = create_docs(nelements, nelements, nwords)

    for set in word_sets[0] :
        doc_to_add = Document(true_class='pos')
        doc_to_add.add_tokens(set)
        documents.append(doc_to_add)
        
    for set in word_sets[1] :
        doc_to_add = Document(true_class='neg')
        doc_to_add.add_tokens(set)
        documents.append(doc_to_add)

    # divide the documents into 5 folds.
    ## for i = 1 to 5
    # cluster 80% of the documents. (four folds)
    #    use classify to classify the other 20%.
    #    measure accuracy - how many of the documents were classified correctly?
    # return the average accuracy


