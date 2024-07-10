def make_hybrid_recommendations(user_id, movie_id, num_recommendations):
    # Get the collaborative filtering recommendations
    cf_recommendations = make_recommendations(user_id, num_recommendations)

    # Get the content-based filtering recommendations
    cbf_recommendations = make_content_based_recommendations(movie_id, num_recommendations)

    # Combine the recommendations
    hybrid_recommendations = list(set(cf_recommendations) & set(cbf_recommendations))

    # Return the hybrid recommendations
    return hybrid_recommendations