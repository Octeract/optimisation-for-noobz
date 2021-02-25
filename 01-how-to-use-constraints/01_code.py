from octeract import *

# Define the model
bob = Model()

# Define an objective function
bob.maximize("happiness_level")

# Set bounds for the decision variable
bob.set("happiness_level").between(0,100)

# Set point system for happiness per task
bob.set("happiness_friends").to("5*time_with_friends")
bob.set("happiness_studying").to("-2*time_studying")

# Define how task happiness contributes to overall happiness
bob.set("happiness_level").to("happiness_friends + happiness_studying")

# Print the model
print(bob)

# Invoke the solver to get a solution
bob.global_solve()

# Print the results
results = bob.get_solution_vector()
print(results)
