# Write your solution here
def sum_of_positives(x: list):
    total = []
    for i in x :
        if i > 0:
            total.append(i)
    return sum(total)            
    
if __name__ == "__main__":
    x = [1, 2, 3, 4]
    result = sum_of_positives(x)
    print(f"The result is: {result}")

    

