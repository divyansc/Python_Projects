from http.client import responses

import streamlit as st
import pandas as pd
from datetime import datetime
import requests
from unicodedata import category

API_URL = "http://localhost:8000"

def analytics_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date",datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End Date",datetime(2024,8,5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/",json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total":[response[category]['total'] for category in response],
            "Percentage":[response[category]['percentage'] for category in response]
               }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Total",ascending=True)

        st.title("Expense Breakdown by Category")
        st.bar_chart(data=df_sorted.set_index("Category")['Total'],width=0,height=0,use_container_width=10)

        df_sorted['Total'] = df_sorted['Total'].map("{:.2f}".format)
        df_sorted['Percentage'] = df_sorted['Percentage'].map("{:.2f}".format)

        st.table(df_sorted)

        # st.write(response)