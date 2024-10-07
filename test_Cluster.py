from lib2to3.btm_utils import tokens
from unittest import TestCase
from Cluster import *
from Document import *
from make_dataset import create_docs


class TestCluster(TestCase):
    def test_calculate_centroid(self):
        d = Document(true_class='pos')
        d.add_tokens(['the', 'quick', 'brown', 'fox'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        d4 = Document(true_class='pos')
        d4.add_tokens(['the', 'quick', 'brown', 'fox'])
        d5 = Document(true_class='pos')
        d5.add_tokens(['cat', 'dog', 'fish'])
        d6 = Document(true_class='neg')
        d6.add_tokens(['bunny', 'lizard', 'octopus'])
        cluster = Cluster(members=[d, d2, d3, d4, d5, d6])
        print(str(cluster.calculate_centroid()))

    def test_kmeans(self):
        pos_sets, neg_sets = create_docs(50, 50, 100)
        docs = []
        for set in pos_sets:
            doc_to_add = Document(true_class='pos')
            doc_to_add.add_tokens(set)
            docs.append(doc_to_add)
        for set in neg_sets:
            doc_to_add = Document(true_class='neg')
            doc_to_add.add_tokens(set)
            docs.append(doc_to_add)
        print(k_means(2, ['pos', 'neg'], docs))


