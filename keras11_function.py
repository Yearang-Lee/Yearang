# 1. 데이터
import numpy as np
x = np.array([range(1,101), range(101,201), range(301,401)])   # (3, 100)
y = np.array([range(101,201)])                                 # (1, 100)
# y2 = np.array(range(101,201))   # (100, )

# print(x.shape)  
# print(y.shape)  
# print(y2.shape)

x = np.transpose(x)   # (100, 3)
y = np.transpose(y)   # (100, 1)

print(x.shape)  
print(y.shape)  


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.6, random_state = 66, shuffle=False)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size = 0.5, random_state = 66, shuffle=False)

# print(x_train)
# print(x_val)
# print(x_test)

# 2. 모델 구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
# model = Sequential()

# 함수형 모델 : 먼저 모델을 구성하고 이 모델이 함수형 모델이라는 것을 제일 나중에 명시한다.
# input1 = Input(shape=(3,))
# dense1 = Dense(5)(input1)
# dense2 = Dense(2)(dense1)
# dense3 = Dense(3)(dense2)
# output1 = Dense(1)(dense3)

# hiden layer 부분은 변수 명을 아무거나 해도 된다.
input1 = Input(shape=(3,))
x = Dense(5)(input1)
x = Dense(2)(x)
x = Dense(3)(x)
output1 = Dense(1)(x)

model = Model(inputs = input1, outputs = output1)


#model.add(Dense(5, input_dim=3))
# model.add(Dense(5, input_shape=(3, )))    
# model.add(Dense(2))
# model.add(Dense(3))
# model.add(Dense(1))                     

model.summary()

        
# 3. 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mse'])  
model.fit(x_train,y_train, epochs=500, batch_size=1, validation_data=(x_val, y_val))  

# 4. 평가예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1)
print('acc : ', mse)

x_pred = np.array([[201,202,203],[204,205,206],[207,208,209]])  
x_pred = np.transpose(x_pred)
p = model.predict(x_pred, batch_size=1)
print(p)

y_predict = model.predict(x_test, batch_size=1)


# RMSE 구하기 
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test,y_predict))
print('RMSE :', RMSE(y_test,y_predict))

# R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test,y_predict)
print("R2 : ",r2_y_predict)
