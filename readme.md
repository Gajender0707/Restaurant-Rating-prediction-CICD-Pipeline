# Zomato Bangalore Restaurants
### A End to  End project using CICD pipeline which will predict rating of the restaurant⭐⭐⭐.
![image](https://user-images.githubusercontent.com/92681972/233918490-f22e93c9-49fa-40a8-8e76-ad996c29be70.png)
## 📝 Table of contents
* [General info](#general-info)
* [Data Source](#data-source)
* [Problem Statement](#Problem-Statement)
* [Demo Photos](#demo-photos)
* [Library Used](#Library-Used)
* [Structure Used](#structure-used)
* [Run Locally](#Run-Locally)
* [Deployment Techniques](#deployment-Techniques)

***
## General info
Bengaluru is one of India's major cities, renowned for its vibrant culture, diverse cuisine, and vibrant nightlife. With its bustling restaurant scene, it's no wonder that locals and tourists alike flock to the city to experience the gastronomical delights on offer.
To better understand the culinary landscape of Bengaluru, an exploratory data analysis was conducted on the restaurants listed on Zomato, a popular restaurant search and discovery platform. The data was analyzed to uncover key trends in the restaurant industry, such as the most popular cuisines and pricing, as well as the most popular restaurants and their ratings. Additionally, the analysis explored geographic trends in the restaurant industry, including the most popular neighbourhoods and restaurant types.
***
## ⏳Data Source
[Zomato Bangalore Restaurants](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants)
***
## Problem Statement
To predict the rating of the restaurant.
***
## 📷Demo Photos
<img width="1006" alt="tour_package" src="https://user-images.githubusercontent.com/92681972/232985096-7026b3ec-d469-442b-beb4-f5209d08acf9.png">
 Our Website will be look like and when we hit the submit button prediction will happen. adn output will be that customer will take the package or customer will not the package.
 
 ##Library Used
 There will be file named requirement.txt which will contain all these libraries used in project.
 ```
 pandas
numpy
seaborn
matplotlib
scikit-learn
xgboost
flask
dill
 ```
*** 
 ## ⚙️Structure Used
 ### There are structure used for different-different work:
 * ```setup.py```This contains all details about the Project.
 * ```requirements.txt``` Contains the all the libraries used in the project.
 * ```logger.py``` is responsible for the log all the information whatever is happening in the project at which perticular time or file.
 * ```exception.py``` is responsible for the give the Customexception when an error in any file, So it give the file_name,Lineno and error also.
 * ```.gitignore``` will add all the files which we don't want to push on the github.
 * ```readme.md``` contain general informtion about the project steps and requiremnts for further explaination.
 * ```data```contain the dataset.
 * ```src``` contain many subfolder. we need to give a ```__init__.py``` file in each directory i.e. we can use each file as a module.
 * ```src/data_ingestion.py``` responsible for the data ingestion from many different-different source like  ***kaggle*** ,***mongodb*** or ***MySQL*** etc. it split the data into train and test and store them in a perticular ```Artifacts``` folder.
 * ```src/data_transformation.py```responsible for the transform the categorical values into vectors. Also used in Scaling and Handle the Missing values and return a preprocessor which transform the data for the ***Machine Learning Models***.
 * ```src/Model_trainer.py``` is responsible for the model training and Hyperparameter tuning it return a Model Pickle file which is train on the data and used for the further Prediction.
 * ```src/Prediction_Pipeline.py``` is responsible for the Creating the Pipeline using the ```app.py``` and ```utils.py``` for the Creating a Web Page for the prediction for the new data.
 * ```utils.py``` is used for creating and storing the common function which are used whole through out the Project.
 * ```app.py``` is web app file which interact with user and take the input for new datapoints from the user and show the output by using the pre-trained model.
 

## 👨🏻‍💻Run Locally
* Before the following steps make sure you have git, Anaconda or miniconda installed on your system
* Clone the complete project with git clonehttps://github.com/Gajender0707/Travel-Package-Project-using-CICD-Pipeline.git or you can just download the code and unzip it.
* Once the project is cloned, open VSCode prompt in the directory where the project was cloned and paste the following block ```python venv -m myenv python=3.11.3``` after that 
* ```myenv/Scripts/Activate.ps1```
* ```pip install -r requirements.txt``` And finally run the project with ```python app.py```.
* Open the localhost url provided after running app.py and now you can use the project locally in your web browser or put ```http://127.0.0.1:5000``` which is your local host.

## Deployment Techniques
* Deployment to AWS: The final step is to deploy the All files to an AWS server. This step is done by us using the ubuntu server where we deployed our model using the winSCP to connect the AWS server(EC2).

## 🎯Project Created BY
[@Gajender](https://linkedin.com/in/gajender07)
