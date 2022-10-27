def find_movies(database: list, search_term: str):
    found_ones = []
    for movie in database:
        # The function lower() converts a string to lowercase
        # when this is done for both strings search is case insensitive
        if search_term.lower() in movie["name"].lower():
            found_ones.append(movie)
 
    return found_ones

if __name__ == "__main__":
    database = [
        {'name': 'The Birds 4', 'director': 'James Hitchcock', 'year': 2003, 'runtime': 119}, 
        {'name': 'The Godfather 4', 'director': 'Antero Coppola', 'year': 2022, 'runtime': 83}, 
        {'name': 'Jaws', 'director': 'Steven Spielberg', 'year': 1975, 'runtime': 124}, 
        {'name': 'Star Wars', 'director': 'George Lucas', 'year': 1977, 'runtime': 121}, 
        {'name': 'Lost in Translation 4', 'director': 'Soena Coppola', 'year': 2032, 'runtime': 120}]

    my_movies = find_movies(database, "4")
    print(my_movies)