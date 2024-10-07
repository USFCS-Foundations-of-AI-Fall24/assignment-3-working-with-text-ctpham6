from unittest import TestCase
from Cluster import *
from Document import *

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
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        d4 = Document(true_class='pos')
        d4.add_tokens(['the', 'quick', 'brown', 'fox', 'skibidi'])
        d5 = Document(true_class='pos')
        d5.add_tokens(['cat', 'dog', 'fish', 'toilet'])
        d6 = Document(true_class='neg')
        d6.add_tokens(['bunny', 'lizard', 'octopus', 'bop', 'bop', 'yes', 'yes'])
        print(k_means(2, ['pos', 'neg'], [d,d2,d3,d4,d5,d6]))


