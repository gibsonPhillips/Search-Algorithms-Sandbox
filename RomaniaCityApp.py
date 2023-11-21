"""
https://github.com/aimacode/aima-python/blob/master/search.py
Gibson Phillips
"""
from Search import *


## helper fn to handle the different algorithms
def results(algo):
    return ["city1", "city2", 300]

## helper fn to prompt user for source city
def city_1(con=0):
    city1 = input("Please input the source city: ")
    if city1 not in Graph.nodes(romania_map):
        print("error: invalid City, please try again")
        city_1()
    return city1


## helper fn to prompt user for destination city
def city_2(city1):
    city2 = input("Please input the destination city: ")
    if city2 == city1:
        print("error, the cities cannot be the same. Please try again. ")
        city_2(city1)
    elif city2 not in Graph.nodes(romania_map):
        print("error: invalid City, please try again")
        city_2(city1)
    return city2


def main(first):
    if first == 0:
        print("Welcome to Romania! Input 2 cities and ")
    city1 = city_1()
    city2 = city_2(city1)
    algo = input("Please select the desired search algorithm: ")

    cities = results(f"→→{algo}→→")
    cost = cities.pop(-1)
    print(f"\nPath: {city1} to {city2}"
            f"\n\nAlgorithm: {algo}"
            f"\n\nTotal cost: {cost}"
            f"\n\nTravel through: {cities}")

    condition = input("\n\n Would you like to do it again? y(yes) n(no)")
    if condition in {"y", "Y", "yes", "Yes", "YES", 1}:
        main(1)
    elif condition in {"n", "N", "no", "No", "NO", 0}:
        print("\n\nThank You for Using Our App.")
        return
    else:
        print("error: unexpected input")
        return

if __name__ == "__main__":
    main(0)