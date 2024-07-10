# Movie Recommendation System
## Overview
**This repository contains a movie recommendation system built using collaborative filtering and machine learning techniques in Python. The system uses a combination of user ratings and movie metadata to provide personalized movie recommendations.**

## Getting Started
### Prerequisites
1. Python 3.6 or later
2. scikit-learn 0.23 or later
3. pandas 1.1 or later
4. numpy 1.19 or later
5. scipy 1.5 or later
### Installation
1. Clone the repository: '**git clone https://github.com/Muskaan-Aggarwal/movie-recommendation-system.git**'
2. Install the required packages: '**pip install -r requirements.txt**'
### Running the System
1. Run the **data.py** script to train the model: **python data.py**
2. Run the **recommendations.py** script to make recommendations: **python recommendations.py --user_id <user_id> --num_recommendations <num_recommendations>**
## Dataset
The system uses the MovieLens dataset, which consists of:

1. 100,000 ratings from 600 users on 4,000 movies
2. Movie metadata, including titles, genres, and summaries
## Model Architecture
The system uses a combination of collaborative filtering and content-based filtering to provide recommendations.

1. Collaborative filtering: uses a nearest neighbors algorithm to find similar users and recommend movies based on their ratings
2. Content-based filtering: uses a TF-IDF matrix to find similar movies based on their metadata
## Performance
The system achieves a mean squared error of 0.85 on the testing set.

## Usage
To use the system, simply run the **recommendations.py** script and pass in the user ID and number of recommendations you want to receive. For example:
![Screenshot 2024-07-11 004637](https://github.com/Muskaan-Aggarwal/movie-recommendation-system/assets/146640075/3fdab84e-0834-4ae9-83a6-b8515d881b75)

The script will output a list of recommended movie IDs.

## Contributing
Contributions are welcome! If you'd like to contribute to the system or suggest improvements, please open an issue or submit a pull request.

## Acknowledgments
This system was developed using the following resources:

1. MovieLens dataset
2. Scikit-learn documentation
3. Pandas documentation
NumPy documentation
