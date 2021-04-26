import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Size of TV',y='Average time spent')
        fig.show()

#get the data source

def getDataSource(data_path):
    size_of_tv=[]
    average_time_spent=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row['Size of TV']))
            average_time_spent.append(float(row['Average time spent']))

    return {'x':size_of_tv,'y':average_time_spent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])
    print('correlation',correlation[0,1])

def setup():
    data_path='F:\python\class\C 106\Size of TV,_Average time spent watching TV in a week (hours).csv'
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()