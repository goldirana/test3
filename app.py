#%% creating app that will fetch the data and display on heroku
from flask import *
import pandas as pd

app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_csv("https://raw.githubusercontent.com/goldirana/nseindia/master/BM_All_Forthcoming_-_F%26O_Securities.csv")
    # tabel = data.head()
    return data.to_html()

if __name__ =="__main__":
    app.run(debug=True)



