# most_frequent is a function to count the repeated letters in the string 

def most_frequent(string): 
    a=dict()
    for i in string:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    return a

y = most_frequent("mississippi")

# sorting in descending order     
sorted_y = sorted(y.items(), key=lambda y:y[1], reverse=True)
print(sorted_y)

for j in sorted_y:
    print(j[0],j[1])
