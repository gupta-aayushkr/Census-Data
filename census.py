import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


def generate_ai_data():
    data = {
        'State': np.random.choice(['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
                                   'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
                                   'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                   'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
                                   'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'], size=20),
        'City': np.random.choice(['Lucknow', 'Kanpur', 'Varanasi', 'Agra', 'Allahabad (Prayagraj)', 'Ghaziabad',
                                  'Noida', 'Meerut', 'Bareilly', 'Aligarh', 'Gorakhpur', 'Moradabad', 'Saharanpur',
                                  'Jhansi', 'Mathura', 'Firozabad', 'Ayodhya (Faizabad)'], size=20),
        'Ward': np.random.choice(['नगर निगम जोन 1 लखनऊ', 'नगर निगम जोन 2 लखनऊ', 'नगर निगम जोन 3 लखनऊ',
                                   'नगर निगम जोन 4 लखनऊ', 'नगर निगम जोन 5 लखनऊ', 'नगर निगम जोन 6 लखनऊ',
                                   'नगर निगम जोन 7 लखनऊ', 'नगर निगम जोन 8 लखनऊ'], size=20),
        'Age': np.random.randint(18, 60, size=20),
        'Sex': [random.choice(['Male', 'Female']) for _ in range(20)],
        'Gender': [random.choice(['M', 'F']) for _ in range(20)]
    }
    return pd.DataFrame(data)


people_data = generate_ai_data()

st.title('People Analytics App')

st.subheader('Data')

st.dataframe(people_data)



st.subheader('Filtered')
st.sidebar.header('Filters')


selected_state = st.sidebar.selectbox('Select State:', people_data['State'].unique())
selected_city = st.sidebar.selectbox('Select City:', people_data[people_data['State'] == selected_state]['City'].unique())
selected_ward = st.sidebar.selectbox('Select Ward:', people_data[people_data['City'] == selected_city]['Ward'].unique())


filtered_data = people_data[(people_data['State'] == selected_state) & 
                            (people_data['City'] == selected_city) & 
                            (people_data['Ward'] == selected_ward)]

st.dataframe(filtered_data, width=1000)

# st.sidebar.subheader('Filtered Data')

# st.sidebar.dataframe(filtered_data)


st.header('People Analytics Visualizations')


st.subheader('Gender Distribution')
st.write('This graph shows the distribution of gender among buyers.')
gender_count_plot = sns.countplot(x='Gender', data=people_data)
st.pyplot(gender_count_plot.figure)


# st.subheader('Age Distribution')
# st.write('This graph shows the distribution of buyers across different age groups.')
# age_distribution_plot = sns.histplot(x='Age', data=people_data, bins=20, kde=True)
# st.pyplot(age_distribution_plot.figure)


thresholds = [20, 30, 40]
for age_threshold in thresholds:
    above_threshold = people_data[people_data['Age'] > age_threshold]
    st.subheader(f'Number of People Above {age_threshold} years old')
    st.bar_chart(above_threshold['Age'].value_counts())


st.header('Summary Statistics')
st.dataframe(people_data[['Age', 'Sex']].describe(), width=1000)