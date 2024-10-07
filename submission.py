from Classifier import classify_submission_showcase
from Cluster import k_means
from Document import Document
from Loader import create_easy_documents, compute_homogeneity, compute_completeness, loader_submission_showcase
from make_dataset import create_docs
import pandasExercise

# Helper Function to print a cluster in a way that will not make scrolling through the print too long
def print_cluster(cluster_to_print, token_per_row = 2):
    print("Cluster of class: " + cluster_to_print.centroid.true_class)
    print("Contains " + str(len(cluster_to_print.members)) + " Documents")
    doc = 1
    for document in cluster_to_print.members:
        token_num = 1
        print("")
        print("Document", doc, "of class " + str(document.true_class))
        for token in document.tokens:
            if token_num % token_per_row == 0:
                print(token_num, ": " + str(token) + " =", document.tokens[token])
            else:
                print(token_num, ": " + str(token) + " =", document.tokens[token], "          ", end=" ")
            token_num += 1
        doc += 1
        print("")
        print("__________________________________")

# Here is my submission for Project 3
# Running the program will give the results of my pandasExercise.py.
# Every part of my output will be seperated by -_-_-_-_
# After that...
# Lets create some documents. 5 positive documents and 5 negative documents of length 100 should do
data = create_docs(5, 5, length=100, use_abnormalities=True)
documents = []

for pos_word_set in data[0]:
    doc_to_add = Document(true_class='pos')
    doc_to_add.add_tokens(pos_word_set)
    documents.append(doc_to_add)

for neg_word_set in data[1]:
    doc_to_add = Document(true_class='neg')
    doc_to_add.add_tokens(neg_word_set)
    documents.append(doc_to_add)

# Prints the documents in raw form. This proves that they exist, have classes, and have unique tokens
for document in documents:
    print(document)

print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
# K-means will be called to make and group the Documents by clusters
# This returns a cluster list
# For every cluster's centroid, print out its tokens and values
# Each token is printed out like this:  "[Token #] [Token String] of value [Token Value]"
cluster_list = k_means(2, ['pos', 'neg'], documents)
for cluster in cluster_list:
    print_cluster(cluster, token_per_row = 250)
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# This section will be to show Loader.py. What this function call will do is basically what the main does:
# First, it generates positive and negative docs. I set it as 50 positive and 50 negatives for a total of 100 docs
# Next, It calls k_means(2, ['pos', 'neg'], positive_docs + negative_docs), making 2 clusters with the generated docs
# Finally, it computes each cluster's homogeneity and completeness and prints its value in an ordered fashion
loader_submission_showcase()
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# This section will be to show Classifier.py. What this function call will do is call five_fold_cross_validation
# The function basically make 50 positive and 50 negative documents for a total of 100. Each doc has 100 tokens
# For 5 loops, 20% of those docs will individually be classified while 80% of those docs will be clustered
# Whether the docs are classified right are put in a boolean list. The percentage of documents classified
# correctly is outputted as a decimal point
classify_submission_showcase()
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("Done!")