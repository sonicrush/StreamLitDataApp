import streamlit as streamlit
import pandas as pandas
import plotly.express as px
from apis import get_apod


#In terminal, run :streamlit run dashboard.py
streamlit.title("Water Quality Dashboard")

streamlit.header("Intership Software Ready Dev")

streamlit.subheader("Prof. Gregory Reis")
streamlit.divider()


tab1, tab2, tab3, tab4 = streamlit.tabs(
    ["Descriptive Statistics",
     "2d Plots",
     "3d Plots",
     "NASA APOD"
     ]
)


dataframe = pandas.read_csv("biscayneBay_waterquality.csv")


with tab1:
    streamlit.info("In progress")
    streamlit.dataframe(dataframe)
    streamlit.caption("Raw Data")
    streamlit.divider()
    streamlit.dataframe(dataframe.describe())
    streamlit.caption("Descriptive Statistics")

with tab2:
    streamlit.info("In progress")
    figure1 = px.line(dataframe,
                      x="Time",
                      y="Temperature (c)")
    streamlit.plotly_chart(figure1)

    figure2 = px.scatter(dataframe,
                         x="ODO mg/L",
                         y="Temperature (c)",
                         color = "pH")
    streamlit.plotly_chart(figure2)

with tab3:
    streamlit.success("It's worth the wait")
    figure3 = px.scatter_3d(dataframe,
                            x="Longitude",
                            y="Latitude",
                            z="Total Water Column (m)",
                            color="Temperature (c)"
                            )
    figure3.update_scenes(zaxis_autorange="reversed")
    streamlit.plotly_chart(figure3)

with tab4:
    streamlit.title("Astronomy Picture of the Day")
    apodDictionary = get_apod()
    streamlit.subheader(apodDictionary["title"])
    streamlit.image(apodDictionary["url"])
    streamlit.caption(apodDictionary["date"] + "\t" + apodDictionary["url"])
    streamlit.text(apodDictionary["explanation"])
    streamlit.divider()




