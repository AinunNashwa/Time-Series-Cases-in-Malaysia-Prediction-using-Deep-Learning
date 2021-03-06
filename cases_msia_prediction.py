# -*- coding: utf-8 -*-
"""cases_msia_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bTIWX-efk_EerK72mj0-JqaF1EISbnEY

This script is about Prediction on Time-Series data using Deep Learning(ANN),
on cases in Malaysia
"""

!cp /content/drive/MyDrive/Colab\ Notebooks/modules_case_msia.py /content

from modules_case_msia import EDA,ModelCreation,model_evaluation
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from tensorflow.keras.layers import LSTM,Dense,Dropout
from tensorflow.keras.callbacks import TensorBoard
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model
from tensorflow.keras import Input

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import pickle
import os

#%% Statics

CSV_TRAIN_DATA = os.path.join(os.getcwd(), "/content/drive/MyDrive/Colab Notebooks/cases_malaysia_train.csv")
MMS_PICKLE_PATH = os.path.join(os.getcwd(),'mms_case.pkl')

log_dir = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
LOG_FOLDER_PATH = os.path.join(os.getcwd(), '/content/sample_data/cases_msia_prediction/logs_cases_msia',log_dir)

#%% EDA
# Step 1: Data Loading

df = pd.read_csv(CSV_TRAIN_DATA, na_values='?')

# Step 2: Data Inspection

print(df.info())
print(df.describe().T)

#cases_new : 674 non-null : object
# convert to numeric cases_new to get the nan values
df['cases_new'] = pd.to_numeric(df['cases_new'],errors='coerce')
df.info()
print(df['cases_new'].isna().sum())

# Plot the graph

eda = EDA()
eda.plot_graph(df)

# Step 3: Data Cleaning
# df['cases_new] has 12 nans --> use df.interpolate

df['cases_new'] = df['cases_new'].interpolate()
print(df['cases_new'].isna().sum())

# To check the nan imputation
print(df['cases_new'].head(100))

# To make sure no decimal points in cases_new
df['cases_new'] = np.ceil(df['cases_new'])
print(df['cases_new'].head(100))

# Step 4: Features selection
# Choose cases_new

# Step 5: Preprocessing

mms = MinMaxScaler()
df = mms.fit_transform(np.expand_dims(df['cases_new'],axis=-1))

# Save model
with open(MMS_PICKLE_PATH, 'wb') as file:
  pickle.dump(mms,file)

X_train = []
y_train = []

win_size = 30

for i in range(win_size,np.shape(df)[0]):
  X_train.append(df[i-win_size:i,0])
  y_train.append(df[i,0])

X_train = np.array(X_train)
y_train = np.array(y_train)

# Model Development

mc = ModelCreation()
model = mc.sequential_layer(X_train,drop_rate=0.05,output_node=1)

# Model Compile
model.compile(optimizer='adam',
              loss='mse',
              metrics='mape')


# Callback

tensorboard_callback = TensorBoard(log_dir=LOG_FOLDER_PATH)

X_train = np.expand_dims(X_train,axis=-1)
hist = model.fit(X_train,y_train,
                 batch_size=64,
                 epochs=500,
                 callbacks=tensorboard_callback)

# Plot Model Architecture
plot_model(model,show_layer_names=(True),show_shapes=(True))

#%% Model Evaluation

print(hist.history.keys())

plt.figure()
plt.plot(hist.history['mape'])
plt.title('Mape')
plt.show()

plt.figure()
plt.plot(hist.history['loss'])
plt.title('Loss')
plt.show

#%% EDA for test Data: 100 dataset
CSV_TEST_DATA = os.path.join(os.getcwd(), "/content/drive/MyDrive/Colab Notebooks/cases_malaysia_test.csv")

# Step 1: Data Loading
test_df = pd.read_csv(CSV_TEST_DATA, na_values='null')

# Step 2: Data Inspection
print(test_df.info())
print(test_df['cases_new'].isna().sum()) # check nan value=1

test_df['cases_new'] = test_df['cases_new'].interpolate()
print(test_df['cases_new'].isna().sum())

# To check the nan imputation
print(test_df['cases_new'].head(65))

# To make sure no decimal points in cases_new
test_df['cases_new'] = np.ceil(test_df['cases_new'])
print(test_df['cases_new'].head(65))

test_df = mms.transform(np.expand_dims(test_df['cases_new'],axis=-1))
con_test = np.concatenate((df,test_df),axis=0)
con_test = con_test[-130:]

X_test = []
for i in range(win_size,len(con_test)):
  X_test.append(con_test[i-win_size:i,0])

X_test = np.array(X_test)

predicted = model.predict(np.expand_dims(X_test,axis=-1))

print((X_test).shape)
print((test_df).shape)

# Plotting the graph

plt.figure()
plt.plot(test_df,'r',label='actual new cases')
plt.plot(predicted,'b',label='predicted new cases')
plt.title('Actual vs Predicted')
plt.legend()
plt.show()

plt.figure()
plt.plot(mms.inverse_transform(test_df),'r',label='actual new cases')
plt.plot(mms.inverse_transform(predicted),'b',label='predicted new cases')
plt.title('Actual_i vs Predicted_i')
plt.legend()
plt.show()

me = model_evaluation()
me.plot_predicted_graph(test_df,predicted,mms)

# To evaluate the answer of MAPE using formulae:
print('Check for MAPE using formulae')
print((mean_absolute_error(test_df, predicted)/sum(abs(test_df))) *100)

#%% Model Saving
MODEL_SAVE_CASE = os.path.join(os.getcwd(),'model_case_msia.h5')
model.save(MODEL_SAVE_CASE)

#%% Discussion
# From the above result, the model achieve good MAPE which is less than 1%
# The cases_new data is being trained and evaluated and produced the good output
# The model can predict well when using only LSTM,Dense and Dropout Layer 
# because the small number of data which is only approximately 700
# The data preprocesing involved only cleaning the null and also change dtype to numeric.
# For this dataset, it produced good accuracy when the dropout rate is being lowered 
# and the number of epochs is being increased.

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %reload_ext tensorboard
# %tensorboard --logdir /content/sample_data/cases_msia_prediction/logs_cases_msia