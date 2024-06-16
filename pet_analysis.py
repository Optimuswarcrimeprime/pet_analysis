import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = ['Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature', 'Extra']
    df.drop(columns=['Extra'], inplace=True)
    df.insert(0, 'PetID', range(1, len(df) + 1)) 
    print("Initial DataFrame with assigned columns:\n", df.head()) 
    return df

def clean_data(df):
    df.dropna(inplace=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Species'] = df['Species'].astype('category')
    df['SpecialFeature'] = df['SpecialFeature'].astype('category')
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')
    df['Age'] = (datetime.now() - df['Birthdate']).dt.days / 365.25 
    return df

def calculate_average_price(df, species):
    species_df = df[df['Species'] == species]
    print(f"Filtered data for species '{species}':\n{species_df}") 
    return species_df['Price'].mean()

def find_pets_with_feature(df, feature):
    feature_df = df[df['SpecialFeature'].str.contains(feature, case=False, na=False)]
    print(f"Filtered data for feature '{feature}':\n{feature_df}")  
    return feature_df['Name'].tolist()

def get_species_statistics(df):
    species_stats = {}
    grouped = df.groupby('Species')
    for species, group in grouped:
        avg_price = group['Price'].mean()
        avg_age = group['Age'].mean()
        species_stats[species] = {'Average Price': avg_price, 'Average Age': avg_age}
    return species_stats

def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_average_price_by_species(df):
    species_stats = df.groupby('Species')['Price'].mean().sort_values()
    species_stats.plot(kind='bar', figsize=(12, 6), color='skyblue')
    plt.title('Average Price by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_price_vs_age(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='Price', color='skyblue')
    plt.title('Price vs. Age')
    plt.xlabel('Age')
    plt.ylabel('Price')
    plt.grid(axis='both', alpha=0.5)
    plt.show()

def plot_age_distribution_by_species(df):
    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species')
    fig.update_layout(xaxis_title='Species', yaxis_title='Age')
    fig.show()
