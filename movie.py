# Just a quick little movie recommender script

movie_genres = {
    "The Matrix": "sci-fi",
    "Inception": "sci-fi",
    "Titanic": "romance",
    "John Wick": "action",
    "Avengers": "action",
    "The Notebook": "romance",
    "Interstellar": "sci-fi",
    "La La Land": "romance",
    "Mad Max": "action",
    "The Martian": "sci-fi"
}

def find_similar_movies(favorite):
    genre = movie_genres.get(favorite)
    if not genre:
        print(f"Never heard of '{favorite}'. Got another one?")
        return

    print(f"\nOh, you like '{favorite}'? Cool.")
    print(f"Here are some other {genre} flicks you might dig:")

    for title, g in movie_genres.items():
        if g == genre and title != favorite:
            print(f" - {title}")

try:
    movie = input("What's a movie you really liked recently? ").strip()
    find_similar_movies(movie)
except KeyboardInterrupt:
    print("\nNo worries, catch you later!")
