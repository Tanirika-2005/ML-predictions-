import csv
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
from tkinter import *
import tkinter as tk
import tkinter as tk
pd.options.display.float_format = '${:,.2f}'.format
#start_date = '2021-01-01'
fh = open("btc2.csv","r",newline="\n")
read = csv.reader(fh)
l = []
for rec in read:
    l.append(rec)
eth_df = pd.DataFrame(l, columns =['Date', 'High',"Low","Open","Close","Volume","Adj_close"])
eth_df.tail()
eth_df.info()
eth_df.isnull().sum()
eth_df.columns
eth_df.reset_index(inplace=True)
eth_df.columns
df = eth_df[["Date", "Open"]]
new_names = {
            "Date": "ds", 
                "Open": "y",
                }
df.rename(columns=new_names, inplace=True)
df.tail()
print("the actual prices")
print(df)
# plot the open price
m = Prophet(
            seasonality_mode="multiplicative" 
            )
m.fit(df)
future = m.make_future_dataframe(periods = 100)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
print(forecast)
trace_open = go.Scatter(
    x = forecast["ds"],
    y = forecast["yhat"],
    mode = 'lines',
    line = {"color": "#f50505"}, 
    name="Forecast"
)
trace_high = go.Scatter(
    x = forecast["ds"],
    y = forecast["yhat_upper"],
    mode = 'lines',
    fill = "tonexty", 
    line = {"color": "#57b8ff"}, 
    name="Higher uncertainty interval"
)
trace_low = go.Scatter(
    x = forecast["ds"],
    y = forecast["yhat_lower"],
    mode = 'lines',
    fill = "tonexty", 
    line = {"color": "#57b8ff"}, 
    name="Lower uncertainty interval"
)
trace_close = go.Scatter(
    x = df["ds"],
    y = df["y"],
    name="Data values"
)
data = [trace_open,trace_high,trace_low,trace_close]
layout = go.Layout(title="BTC Stock Price Forecast",xaxis_rangeslider_visible=True)
fig = go.Figure(data=data,layout=layout)
import plotly.express as px
fig.write_image("file.pdf")
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("file.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
def export():
	header = ["ds", "yhat_lower", "yhat_upper", "yhat"]
	forecast.to_csv('output.csv', columns = header)
B=tk.Button(win,text="save to csv(output.csv)",command= export,fg = 'red',bg='white')
B.pack()
B.place(relx=0,rely=0, anchor='nw')
win.mainloop()

