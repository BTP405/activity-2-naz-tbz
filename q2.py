import matplotlib.pyplot as plt
def graphSnowfall(t):
    # Initialize dictionary to count each occurrence
    snowfall_ranges = {
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0
    }
    # Read data from file
    with open(t, 'r') as file:
        for line in file:
            #removing any leading or trailing whitespace characters and converting it to Int
            snowfall = int(line.strip()) 
            if snowfall <= 10:
                snowfall_ranges['0-10'] += 1
            elif snowfall <= 20:
                snowfall_ranges['11-20'] += 1
            elif snowfall <= 30:
                snowfall_ranges['21-30'] += 1
            elif snowfall <= 40:
                snowfall_ranges['31-40'] += 1
            else:
                snowfall_ranges['41-50'] += 1
    
    # Plotting the bar graph
    ranges = list(snowfall_ranges.keys())
    counts = list(snowfall_ranges.values())
    
    plt.bar(ranges, counts, color='blue')
    plt.xlabel('Snowfall Range (cms)')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Accumulation')
    return plt

# Call the function to generate the plot
plt = graphSnowfall('snowfall_data.txt')
# Save the plot to a file
plt.savefig('snowfall_data.png')
# Show the plot
plt.show()

