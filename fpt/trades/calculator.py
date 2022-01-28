def percentage_calculator(total_val, partial_val):

    if total_val > partial_val and partial_val > 0:
        percentage = 100 * partial_val / total_val
    elif partial_val < 0:
        partial_val = -partial_val
        percentage = 100 * partial_val / total_val
        percentage = -percentage
    else:
        print("ERROR: Total value inferior to partial value")

    return percentage


print(percentage_calculator(12500, 100))


