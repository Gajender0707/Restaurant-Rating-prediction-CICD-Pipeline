from flask import Flask,render_template,request
from model_prediction import Prediction

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST":
        online_order=request.form.get("online_order")
        book_table=request.form.get("book_table")
        votes=request.form.get("votes")
        rest_type=request.form.get("rest_type")
        cost=request.form.get("cost")
        type=request.form.get("type")
        city=request.form.get("city")
        model_prediction_obj=Prediction(
            online_order=online_order,
            book_table=book_table,
            votes=votes,
            rest_type=rest_type,
            cost=cost,
            type=type,
            city=city)
        model_path=r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\model.pkl"
        preprocessor_path=r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Restaurant-Rating-Prediction\Artifacts\Preprocessor.pkl"
        output=model_prediction_obj.Predict_rating(model_path=model_path,preprocessor_path=preprocessor_path)
        def rating_star(rate):
            if rate==2:
                return "⭐⭐"
            elif rate==3:
                return "⭐⭐⭐"
            elif rate==4:
                return "⭐⭐⭐⭐"
            elif rate==5:
                return "⭐⭐⭐⭐⭐"
            else:
                return "⭐"
        
        pred=rating_star(output)
        return render_template("home.html",pred=pred)
    else:
        return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
