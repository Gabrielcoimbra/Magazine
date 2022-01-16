
import streamlit as st
import yfinance as yf 
from datetime import date
#from fbprophet import Prophet
import pandas as pd
import numpy as np
from plotly import graph_objs as go



st.write("""
         
         ***Acompanhamento de ações 2Neuron***
         
         Magazine Luiza
         
         
         
         
         
         """)
         
tickerSymbol = 'MGLU3.SA'

tickerData = yf.Tickers(tickerSymbol)

number_stocks = 186494467.00

tickerDf = yf.download(tickers= tickerSymbol, period='1d', start='2010-5-30')

Last_ticker = tickerDf['Close'].iloc[-1]

Aquisition_price = number_stocks * Last_ticker*0.01

st.write("""
         
         ***Preço atual para aquisição de 1% da empresa***
         
    
         
         
         
         """, format(Aquisition_price,".2f"))



#tickerDf = tickerData.history(period='1d', start='2010-5-30', end ='2022-1-12')

#Grafico simples
#st.line_chart(tickerDf.Close)
#st.line_chart(tickerDf.Volume)


#Grafico complexo

st.subheader('Gráfico de preços fechamento')

fig = go.Figure()
fig.add_trace(go.Scatter(x=tickerDf.index,
                         y=tickerDf['Close'],
                         name = 'Preco Fechamento',
                         line_color='blue',))
fig.update_layout(
    height=500,
    title_text='Preço Fechamento')
    
    


fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=tickerDf.index,
                         y=tickerDf['Volume'],
                         name = 'Volume',
                         line_color='red'))
fig_2.update_layout(
    height=500,
    title_text='Volume')


st.plotly_chart(fig)
st.plotly_chart(fig_2)

#st.line_chart(tickerDf.Volume)












