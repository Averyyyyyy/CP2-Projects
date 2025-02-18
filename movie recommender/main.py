#Avery bowman, Movie Recommendation

import csv

# Function to load movies from a file
def load_movies(filename):
    movies = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Length"] = int(row["Length"])  # Convert movie length to integer
                movies.append(row)
    except FileNotFoundError:
        print("Error: File not found. Make sure the movie list file is in the same directory.")
    return movies

# Function to filter movies based on user input
def filter_movies(movies, filters):
    filtered_movies = movies
    if "genre" in filters:
        filtered_movies = [m for m in filtered_movies if filters["genre"].lower() in m["Genre"].lower()]
    if "director" in filters:
        filtered_movies = [m for m in filtered_movies if filters["director"].lower() in m["Director"].lower()]
    if "actor" in filters:
        filtered_movies = [m for m in filtered_movies if filters["actor"].lower() in m["Actors"].lower()]
    if "min_length" in filters and "max_length" in filters:
        filtered_movies = [m for m in filtered_movies if filters["min_length"] <= m["Length"] <= filters["max_length"]]
    return filtered_movies

# Function to get user filters
def get_filters():
    filters = {}
    print("\nChoose at least two filters for movie recommendations:")
    genre = input("Enter a genre (or press Enter to skip): ").strip()
    if genre:
        filters["genre"] = genre

    director = input("Enter a director's name (or press Enter to skip): ").strip()
    if director:
        filters["director"] = director

    actor = input("Enter an actor's name (or press Enter to skip): ").strip()
    if actor:
        filters["actor"] = actor

    length_range = input("Enter a time range (e.g., 90-120 for minutes, or press Enter to skip): ").strip()
    if length_range:
        try:
            min_length, max_length = map(int, length_range.split("-"))
            filters["min_length"] = min_length
            filters["max_length"] = max_length
        except ValueError:
            print("Invalid range format. Skipping length filter.")

    if len(filters) < 2:
        print("\nYou must select at least two filters.")
        return get_filters()
    
    return filters

# Function to display movie recommendations
def display_movies(movies):
    if not movies:
        print("\nNo movies found matching your criteria.")
    else:
        print("\nRecommended Movies:")
        for movie in movies:
            print(f"{movie['Title']} - {movie['Genre']} - {movie['Director']} - {movie['Length']} min - Starring: {movie['Actors']}")

# Main function
def main():
    filename = "movies.csv"  # Replace with the actual filename
    movies = load_movies(filename)
    
    if not movies:
        return
    
    while True:
        print("\nMovie Recommendation System")
        print("1. Get movie recommendations")
        print("2. Print full movie list")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            filters = get_filters()
            recommended_movies = filter_movies(movies, filters)
            display_movies(recommended_movies)

        elif choice == "2":
            display_movies(movies)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
