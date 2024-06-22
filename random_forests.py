from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# import feature_extraction as fe
# import pandas as pd




def train_random_forests(df, labels):
    X,y = df , labels
    
    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    # train_model
    model = RandomForestClassifier(n_estimators=100, random_state = 42)
    model.fit(X_train, y_train)
    
    return model

def predict_labels(model,df):
    return model.predict(df)


