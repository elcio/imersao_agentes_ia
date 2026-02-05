import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from rich import print
import joblib

df = pd.read_csv("buscape.csv", sep="\t")

X = df['review_text'].fillna('').astype(str)
Y = df['rating'].astype(int)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = Pipeline([
    ('vectorizer', TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
    ('classifier', LogisticRegression(max_iter=3000, class_weight='balanced'))
])

model.fit(X_train, Y_train)

pred = model.predict(X_test)

if model.score(X_test, Y_test) > 0.8:
    joblib.dump(model, 'rating.joblib')
    print('Success!')

