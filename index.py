import numpy as np
import matplotlib.pyplot as mp
import pandas as pd
from fungsi.sigmoid import sigmoid
from sklearn.utils import shuffle

#data pertama
#data delvin
#tinggi badan
x1 = np.array([18 + 1*np.random.randn() for i in range(1,100)])
#berat badan
x2= np.array([ + 1*np.random.randn() for i in range(1,100)])
#status delvin
y1 =  np.array([1 for i in range(1,100)])
#status nin
y2 =  np.array([0 for i in range(1,100)])
#label
lael = ["delvin" for i in range(1,100)]
data_delvin= {
    'x1': x1,
    'x2': x2,
    'y1': y1,
    'y2': y2,
    'label': lael
    
}
data_frame1 = pd.DataFrame(data=data_delvin)
x1 = np.array([1 + 1*np.random.randn() for i in range(1,100)])
#berat badan
x2= np.array([ + 18*np.random.randn() for i in range(1,100)])
#status delvin
y1 =  np.array([0 for i in range(1,100)])
#status nin
y2 =  np.array([1 for i in range(1,100)])
label = ["nin" for i in range(1,100)]
data_nin= {
    'x1': x1,
    'x2': x2,
    'y1': y1,
    'y2': y2,
    'label': label
    
}
data_frame2 = pd.DataFrame(data=data_nin)

data_frame = pd.concat([data_frame1,data_frame2])
data_frame = shuffle(data_frame)
data_frame = data_frame.reset_index(drop=True)
w12 = np.random.uniform(-0.01,0.01)
w11 = np.random.uniform(-0.01,0.01)
w21 =np.random.uniform(-0.01,0.01)
w22 = np.random.uniform(-0.01,0.01)

W = np.array([[w11,w12],[w21,w22]])
bias = np.random.uniform(-0.01,0.01)

learning_rate = 0.01
for i,baris in data_frame.iterrows():
    w_lama = W
    bias_lama = bias
    input = np.array([[baris.x1],[baris.x2]])
    output = np.dot(W,input) + bias_lama
    output_belajar = sigmoid(output)
    output_sebensrnya = np.array([[baris.y1],[baris.y2]])
    error = output_belajar - output_sebensrnya
    delta_w = np.dot(learning_rate * error * output_belajar * (1 - output_belajar), input.T)
    delta_bias = learning_rate * error * output_belajar * (1 - output_belajar)
    bias_baru = bias_lama - delta_bias
    bias = bias_baru
    W_baru = w_lama - delta_w
    W = W_baru
    tebakan = np.argmax(output_belajar)
    jawaban = np.argmax(output_sebensrnya)

    label_tebakan = "nin" if tebakan == 1 else "Delvin"

    print(f"index {i} , tebakan : {label_tebakan} , kebenaran : {baris.label}")

