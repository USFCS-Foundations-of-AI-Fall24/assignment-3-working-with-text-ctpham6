from Cluster import *
from Document import *
from make_dataset import create_docs


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
    # Clusters the 80%
    # Classifies the other 20%
    # Repeats until every individual document has been classified
    fold_size = len(documents) // 5
    averages = []
    i = 0
    while i < 5:
        if i == 4:
            docs_to_classify = documents[fold_size * 4:len(documents)]
            docs_to_cluster = documents[0:fold_size * 4]
        else:
            docs_to_classify = documents[(fold_size * i):(fold_size * (i + 1))]
            docs_to_cluster = documents[:fold_size * i] + documents[(fold_size * (i + 1)):]

        clusters = k_means(2, ['pos','neg'], docs_to_cluster)

        for doc in docs_to_classify :
            averages.append(doc.true_class == classify(clusters, doc))
        i += 1

    return round(sum(averages) / len(averages), 2)

def classify_submission_showcase(doc_count = 50) :
    print("Percentage of the", doc_count * 2, "documents that were classified CORRECTLY was", five_fold_cross_validation(100, doc_count), "out of 1.00")

if __name__=="__main__" :
    five_fold_cross_validation(100, 50)