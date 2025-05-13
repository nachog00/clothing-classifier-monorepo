if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
import pandas as pd

@custom
def transform_custom(df,*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # Combine inputs into a single text feature
    def combine_features(row):
        url_part = str(row.get("identificador_de_url", "")).lower()
        cat_part = str(row.get("categorias", "")).lower()
        return f"{url_part} {cat_part}"

    df = pd.DataFrame(df)  # ensure it's a DataFrame

    df = df[df["label"].notnull()]  # keep labeled rows only

    df["text"] = df.apply(combine_features, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42)),
    ])

    pipeline.fit(X_train, y_train)

    # Save the model to mounted volume
    model_path = "/home/src/model_output/clothing_classifier.pkl"
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(pipeline, model_path)

    return {
        "accuracy": pipeline.score(X_test, y_test),
        "model_path": model_path,
        "train_samples": len(X_train),
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
