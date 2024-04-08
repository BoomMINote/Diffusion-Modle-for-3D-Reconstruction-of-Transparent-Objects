import numpy as np 
data1 = np.load("./npy/data1.npy")
data2 = np.load("./npy/data2.npy")
data3 = np.load("./npy/data3.npy")
data4 = np.load("./npy/data4.npy")
data5 = np.load("./npy/data5.npy")
data6 = np.load("./npy/data6.npy")
data7 = np.load("./npy/data7.npy")
data8 = np.load("./npy/data8.npy")

label1 = np.load("./npy/label1.npy")
label2 = np.load("./npy/label2.npy")
label3 = np.load("./npy/label3.npy")
label4 = np.load("./npy/label4.npy")
label5 = np.load("./npy/label5.npy")
label6 = np.load("./npy/label6.npy")
label7 = np.load("./npy/label7.npy")
label8 = np.load("./npy/label8.npy")

all_data  = np.concatenate([data1,data2,data3,data4,data5,data6,data7,data8],axis=0)
np.save("data.npy",all_data)
all_label = np.concatenate([label1,label2,label3,label4,label5,label6,label7,label8],axis=0)
np.save("label.npy",all_label)
print(all_data.shape,all_label.shape)


