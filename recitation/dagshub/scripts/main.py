import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score, accuracy_score, precision_score, recall_score, \
    f1_score
from sklearn.model_selection import train_test_split


def feature_engineering(raw_df):
    df = raw_df.copy()
    df['CreationDate'] = pd.to_datetime(df['CreationDate'])
    df['CreationDate_Epoch'] = df['CreationDate'].astype('int64') // 10 ** 9
    df['MachineLearning'] = df['Tags'].str.contains('machine-learning').fillna(False)
    df = df.drop(columns=['Id', 'Tags'])
    df['Title_Len'] = df.Title.str.len()
    df['Body_Len'] = df.Body.str.len()
    # Drop the correlated features
    df = df.drop(columns=['FavoriteCount'])
    df['Text'] = df['Title'].fillna('') + ' ' + df['Body'].fillna('')
    return df


def fit_tfidf(train_df, test_df):
    tfidf = TfidfVectorizer(max_features=25000)
    tfidf.fit(train_df['Text'])
    train_tfidf = tfidf.transform(train_df['Text'])
    test_tfidf = tfidf.transform(test_df['Text'])
    return train_tfidf, test_tfidf, tfidf


def fit_model(train_X, train_y):
    clf_tfidf = LogisticRegression(solver='sag')
    clf_tfidf.fit(train_X, train_y)
    return clf_tfidf


def eval_model(clf, X, y):
    y_proba = clf.predict_proba(X)[:, 1]
    y_pred = clf.predict(X)
    return {
        'roc_auc': roc_auc_score(y, y_proba),
        'average_precision': average_precision_score(y, y_proba),
        'accuracy': accuracy_score(y, y_pred),
        'precision': precision_score(y, y_pred),
        'recall': recall_score(y, y_pred),
        'f1': f1_score(y, y_pred),
    }


if __name__ == '__main__':
    print('Loading data...')
    df = pd.read_csv('data/CrossValidated-Questions.csv')
    train_df, test_df = train_test_split(df)
    del df

    train_df = feature_engineering(train_df)
    test_df = feature_engineering(test_df)

    print('Fitting TFIDF...')
    train_tfidf, test_tfidf, tfidf = fit_tfidf(train_df, test_df)

    print('Fitting classifier...')
    train_y = train_df['MachineLearning']
    model = fit_model(train_tfidf, train_y)

    train_metrics = eval_model(model, train_tfidf, train_y)
    print('Train metrics:')
    print(train_metrics)

    test_metrics = eval_model(model, test_tfidf, test_df['MachineLearning'])
    print('Test metrics:')
    print(test_metrics)
