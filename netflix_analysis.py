import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Basic Information
print(df.head())
print(df.shape)
print(df.info())

# Missing Values
print(df.isnull().sum())

# Data Cleaning
df.drop_duplicates(inplace=True)

df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# Movies vs TV Shows
print(df['type'].value_counts())

sns.countplot(data=df, x='type')
plt.title("Movies vs TV Shows")
plt.show()

# Top Countries
countries = (
    df['country'].str.split(',')
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

countries.plot(kind='bar')
plt.title("Top 10 Countries")
plt.show()

# Top Genres
genres = (
    df['listed_in'].str.split(',')
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

genres.plot(kind='barh')
plt.title("Top 10 Netflix Genres")
plt.show()

# Year-wise Content
yearly = df['release_year'].value_counts().sort_index()

yearly.plot(figsize=(10,5))
plt.title("Netflix Content by Release Year")
plt.show()

print("Netflix Analysis Completed!")
