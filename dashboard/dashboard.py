import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')
# Prepare day_df data
day_df = pd.read_csv("dashboard/day.csv")
day_df.head()

# Remove unnecessary columns
day_df.drop(columns='windspeed', inplace=True)

# Rename column headers
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weathearCondition',
    'cnt': 'count'
}, inplace=True)

day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weathearCondition'] = day_df['weathearCondition'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Prepare daily rental dataframe
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dateday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

# Prepare daily casual rental dataframe
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dateday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Prepare daily registered rental dataframe
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dateday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Prepare seasonal rental dataframe
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Prepare weekday rental dataframe
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Prepare working day rental dataframe
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Prepare holiday rental dataframe
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Prepare weather rental dataframe
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weathearCondition').agg({
        'count': 'sum'
    })
    return weather_rent_df

# Create filter components
min_date = pd.to_datetime(day_df['dateday']).dt.date.min()
max_date = pd.to_datetime(day_df['dateday']).dt.date.max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Get start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Date Range',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dateday'] >= str(start_date)) & 
                (day_df['dateday'] <= str(end_date))]

# Prepare various dataframes
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
# monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# DASHBOARD
# Create title
st.header('Bike Rental Dashboard 🚲')

# Create daily rental metrics
st.subheader('Daily Rentals')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)

with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)


st.markdown(""" 
### The most enjoyed season for bike users, both Casual and Registered
This is indicated by the high number of bike rentals carried out by both casual users
and registered users, where autumn has the most enthusiasts, followed by summer, winter, and spring.

""")
# Create rental counts by season

# Create rental counts by season
st.subheader('Seasonly Rentals')

# Custom visualization based on provided code
seasonal_usage = main_df.groupby('season')[['registered', 'casual']].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.4
x = range(len(seasonal_usage['season']))

# Plotting registered users
ax.bar(
    [pos - bar_width / 2 for pos in x],
    seasonal_usage['registered'],
    width=bar_width,
    label='Registered',
    color='steelblue'
)

# Plotting casual users
ax.bar(
    [pos + bar_width / 2 for pos in x],
    seasonal_usage['casual'],
    width=bar_width,
    label='Casual',
    color='salmon'
)

# Adding labels and legends
ax.set_xlabel('Season', fontsize=12)
ax.set_ylabel('Total Rentals', fontsize=12)
ax.set_title('Total Bike Rentals by Season', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(seasonal_usage['season'], fontsize=10)
ax.legend()

st.pyplot(fig)

#Visual 2
st.subheader('Seasonly Rentals')

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x='season',
    y='registered',
    data=season_rent_df,
    label='Registered',
    color='tab:blue',
    ax=ax
)

sns.barplot(
    x='season',
    y='casual',
    data=season_rent_df,
    label='Casual',
    color='tab:cyan',
    ax=ax
)

for index, row in season_rent_df.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)


st.markdown(""" 
### The factor of weather conditions in determining the level of bike rentals by users.
Based on the chart below, it can be observed that weather conditions play a significant role
in the interest of renters when it comes to bike rentals. Good weather offers a greater opportunity 
for renters to engage in rentals compared to less favorable weather conditions. The data below shows 
that renters tend to rent bikes during clear or partly cloudy weather, whereas no rentals occur during poor weather conditions.
However, overcast weather still attracts some renters, followed by snowy or rainy weather, which has a relatively smaller 
number of renters.

""")
# Create rental counts by weather condition
st.subheader('Weatherly Rentals')

fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:blue", "tab:orange", "tab:green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['count'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(weather_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)


st.markdown(""" 
### The difference in bike rental counts between weekdays and weekends
Based on the data below, it can be observed that weekdays tend to have higher rental rates compared to weekends.
This could be influenced by several factors. Notably, Friday shows the highest rental interest compared to the weekend.

""")
# Create rental counts by weekday, working day and holiday
st.subheader('Weekday, Workingday, and Holiday Rentals')

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15,10))

# Colors customized to match Jupyter code
palette_workingday = 'Blues'    
palette_holiday = 'Greens'      
palette_weekday = 'Oranges'     

# Based on working day
sns.barplot(
    x='workingday',
    y='count',
    data=workingday_rent_df,
    palette=palette_workingday,
    ax=axes[0])

for index, row in enumerate(workingday_rent_df['count']):
    axes[0].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[0].set_title('Number of Rents based on Working Day')
axes[0].set_ylabel(None)
axes[0].tick_params(axis='x', labelsize=15)
axes[0].tick_params(axis='y', labelsize=10)

# Based on holiday
sns.barplot(
    x='holiday',
    y='count',
    data=holiday_rent_df,
    palette=palette_holiday,
    ax=axes[1])

for index, row in enumerate(holiday_rent_df['count']):
    axes[1].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[1].set_title('Number of Rents based on Holiday')
axes[1].set_ylabel(None)
axes[1].tick_params(axis='x', labelsize=15)
axes[1].tick_params(axis='y', labelsize=10)

# Based on weekday
sns.barplot(
    x='weekday',
    y='count',
    data=weekday_rent_df,
    palette=palette_weekday,
    ax=axes[2])

for index, row in enumerate(weekday_rent_df['count']):
    axes[2].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[2].set_title('Number of Rents based on Weekday')
axes[2].set_ylabel(None)
axes[2].tick_params(axis='x', labelsize=15)
axes[2].tick_params(axis='y', labelsize=10)

plt.tight_layout()
st.pyplot(fig)

st.caption('Copyright (c) Lywen Chandra 2025')