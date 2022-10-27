class Series:
    def __init__(self, title: str, seasons: int, genre: list,):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.rate_list = []
        
    def rate(self, rating: int):
        if rating >= 0 or rating <= 5:
            self.rate_list.append(rating)
    
    def __str__(self):
        genre_string = ", ".join(self.genre)
        if len(self.rate_list) == 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"
        else:
            average = float(sum(self.rate_list)/len(self.rate_list))
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{len(self.rate_list)} ratings, average {str(round(average, 1))} points"
        

def minimum_grade(rating: float, series_list: list):
    minimum_grade = []
    for serie in series_list:
        if sum(serie.rate_list)/len(serie.rate_list) >= rating:
            minimum_grade.append(serie)
    return minimum_grade

def includes_genre(genre: str, series_list: list):
    includes_genre = []
    for serie in series_list:
        if genre in serie.genre:
            includes_genre.append(serie)
    return includes_genre
    
            
if __name__ == "__main__":   

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)