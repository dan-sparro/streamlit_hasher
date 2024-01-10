# streamlit app for Sparro by Dan Baker

# imports

import streamlit as st
import pandas as pd
from hashlib import sha256

# h1
st.title('Hasher')

st.subheader('Upload CSV')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    data = pd.DataFrame(columns=['email', 'hashed_email'])
    df = pd.read_csv(uploaded_file)
    st.subheader('CSV Statistics')
    st.write(df.describe())
    st.subheader('Dataframe')
    st.write(df)
    for value in df['email']:
        hashed_email = sha256(value.encode()).hexdigest()
        row = {'email': value, 'hashed_email': hashed_email}
        data.loc[len(data)] = row
    st.subheader('Hashed Emails')
    @st.cache_data
    def convert_df(data):
        return data.to_csv().encode('utf-8')
    csv = convert_df(data)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='hashed_emails.csv',
        mime='text/csv'
    )
    st.dataframe(data)
else:
    st.info('Awaiting for CSV file to be uploaded.')