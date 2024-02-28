import json


def get_films(f_path:str = "app/data/films.json") -> list:
    with open(f_path) as file:
        data = json.load(file)
        films = data.get("films")
        return films


def grt_films():
    ""


if __name__ == "__main__":
    print(get_films())
