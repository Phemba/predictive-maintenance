import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
import joblib 

#Loading the dataset
df = pd.read_csv('data/ai4i2020.csv')

#drop columns that don't contribute to the prediction - labels/IDs
df = df.drop(columns=['UDI', 'Product ID'])


#Convert Type (L/M/H) to numerical values [[Encoding]]
type_mapping = {'L': 0, 'M': 1, 'H': 2}
df['Type'] = df['Type'].map(type_mapping)

print(df['Type'].value_counts())
print(df.dtypes)

#Drop leakage columns -- These directly reveal the input vales

df = df.drop(columns=['TWF', 'HDF', 'PWF', 'OSF', 'RNF'])

#Split into features (X) and target (y)
X = df.drop(columns=['Machine failure'])
y = df['Machine failure']

print(X.columns.tolist())
print(X.shape, y.shape)

#Split into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)                                                    

#Train the model
model = RandomForestClassifier(
    n_estimators=100, # number of decision trees to create
    max_depth=6,      # how deep each tree can grow limiting overfitting
    random_state=42,  # make results reproducible
    class_weight='balanced'
)
model.fit(X_train, y_train)

#Evaluate on the test set
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred): .3f}")
print(f"Precision: {precision_score(y_test, y_pred, zero_division=0): .3f}")
print(f"Recall: {recall_score(y_test, y_pred, zero_division=0): .3f}")
print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"\nFull Report:\n{classification_report(y_test, y_pred, zero_division=0)}")

#Save the trained model to disk
joblib.dump(model, 'model.joblib')
print("Model trained and saved!")

print(df.head())
print(df.shape)

