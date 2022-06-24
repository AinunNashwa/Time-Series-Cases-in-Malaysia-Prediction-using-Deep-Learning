<a><img alt='tf' src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"></a>
<a><img alt = 'image' src="https://img.shields.io/badge/Spyder%20Ide-FF0000?style=for-the-badge&logo=spyder%20ide&logoColor=white"></a>
<a><img alt = 'image' src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></a>
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Spyder](https://img.shields.io/badge/Spyder-838485?style=for-the-badge&logo=spyder%20ide&logoColor=maroon)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

# Time-Series Cases in Malaysia Prediction using Deep Learning

### Descriptions
1) The objectives of this project is to develop a deep learning model using LSTM neural network to predict new cases in Malaysia.
2) The datasets contain approximately 700 training data and 100 testing data
3) It is a Time-Series problem and cases_new data is being trained and evaluated as per request
4) The model is being trained using Seqential, LSTM, Dropout and Dense Layer with 500 epochs
5) The model analysis is based on `mean_squared_error`,`mean_absolute_error`, `mean_absolute_percentage_error`

### Results
`Model`

![model](https://user-images.githubusercontent.com/106902414/175518804-21d7914e-9554-40e2-86c0-e0f1fd9052e9.PNG)



`Model Architecture`


![model_architecture](https://user-images.githubusercontent.com/106902414/175518828-d11a8cd3-31d4-4679-8114-c45cda54ec67.png)

`Model Analysis`

![graph](https://user-images.githubusercontent.com/106902414/175519182-a69faaa9-2d0c-41bb-979d-d14c5b6c2ed2.png)


`Model Evaluation`

![The error values](https://user-images.githubusercontent.com/106902414/175519137-f3ee6ba5-5425-4e35-9276-74008f3b7deb.PNG)



`Training Data`: Mape vs Loss

![Loss vs Mape](https://user-images.githubusercontent.com/106902414/175518873-d8cd9321-3c5c-422f-84a4-7c7a271bc2f3.PNG)



`Tensor Board`



![tensorboard](https://user-images.githubusercontent.com/106902414/175519202-ebb5db7e-0ab8-4baa-a6bc-6dd95fdde840.PNG)



### Discussion
1) The result produced is quite good which is MAPE is less than 1%
2) The model can predict well based on the accuracy produced
3) The data preprocessing involved is only fill the Nan using interpolation of data: `df.interpolate`
4) The drop out rate is being decrease to increase the accuracy
5) Also the number of epochs is being increase when lowered the dropout rate
6) Final result, the model is being trained with <=64 number of node in each layer,only 1 LSTM layer and 1 Dense layer

*Suggestions to Improve the Performance of Model*

1) Collect more training data
2) Make sure no extreme values in the dataset
3) Increase the complexity of the model layer
4) Used correct number of window size

### Credits
`You can load the dataset from here`
GitHub - MoH-Malaysia/covid19-public: Official data on the COVID-19 epidemic in Malaysia. Powered by CPRC, CPRC Hospital System, MKAK, and MySejahtera.
https://github.com/MoH-Malaysia/covid19-public



