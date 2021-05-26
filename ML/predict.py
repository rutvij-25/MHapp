import pickle
import numpy as np 

# test = [0, 3, 0, 1, 0, 4, 3, 0, 2, 2, 4, 3, 3, 4, 4, 4, 2, 2, 2, 2, 4, 4, 2, 3, 4, 4, 2, 4, 2, 3, 4, 2, 4, 4, 2, 4, 3, 3, 1, 2]

def predict(ans):
    ans = np.array(ans)
    ans = ans.reshape(1,-1)
    loaded_model = pickle.load(open("ML\model.pkl", 'rb'))
    result = loaded_model.predict(ans)
    return result

# print(predict(test))