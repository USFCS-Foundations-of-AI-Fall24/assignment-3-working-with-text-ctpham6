from unittest import TestCase
from Document import *


class TestDocument(TestCase):
    def testinit(self):
        d = Document(true_class='pos')
        print(d.tokens['fish'])

    def test_addTokens(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        self.assertEqual(d.tokens['cat'], 1)
        self.assertEqual(d.tokens['aardvark'], 0)


class Test(TestCase):
    def test_euclidean_distance(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        self.assertEqual(euclidean_distance(d, d2), 0)
        d3 = Document(true_class='pos')
        d3.add_tokens(['cat', 'bunny', 'fish'])
        self.assertEqual(euclidean_distance(d, d3), 2)

    def test_cosine_similarity(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        print(cosine_similarity(d,d2))
        self.assertAlmostEqual(cosine_similarity(d,d2),1,4)
