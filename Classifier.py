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
    fold_size = len(documents) // 5
    docs_to_classify = documents[0:fold_size]
    docs_to_cluster = documents[fold_size:len(documents)]
    clusters = []
    for doc in docs_to_cluster :
        cluster_to_add = Cluster(centroid=Document(true_class=doc.true_class), members=[doc])
        cluster_to_add.calculate_centroid()
        clusters.append(cluster_to_add)

    averages = []
    for doc in docs_to_classify :
        averages.append(classify(clusters, doc))

    for average in averages :
        print(average)

five_fold_cross_validation(100, 40)