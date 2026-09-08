def fill_unique(input_list, arg=None):
    if arg is None:  # To allow for reuse in multiple calls
        arg = []
    # Base case: filled all the values
    if len(input_list) == len(arg):
        return arg
    # Copy pre-given value
    if 0 < input_list[len(arg)]:
        arg.append(input_list[len(arg)])
    # Fill with the smallest value
    else:
        # Go over all possible values from smallest to largest
        for val in range(1, len(input_list) + 1):
            if (val not in input_list) and (val not in arg):  # If the value is not in either list
                arg.append(val)  # Add the value and leave
                break  # Exit the loop
    # Recursively add one more value
    return fill_unique(input_list, arg)


if __name__ == "__main__":
    numbers = [3, 0, 0, 1]
    filled = fill_unique(numbers)
    print("Original list:", numbers)
    print("Filled unique list:", filled)
