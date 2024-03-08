from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import pip 

def reemplazos(v):
  v=str(v)
  v=v.replace(',','')
  return v

pip.main(['install', 'plotly_express'])
pip.main(["install","openpyxl"])

st.title("FUNNEL Y TRACKING DE INVER+")
st.text('La presente página permite visualizar el comportamiento generalizado de los socios en la aplicacion.')
#df=pd.read_excel('PROCESOS_PIVOTE.xlsx')

#df_2=pd.read_csv('APROBADOS.csv')
#st.write(df_2)

st.markdown(f' FUNNEL')
df=pd.read_csv('FUNEL (1).csv',encoding='latin-1')
#fig = px.funnel(data, x='number', y='stage')
#st.ploty_chart(fig)
#fig.show()
#st.image('FUNNEL.png',caption='ACTIVIDAD REGISTRADA PARA CADA UNA DE LAS PANTALLAS')
#data = dict(
 #   number=[39, 27.4, 20.6, 11, 2],
  #  stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig = px.funnel(df, x=df['FRECUENCIA'], y=df['PASO'])
st.plotly_chart(fig)


st.markdown(f' AFLUENCIA DIARIA EN EL UNBORDING 2.0')
chart_data = pd.read_csv('FECHAS (1).csv',encoding='latin-1')
chart_data = chart_data.drop('Unnamed: 0',axis=1)
chart_data = chart_data.set_index('FECHA')
st.bar_chart(chart_data)
#st.image('BARRAS.png',caption='EVOLUCION DE LA ACTIVIDAD')

st.text('Estos valores corresponden a los ingresos identificados en las siguientes ubicaciones.')
df=pd.read_csv('COORDENADAS (1).csv',encoding='latin-1')
df=df.rename(columns={'LATITUD':'lat','LONGITUD':'lon'})
chart_data = df

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=19.69816,
        longitude=-101.15816,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[0]',
            get_radius=200,
        ),
    ],
))

st.markdown(f' SISTEMA OPERATIVO')
df=pd.read_csv('SO (1).csv',encoding='latin-1')
df=df.drop('Unnamed: 0',axis=1)
st.text('Las visitas obtenidas corresponden al uso de los siguientes sistemas operativos.')
fig=px.pie(df, values='FRECUENCIA', names='SISTEMA')#,width=500,height=400)
st.plotly_chart(fig)

st.markdown(f' NAVEGADOR')
df=pd.read_csv('NAVEGADOR (1).csv',encoding='latin-1')
df=df.drop('Unnamed: 0',axis=1)
st.text('Como enfoque adicional se puede identificar el navegador implementado como se muestra a continuación.')
fig=px.pie(df,values='FRECUENCIA',names='NAVEGADOR',width=500,height=400)
#,width=500,height=400)
st.plotly_chart(fig)

