def wordCount(t):
    word_dict = {}   
    with open(t, 'r') as file:
        line_num = 1
        #Read the first line
        line = file.readline()
        while line:
            #Split the line into words
            words = line.strip().split()
            for word in words:
                #add it, if word is not in dictionary
                if word not in word_dict:
                    word_dict[word] = [line_num]
                #append line number to its list, if word is already in dictionary
                else:
                    word_dict[word].append(line_num)
            # Read the next line
            line = file.readline()
            # Increment line number
            line_num += 1    
    return word_dict

file_path = 'example.txt' 
result = wordCount(file_path)
print(result)



