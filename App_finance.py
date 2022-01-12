# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:01:03 2022


import streamlit as st
import yfinance as yf 
from datetime import date
import pandas as pd
from plotly import graph_objs as go

st.write("""Acompanhamento de ações Magazine Luiza""")
         
tickerSymbol = 'MGLU3.SA'

tickerData = yf.Tickers(tickerSymbol)


tickerDf = yf.download(tickers= tickerSymbol, period='1d', start='2010-5-30')


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












