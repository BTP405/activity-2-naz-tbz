def printStats(t):
    # Define a function inside printStats to handle the decoration
    def my_decorator(func):
        # Define another function inside my_decorator to wrap the original function
        def wrapper(line):
            # Inside the wrapper function, print the stats and call the original function
            print(*line)
            print("count of numbers:", len(line))
            print("average of numbers:", round(sum(line) / len(line), 2))
            print("maximum of numbers:", max(line))
            print('\n')
            result = func(line)
            return result
        # Return the wrapper function
        return wrapper
    
    # Open the file
    with open(t, "r") as file:
        for line in file:
            # Removing any leading or trailing whitespace characters, use "," as deliminator, converting to Int, put them into the list
            numbers = list(map(int, line.strip().split(",")))

            # Define a function named print_stats_decorated with the decoration
            @my_decorator
            def print_stats_decorated(line):
                pass    
            # Call the decorated function with the numbers
            print_stats_decorated(numbers)

# Call the function with the filename
printStats("file.txt")

