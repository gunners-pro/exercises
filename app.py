#ler e mostrar todas as linhas do arquivo cities
def show_cities():
    with open("cities.txt", encoding="utf-8") as cities:
        print(cities.read())

#conta o numero de linhas do arquivo cities
def count_lines():
    with open("cities.txt", encoding="utf-8") as cities:
        print(len(cities.readlines()))
        

count_lines()