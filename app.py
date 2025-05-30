#ler e mostrar todas as linhas do arquivo cities
def show_cities():
    with open("cities.txt", encoding="utf-8") as cities:
        print(cities.read())

show_cities()