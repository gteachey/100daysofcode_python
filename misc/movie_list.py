# add movies to list
def add_movie(movies):
    title = input('Enter movie title: ')
    director = input('Enter movie director: ')
    year = int(input('Enter movie year: '))

    movies.append({
        'title': title,
        "director": director,
        "year": year
    })


# show all movies
def list_movies(movies):
    for movie in movies:
        print_movie(movie)


# find movies
def find_movie(movies):
    find_by = input('What do you want to search by? ')
    search_for = str(input('Enter what to search for: ').lower())

    results = find_by_attribute(movies, search_for, lambda x: x[find_by])

    list_movies(results)
    # for movie in movies:
    #     if search_for == movie['title'].lower():
    #         print_movie(movie)

    # return "Not Found"


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if str(finder(i)) == expected:
            found.append(i)

    return found


user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function(movies)
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


def print_movie(movie):
    print(f"Movie: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")


# Show menu, 'q' to quit the app
movies = []
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

menu()
