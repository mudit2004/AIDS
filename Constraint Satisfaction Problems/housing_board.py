#house allotment problem - csp

from constraint import Problem

def house_allotment():
    problem = Problem()

    # Define the variables (people) and their possible assignments (houses)
    people = ["P1", "P2", "P3", "P4", "P5"]
    houses = ["H1", "H2", "H3", "H4", "H5"]

    # Add variables to the problem and specify their domains (possible house assignments)
    for person in people:
        problem.addVariable(person, houses)

    # Add constraints based on preferences
    problem.addConstraint(lambda p1, h: h in ["H3", "H4"], ("P1", "H3"))
    problem.addConstraint(lambda p2, h: h in ["H2", "H3"], ("P2", "H2"))
    problem.addConstraint(lambda p3, h: h in ["H1", "H5"], ("P3", "H1"))
    problem.addConstraint(lambda p4, h: h in ["H2", "H3"], ("P4", "H2"))
    problem.addConstraint(lambda p5, h: h in ["H4", "H5"], ("P5", "H4"))

    # Solve the CSP problem
    solutions = problem.getSolutions()

    return solutions

solutions = house_allotment()

for solution in solutions:
    print(solution)
