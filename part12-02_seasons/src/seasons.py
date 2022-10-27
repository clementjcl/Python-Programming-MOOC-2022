def sort_by_seasons(items: list):
    def send_by_season(item: dict):
        return item["seasons"]
    new_list = sorted(items, key=send_by_season)
    return new_list
    



if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")