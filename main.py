from prediction.data_preprocessing import preprocess
from prediction.model_training import train_model
from prediction.model_evaluation import evaluate_model,final_submission

Data="data/Student_Performance.csv"

def main():
    x_train,x_test,y_train,y_test=preprocess(Data)

    model=train_model(x_train,y_train)
    evaluate_model(model,x_train,y_train)
    
    y_pred=model.predict(x_test)

    
    final_submission(x_test,y_test,y_pred,output_path="submission.csv")

if __name__=="__main__":
    main()