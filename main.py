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
    pass



def main():
    city1 = input("Please input the source city")
    city2 = input("Please input the destination city")
    algo = input("Please select the desired search algorithm")


    results = results(algo)
    print(f"Path: {city1} to {city2}"
            f"Algorithm: {algo}"
            f"Total cost: "
          f"Travel through: {cities}")


if __name__ == "__main__":
    main()