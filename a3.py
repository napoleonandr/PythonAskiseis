
def calculate_cost(lst):
    sum = 0
    for expense in lst:
        cost = expense["cost"]
        tax = expense["tax"]/100

        cost -= cost*tax
        sum += cost
    print(sum)


expenses = [
    {"cost": 100, "tax": 20},
    {"cost": 100, "tax": 25},
    {"cost": 100, "tax": 23},
    {"cost": 100, "tax": 15},
]

calculate_cost(expenses)

