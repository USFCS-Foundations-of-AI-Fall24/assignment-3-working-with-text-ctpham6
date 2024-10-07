## Code for loading training sets and creating documents.
import string
from turtledemo.clock import datum

from docutils.utils.smartquotes import default_smartypants_attr

from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword, not_car],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])
def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        for f in filters:
            if f == 'not_stopword':
                words = [word for word in words if not_stopword(word)]
            elif f == 'not_cat':
                words = [word for word in words if not_cat(word)]

        for t in transforms:
            if t == 'convert_to_lowercase':
                word = 0
                while word < len(words):
                    words[word] = convert_to_lowercase(words[word].lower())
                    word += 1
            elif t == 'remove_trailing_punct':
                word = 0
                while word < len(words):
                    words[word] = remove_trailing_punct(words[word])
                    word += 1
        d.add_tokens(words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

def not_stopword(token) :
    return token not in ['a','an','the']

def not_cat(token) :
    return token != 'cat'


# transforms - convert a token into a new format

def remove_trailing_punct(token) :
    return token.strip(string.punctuation)

def convert_to_lowercase(token) :
    return token.lower()



## Calculates the fraction of the cluster that consists of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes) :

    # hlist will be the homogeneity for each cluster.
    hlist = []

    # goes through every cluster to find the largest class in each of them
    for cluster in list_of_clusters :
        largest_class = None
        # count variable is to find the largest class
        count = 0
        # list keeps track of count of each class in cluster corresponding with list_of_classes[i]
        # if class_count[0] = 5, then the frequency of the class in list_of_classes[0] is 5
        class_count = defaultdict(lambda:0)
        # for every document in the cluster, if its classes are valid, increment the frequency list and count
        # calculate the largest class as needed
        for doc in cluster.members:
            if doc.true_class in list_of_classes :
                class_count[list_of_classes.index(doc.true_class)] += 1
                if count == 0:
                    largest_class = doc.true_class
                else:
                    if largest_class != doc.true_class:
                        count -= 1
                    else:
                        count += 1
        # my own decision to use the first class as the largest class if there is an equal amount of them
        # calculates the homogeneity (# articles of largest class / total # articles to 2 places)
        if count == 0 :
            hlist.append(round(class_count[0] / len(cluster.members), 2))
        else :
            hlist.append(round(class_count[list_of_classes.index(largest_class)] / len(cluster.members), 2))

    return hlist

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])
def compute_completeness(list_of_clusters, list_of_classes) :

    # clist will be the completeness for each cluster.
    clist = []
    # list to count the total documents and their classes according to list_of_classes[i]
    # if class_count[0] = 5, then the frequency of the class in list_of_classes[0] is 5
    # sum(doc_class_counter) = total doc num
    doc_class_counter = defaultdict(lambda:0)
    for class_type in list_of_classes :
        doc_class_counter[list_of_classes.index(class_type)] = 0
    # for every cluster, go through its members and calculate their members
    for cluster in list_of_clusters :
        for doc in cluster.members:
            if doc.true_class in list_of_classes :
                doc_class_counter[list_of_classes.index(doc.true_class)] += 1

    for cluster in list_of_clusters :
        # list keeps track of count of each class in cluster corresponding with list_of_classes[i]
        # if class_count[0] = 5, then the frequency of the class in list_of_classes[0] is 5
        class_count = defaultdict(lambda:0)
        for class_type in list_of_classes:
            class_count[list_of_classes.index(class_type)] = 0
        # count variable is to find the largest class
        count = 0
        largest_class_index = -1
        # for every document in the cluster, if its classes are valid, increment the frequency list and count
        # calculate the largest class as needed
        for doc in cluster.members:
            if doc.true_class in list_of_classes:
                class_count[list_of_classes.index(doc.true_class)] += 1
                if count == 0:
                    largest_class_index = list_of_classes.index(doc.true_class)
                else:
                    if largest_class_index != list_of_classes.index(doc.true_class):
                        count -= 1
                    else:
                        count += 1
        # my own decision to make largest class the first class in the cluster if the amounts are equal
        if count == 0 :
            largest_class_index = 0
        # calculates completeness. Takes the amount of docs of the largest class present in the cluster and divides it
        # by the total amount of documents that identify with that class. Rounded to 2 decimal places
        clist.append(round(class_count[largest_class_index] / doc_class_counter[largest_class_index], 2))
    return clist

def loader_submission_showcase() :
    pos_reviews, neg_reviews = create_docs(50, 50)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                          filters=[],
                                          transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                          filters=[],
                                          transforms=[])

    result = k_means(2, ['pos', 'neg'], positive_docs + negative_docs)
    print("Out of every cluster, what percentage of their documents are comprised of the most common class?")
    print("Homogeneity:")
    for homogeneity in compute_homogeneity(result, ['pos', 'neg']):
        print(homogeneity)
    print(
        "\nOut of every cluster's most common class, what percentage of all documents in said common class are in the cluster?")
    print("Completeness:")
    for completeness in compute_completeness(result, ['pos', 'neg']):
        print(completeness)

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(50,50)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])

    result = k_means(2, ['pos', 'neg'], positive_docs + negative_docs)
    print("Out of every cluster, what percentage of their documents are comprised of the most common class?")
    print("Homogeneity:")
    for homogeneity in compute_homogeneity(result, ['pos','neg']):
        print(homogeneity)
    print("\nOut of every cluster's most common class, what percentage of all documents in said common class are in the cluster?")
    print("Completeness:")
    for completeness in compute_completeness(result, ['pos', 'neg']):
        print(completeness)




