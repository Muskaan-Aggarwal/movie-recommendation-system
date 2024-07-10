# Create a nearest neighbors model
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)

# Fit the model to the sparse matrix
knn.fit(X)