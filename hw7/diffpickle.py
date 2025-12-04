import pickle

with open("myall.pickle", "rb") as f1, open("all.pickle", "rb") as f2:
    obj1 = pickle.load(f1)
    obj2 = pickle.load(f2)

print(obj1 == obj2)
