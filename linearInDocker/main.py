import pickle
import numpy as np

def linear_pred(x):
    with open('my_lin_reg.pkl', 'rb') as my_lin_reg:
        lin_reg = pickle.load(my_lin_reg)
        result = lin_reg.predict(x.reshape(-1, 1))
        return result

import sys

# Импортируем Flask для создания API
from flask import Flask, request
# Инициализируем приложение Flask
name = 'main'
app = Flask(name)
# Создайте конечную точку API
@app.route('/predict')
def predict_lin_reg():
    # Считываем все необходимые параметры запроса
    X1 = request.args.get('x')
    x = np.array(X1.split(','))
    linear = np.array2string(linear_pred(x))
    return linear

if name == 'main':
    app.run(host='0.0.0.0')