import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(data_path):
    data=pd.read_csv(data_path)
    return data

def feature_engineering(data):
    data['Extracurricular Activities']=data['Extracurricular Activities'].replace({
    'Yes':1,
    'No':0
    })
    return data

def feature_selection(data):
    x=data.drop(['Performance Index'],axis=1)
    y=data['Performance Index']

    return x,y

def preprocess(data_path):
    data=load_data(data_path)

    data=feature_engineering(data)
    x,y=feature_selection(data)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)

    return x_train,x_test,y_train,y_test