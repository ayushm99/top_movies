import pandas as pd

#path 
csv_path = '/Users/ayushmohanty/Documents/top_movies/top-500-movies.csv'

#creating df from csv data
df = pd.read_csv(csv_path, index_col=('rank'))

#prelim analysis
print(df.head())
print(df.tail())

