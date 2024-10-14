import pandas as pd
import random
from flask import Flask, render_template, request

app = Flask(__name__)

def load_movies(file_path):
    """Load the MovieLens dataset."""
    df = pd.read_csv(file_path)
    print(f"Movies DataFrame: {df.head()}")  # Debug statement
    return df

def load_ratings(file_path):
    """Load the ratings dataset."""
    df = pd.read_csv(file_path)
    print(f"Ratings DataFrame: {df.head()}")  # Debug statement
    return df

def get_popular_movies_by_genre(movies_df, ratings_df, selected_genre):
    """Filter movies based on the selected genre and get 5 popular movies."""
    # Filter movies by genre
    filtered_movies = movies_df[movies_df['genres'].str.contains(selected_genre, case=False)]
    print(f"Filtered Movies: {filtered_movies.head()}")  # Debug statement

    # Merge with ratings to calculate popularity
    merged_df = filtered_movies.merge(ratings_df, on='movieId')
    print(f"Merged DataFrame: {merged_df.head()}")  # Debug statement

    # Calculate average rating and count of ratings
    popular_movies = (merged_df.groupby('movieId')
                      .agg({'rating': 'mean', 'userId': 'count'})
                      .rename(columns={'userId': 'number_of_ratings'})
                      .reset_index())
    
    # Sort by number of ratings (popularity) and get top 100
    top_movies = popular_movies.sort_values(by='number_of_ratings', ascending=False).head(100)
    
    # Get the corresponding titles for the top movieIds
    top_movie_titles = merged_df[merged_df['movieId'].isin(top_movies['movieId'])]

    # Drop duplicates based on 'title'
    unique_movies = top_movie_titles[['title', 'rating']].drop_duplicates(subset='title').reset_index(drop=True)

    # Randomly sample 5 movies from the top 100
    if len(unique_movies) >= 5:
        sampled_movies = unique_movies.sample(n=5, random_state=random.randint(1, 1000))
    else:
        sampled_movies = unique_movies  # Return all if less than 5

    return sampled_movies

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    # Load datasets
    movies_df = load_movies('data/movies.csv')
    ratings_df = load_ratings('data/ratings.csv')

    # Get popular movies for the selected genre
    movies = get_popular_movies_by_genre(movies_df, ratings_df, genre)

    # Check if movies DataFrame is not empty
    if movies.empty:
        recommendations = None  # No recommendations if the DataFrame is empty
    else:
        recommendations = movies.to_dict(orient='records')  # Convert to dictionary for easier handling in the template

    return render_template('index.html', recommendations=recommendations, genre=genre)

if __name__ == "__main__":
    app.run(debug=True)
