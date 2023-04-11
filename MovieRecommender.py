# code example
movies_watched = ["The Matrix", "Inception", "Blade Runner"]
genres = ["sci-fi", "action"]
mood = "adventurous"

recommended_movies = ["Interstellar", "Alien", "Mad Max: Fury Road"]

if mood == "adventurous":
    recommended_movies.append("Indiana Jones and the Raiders of the Lost Ark")
if "sci-fi" in genres:
    recommended_movies.append("The Terminator")
if "action" in genres:
    recommended_movies.append("Die Hard")

for movie in recommended_movies:
    if movie not in movies_watched:
        print(movie)
