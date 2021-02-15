from octeract import *

# Define the model
bob = Model()

# Define an objective function
bob.maximize("happiness_level")

# Set bounds for the decision variable
bob.set("happiness_level").between(0,100)

# Print the model
print(bob)

# Invoke the solver to get a solution
bob.global_solve()
