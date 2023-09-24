import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame, skipping the first row (header)
df = pd.read_csv('merged_mart_april_modified.csv', sep=',', skiprows=[0], names=['Date', 'User', 'Tweet'])

# Initialize an empty list to store parsed dates
parsed_dates = []

# Iterate through the 'Date' column and attempt to convert each value
for date_str in df['Date']:
    try:
        parsed_date = pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S%z')
        parsed_dates.append(parsed_date)
    except ValueError:
        # Handle cases where the conversion fails (e.g., non-datetime values)
        parsed_dates.append(None)  # You can choose to replace with None or handle differently

# Replace the 'Date' column in the DataFrame with the parsed dates
df['Date'] = parsed_dates

# Convert 'Date' column to datetime with explicit format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S%z')

# Extract year, month, day, and hour from 'Date'
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Hour'] = df['Date'].dt.hour

# Group the data by date and count the number of posts per day
daily_counts = df.groupby(df['Date'].dt.date)['Date'].count()

# Create a time series plot
plt.figure(figsize=(20, 10))
plt.plot(daily_counts.index, daily_counts.values)
plt.xlabel('Datum')
plt.ylabel('Broj objava')
plt.title('Vremenska analiza frekvencije objava')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()