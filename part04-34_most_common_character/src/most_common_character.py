# Write your solution here
def most_common_character(x: str):        # def function
    high = 0                                # init counter to 0
    new = [" "]                               # list with " " indexed 0
    for i in x:                                     
        sum = (x.count(i))                      #creates a variable with number of count
        if sum > high:                              
            high = sum                            #reset high value
            new[0] = i                              #replace with new value in list
    return new[0]                                   #return the value with highest


if __name__ == "__main__":
    string = str(input("type in a word:"))
    print(most_common_character(string))