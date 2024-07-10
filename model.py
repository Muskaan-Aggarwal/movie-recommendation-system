# Load the movie metadata
movies = pd.read_csv('movies_metadata.csv')

# Create a TF-IDF matrix of the movie metadata
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies['overview'])

# Create a cosine similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

def make_content_based_recommendations(movie_id, num_recommendations):
    # Get the movie's similarity scores
    similarity_scores = similarity_matrix[movie_id]

    # Get the recommended movie IDs
    recommended_movie_ids = np.argsort(-similarity_scores)[:num_recommendations+1]

    # Return the recommended movie IDs
    return recommended_movie_ids