"""
https://github.com/aimacode/aima-python/blob/master/search.py
Gibson Phillips
"""

"""
The output should include the results for two cities (See the sample outputs).
▪ Two Test Cities: Arad and Bucharest, Bucharest and Craiova, and Craiova and Arad
▪ Search Method Name
▪ Total Cost between Two Cities
▪ All the Intermediate Cities Between Them
▪ Ask the Users If They Would Like to Find the Optimal Path Between Any Two
Cities Again
▪ Terminate the Program and Then Display "Thank You for Using Our App."
"""


def results(algo):
    return ["city1", "city2", 300]


def main(first):
    if first == 0:
        print("Welcome to Romania! Input 2 cities and ")

    city1 = input("Please input the source city: ")
    city2 = input("Please input the destination city: ")
    algo = input("Please select the desired search algorithm: ")

    cities = results(algo)
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