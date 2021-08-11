import csv
import plotly_express as px
import numpy as np
with open('s.csv') as f:
    df=csv.DictReader(f)
  
    fig=px.scatter(df,x="Roll No",y="Marks In Percentage") 
    fig.show()   



def getdatasource(path):
    icesales=[]
    temp=[]
    with open (path) as f:
        df=csv.DictReader(f)
        for row in df:
            temp.append(float(row["Roll No"]))
            icesales.append(float(row["Marks In Percentage"]))

    return {"x": icesales,"y": temp}



def setup():
    path="s.csv"
    datasource=getdatasource(path)
    c=np.corrcoef(datasource["x"],datasource["y"])
    print(c[0,1])


setup()


    