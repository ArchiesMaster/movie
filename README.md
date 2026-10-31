# Movie Recommender

A genre-based movie discovery app built with Python, Flask and pandas. Choose a genre to receive up to five randomly selected titles from the most-rated movies in that category, using MovieLens data.

This project combines data filtering and aggregation with a browser interface built using HTML, CSS, JavaScript and Bootstrap.

## Features

- Clickable genre cards with icons
- Recommendations generated when a genre is selected
- Up to five movie suggestions per request
- Random sampling for variety across requests
- Browser local storage to remember and highlight the selected genre

## How recommendations work

1. Filter movies by the selected genre.
2. Join the matching movies with their ratings using `movieId`.
3. Count the ratings for each movie and select up to 100 with the most ratings.
4. Select up to five distinct movie titles at random from that pool.
5. Display the selected titles in the browser.

Popularity here means **number of ratings**, rather than highest average rating. Suggestions are based on the chosen genre and are not personalised to a user's viewing history.

## Technology

| Component         | Technology                                 |
| ----------------- | ------------------------------------------ |
| Web application   | Python and Flask                           |
| Data processing   | pandas                                     |
| Interface         | HTML, CSS and JavaScript                   |
| Styling and icons | Bootstrap 4, Font Awesome and Google Fonts |
| Dataset           | MovieLens                                  |

## Dataset acknowledgement

Movie and rating data are provided by [GroupLens Research](https://grouplens.org/datasets/movielens/) through the MovieLens datasets. Dataset usage is subject to the terms supplied with the specific download; those terms are separate from this project's code.

Reference: F. Maxwell Harper and Joseph A. Konstan. 2015. _The MovieLens Datasets: History and Context_. ACM Transactions on Interactive Intelligent Systems, 5(4), Article 19. https://doi.org/10.1145/2827872
