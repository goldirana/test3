#%% creating app that will fetch the data and display on heroku
from flask import *
import pandas as pd

app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_csv("https://raw.githubusercontent.com/goldirana/nseindia/master/BM_All_Forthcoming_-_F%26O_Securities.csv",index_col="Symbol")
    df= pd.read_csv("https://raw.githubusercontent.com/goldirana/nseindia/master/CA_ALL_FORTHCOMING_-_F%26O_SECURITIES.csv", sep=",",index_col="Symbol")
    result = pd.concat([df, data],)
    
    result.fillna("-",inplace=True)
    return result.to_html()



if __name__ =="__main__":
    app.run(debug=True)



# %%
