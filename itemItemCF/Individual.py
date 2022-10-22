import pandas as pd # Data processing
import seaborn as sns # Visualization

ratings_cols = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv("C:\\Users\\Jegadit\\Desktop\\root\\college\\projects\\ML\\RecommendationSystem\\ml-100k\\u.data", sep="\\t", names=ratings_cols, encoding="latin-1")

'''print('The dataset has', ratings['user_id'].nunique(), 'unique users') # Number of users
print('The dataset has', ratings['movie_id'].nunique(), 'unique movies') # Number of movies
print('The dataset has', ratings['rating'].nunique(), 'unique ratings') # Number of ratings
print('The unique ratings are', sorted(ratings['rating'].unique())) # List of unique ratings'''

movies_cols = [ "movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL", 
            "unknown", "Action", "Adventure", "Animation",
            "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
            "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
            "Thriller", "War", "Western"]
movies = pd.read_csv("C:\\Users\\Jegadit\\Desktop\\root\\college\\projects\\ML\\RecommendationSystem\\ml-100k\\u.item", sep="|", names=movies_cols)

df = pd.merge(ratings, movies, on='movie_id')


# IGNORE --------------------------------------------------------------------------------------------------------------------------------------
# filter the movies and keep only those with over 50 ratings for the analysis
agg_ratings = df.groupby('movie_title').agg(mean_rating = ('rating', 'mean'), number_of_ratings = ('rating', 'count')).reset_index()
agg_ratings_GT100 = agg_ratings[agg_ratings['number_of_ratings']>50]
agg_ratings_GT100.sort_values(by='number_of_ratings', ascending=False)
df_GT100 = pd.merge(df, agg_ratings_GT100[['movie_title']], on='movie_title', how='inner')
'''print('The ratings dataset has', df_GT100['user_id'].nunique(), 'unique users') # Number of users
print('The ratings dataset has', df_GT100['movie_id'].nunique(), 'unique movies') # Number of movies
print('The ratings dataset has', df_GT100['rating'].nunique(), 'unique ratings') # Number of ratings
print('The unique ratings are', sorted(df_GT100['rating'].unique())) # List of unique ratings'''
# END IGNORE -----------------------------------------------------------------------------------------------------------------------------------

matrix = df_GT100.pivot_table(index='movie_title', columns='user_id', values='rating')
matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 0)
item_similarity = matrix_norm.T.corr()

picked_userid = 42 # Pick a user
picked_movie = 'Terminator 2: Judgment Day (1991)' # Pick a movie
# Movies that the target user has watched
picked_userid_watched = pd.DataFrame(matrix_norm[picked_userid].dropna(axis=0, how='all').sort_values(ascending=False)).reset_index().rename(columns={picked_userid:'rating'})

picked_movie_similarity_score = item_similarity[[picked_movie]].reset_index().rename(columns={picked_movie:'similarity_score'})
# Rank the similarities between the movies user has rated and the movie chosen.
picked_userid_watched_similarity = pd.merge(left=picked_userid_watched, right=picked_movie_similarity_score, on='movie_title', how='inner').sort_values('similarity_score', ascending=False)[:10]

#print(picked_userid_watched_similarity)
print(picked_userid_watched_similarity[['movie_title','similarity_score']])