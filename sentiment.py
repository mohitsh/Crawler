import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_recall_curve, auc
from sklearn.cross_validation import ShuffleSplit

np.set_printoptions(precision=20) # increase decimal places
data = pd.read_csv('data/full-corpus.csv')

X = data.TweetText
Y = data.Sentiment


classes = np.unique(Y)

unique, counts = np.unique(Y, return_counts=True)

"""
# print Prior
n = sum(counts)
for elem in (zip(unique,counts)):
    print("P(C={0}) = {1}".format(elem[0],round(elem[1]/n,3)))
"""


# take all the rows where sentiment is positive or negative
pos_neg_index = np.logical_or(Y=="positive", Y=="negative")


# take X and Y accordingly
X = X[pos_neg_index]
Y = Y[pos_neg_index]


Y = (Y=="positive").astype(int)


def ngram_creator():
    tfidf = TfidfVectorizer(ngram_range=(1,3), analyzer="word", binary=False)
    clf = MultinomialNB()
    pipeline = Pipeline([('vect', tfidf), ('clf', clf)])
    return pipeline


def model_trainer(clf_hub, X, Y):
    cv = ShuffleSplit(n=len(X), n_iter=10, test_size=0.3, random_state=0)
    scores = []
    pr_scores = []

    for train, test in cv:
        X_train, Y_train = X[train], Y[train]
        X_test, Y_test = X[test], Y[test]

        clf = clf_hub()
        clf.fit(X_train, Y_train)

        train_score = clf.score(X_train, Y_train)
        test_score  = clf.score(X_test, Y_test)

        scores.append(test_score)
        proba = clf.predict_proba(X_test)
        
        Y_test = Y_test.astype(int) # next step needs ints as value
        precision, recall, pr_thresholds = precision_recall_curve(Y_test, proba[:,1])
        pr_scores.append(auc(recall, precision))

    summary = (np.mean(scores), np.std(scores), np.mean(pr_scores), np.std(pr_scores))
    print("scores_mean: {0}\nscores_std: {1}\npr_scores_mean: {2}\npr_socres_std: {3}\n".format(summary[0],summary[1], summary[2], summary[3]))

X = X.values.astype('U')
Y = Y.values.astype('U')
model_trainer(ngram_creator,X,Y)
