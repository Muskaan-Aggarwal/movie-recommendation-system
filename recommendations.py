def make_recommendations(user_id, num_recommendations):
    # Get the user's ratings
    user_ratings = ratings_pivot.loc[user_id]

    # Get the nearest neighbors
    distances, indices = knn.kneighbors(user_ratings.values.reshape(1, -1), n_neighbors=num_recommendations+1)

    # Get the recommended movie IDs
    recommended_movie_ids = ratings_pivot.columns[indices[0][1:]]

    # Return the recommended movie IDs
    return recommended_movie_ids