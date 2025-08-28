def find_occurrences(text, pattern):
    positions = []
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
            count += 1
    
    if count > 0:
        return(True,count,positions)
    else:
        return(False,count,[])
    pass

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
