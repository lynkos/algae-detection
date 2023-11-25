import pickle
with open('X_cal.pkl', 'rb') as f:
    (X) = pickle.load(f)
with open('y_cal.pkl', 'rb') as f:
    (y) = pickle.load(f)

print(type(X))
print(type(y))
print(X.shape)
print(y[5])