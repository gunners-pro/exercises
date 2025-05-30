#ler e mostrar todas as linhas do arquivo cities
def show_cities():
    with open("cities.txt", encoding="utf-8") as cities:
        print(cities.read())

#conta o numero de linhas do arquivo cities
def count_lines():
    with open("cities.txt", encoding="utf-8") as cities:
        print(len(cities.readlines()))
        
#conta cidades que começam com a letra S
def count_cities_with_s():
    cities_started_with_s = []
    with open("cities.txt", encoding="utf-8") as cities:
        for city in cities.readlines():
            if city.startswith("S"):
                cities_started_with_s.append(city.replace("\n", ""))
    print(len(cities_started_with_s))

count_cities_with_s()