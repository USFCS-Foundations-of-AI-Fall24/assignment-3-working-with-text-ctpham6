import string
from unittest import TestCase

from nltk.corpus import stopwords

from Loader import *


class Test(TestCase):
    def test_apply_filters(self):
        pos_reviews, neg_reviews = create_docs(10, 10)
        has_stopword = False
        for document in create_easy_documents(pos_reviews, 'pos', filters=['not_stopword'], transforms=[]):
            for token in document.tokens:
                if token in ['a','an','the']:
                    has_stopword = True
        self.assertEqual(has_stopword,False)

    def test_apply_transforms(self):
        pos_reviews, neg_reviews = create_docs(10, 10)
        for document in create_easy_documents(pos_reviews, 'pos', filters=[], transforms=['remove_trailing_punct']):
            for token in document.tokens:
                if any(string.punctuation in token for token in document.tokens):
                    assert (False)
        assert (True)

    def test_workflow(self):
        pos_reviews, neg_reviews = create_docs(10, 10)

        positive_docs = create_easy_documents(pos_reviews, 'pos',
                                              filters=[],
                                              transforms=[])

        negative_docs = create_easy_documents(neg_reviews, 'neg',
                                              filters=[],
                                              transforms=[])



