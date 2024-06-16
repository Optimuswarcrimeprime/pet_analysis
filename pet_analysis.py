# Importing necessary libraries
import pandas as pd  # For data manipulation
from datetime import datetime  # For date operations
import matplotlib.pyplot as plt  # For plotting histograms and bar charts
import seaborn as sns  # For advanced data visualization
import plotly.express as px  # For interactive plots

# Function to load data from a CSV file
def load_data(file_path):
    df = pd.read_csv(file_path)
    # Rename columns for better readability
    df.columns = ['Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature', 'Extra']
    # Drop the 'Extra' column as it's not needed
    df.drop(columns=['Extra'], inplace=True)
    # Add a 'PetID' column with unique IDs for each pet
    df.insert(0, 'PetID', range(1, len(df) + 1)) 
    # Print the first few rows of the DataFrame to show the loaded data
    print("Initial DataFrame with assigned columns:\n", df.head()) 
    return df

# Function to clean the data
def clean_data(df):
    # Drop rows with any missing values
    df.dropna(inplace=True)
    # Convert 'Price' column to numeric data type
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    # Convert 'Species' and 'SpecialFeature' columns to categorical data type
    df['Species'] = df['Species'].astype('category')
    df['SpecialFeature'] = df['SpecialFeature'].astype('category')
    # Convert 'Birthdate' column to datetime data type
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')
    # Calculate the age of each pet in years
    df['Age'] = (datetime.now() - df['Birthdate']).dt.days / 365.25 
    return df

# Function to calculate the average price of pets in a specific species
def calculate_average_price(df, species):
    species_df = df[df['Species'] == species]
    print(f"Filtered data for species '{species}':\n{species_df}") 
    return species_df['Price'].mean()

# Function to find pets with a specific special feature
def find_pets_with_feature(df, feature):
    feature_df = df[df['SpecialFeature'].str.contains(feature, case=False, na=False)]
    print(f"Filtered data for feature '{feature}':\n{feature_df}")  
    return feature_df['Name'].tolist()

# Function to get statistics (average price and average age) for each species
def get_species_statistics(df):
    species_stats = {}
    grouped = df.groupby('Species')
    for species, group in grouped:
        avg_price = group['Price'].mean()
        avg_age = group['Age'].mean()
        species_stats[species] = {'Average Price': avg_price, 'Average Age': avg_age}
    return species_stats

# Function to plot the distribution of prices using a histogram
def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Function to plot the average price by species using a bar chart
def plot_average_price_by_species(df):
    species_stats = df.groupby('Species')['Price'].mean().sort_values()
    species_stats.plot(kind='bar', figsize=(12, 6), color='skyblue')
    plt.title('Average Price by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Function to plot a scatter plot of price vs. age
def plot_price_vs_age(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='Price', color='skyblue')
    plt.title('Price vs. Age')
    plt.xlabel('Age')
    plt.ylabel('Price')
    plt.grid(axis='both', alpha=0.5)
    plt.show()

# Function to plot the distribution of ages for each species using a box plot
def plot_age_distribution_by_species(df):
    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species')
    fig.update_layout(xaxis_title='Species', yaxis_title='Age')
    fig.show()

