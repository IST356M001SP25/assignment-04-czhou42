'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py
file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])

if file:
    file_type = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_type)
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    if st.toggle("Enable Data Filtering"):
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(df, 'object')

        if text_cols:
            filter_col = stcols[0].selectbox("Select column to filter", text_cols)
            if filter_col:
                vals = pl.get_unique_values(df, filter_col)
                val = stcols[1].selectbox("Select value to filter On", vals)
                df_show = df[df[filter_col] == val][selected_cols]
            else:
                df_show = df[selected_cols]
        else:
            st.warning("No suitable text columns for filtering.")
            df_show = df[selected_cols]
    else:
        df_show = df[selected_cols]

    st.subheader("Filtered Data")
    st.dataframe(df_show)
    st.subheader("Data Summary")
    st.dataframe(df_show.describe())

