import pandas as pd
import pickle 
df = pd.read_excel(r'C:\Users\Yogita Wamanse\Desktop\PBLwebsite\ML\KPK data set.xlsx')

X = df.drop(columns=['D1'])
y = df.D1

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

import xgboost as xgb

model = xgb.XGBClassifier()

model.fit(X_train,y_train)

pickle.dump(model, open("model.pkl", "wb"))