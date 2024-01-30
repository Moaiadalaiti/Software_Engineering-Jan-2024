import pandas as pd
import pickle

file_to_open = open('data\models\baummethoden_lr.pickle', 'rb')

trained__model = pickle.load(file_to_open)
file_to_open.close()

prediction_data = pd.read_csv('data\prediction_data.csv', sep=";")

print(trained__model.predict(prediction_data))
