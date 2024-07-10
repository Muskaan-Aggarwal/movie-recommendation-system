# Split the data into training and testing sets
train_ratings, test_ratings = train_test_split(ratings, test_size=0.2, random_state=42)

# Create a pivot table of the training ratings
train_ratings_pivot = train_ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Convert the pivot table to a sparse matrix
X_train = csr_matrix(train_ratings_pivot.values)

# Fit the model to the training data
knn.fit(X_train)

# Make predictions on the testing data
predictions = []
for user_id in test_ratings.userId.unique():
    recommended_movie_ids = make_recommendations(user_id, 10)
    predictions.extend([(user_id, movie_id) for movie_id in recommended_movie_ids])

# Evaluate the model using mean squared error
mse = mean_squared_error(test_ratings, predictions)
print(f'MSE: {mse:.2f}')