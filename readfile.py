import pickle



list1=[2,3,4,5,6,7]
fileName="data.pickel"


with open("data.pickle", "wb") as file:
    
    pickle.dump(list1, file)
print("Data has been serialized and saved to data.pickle")

with open("data.pickle", "rb") as file:
   
    loaded_data = pickle.load(file)
print("Deserialized data:", loaded_data)


