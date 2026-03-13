# Write your solution here
let_1 = input("1st letter:")
let_2 = input("2nd letter:")
let_3 = input("3rd letter:")

if let_1 > let_2 and let_1 > let_3:
    if let_2 > let_3:
        print("The letter in the middle is", let_2)
    else:
        print("The letter in the middle is", let_3)    

elif let_2 > let_1 and let_2 > let_3:
    if let_1 < let_3:
        print("The letter in the middle is", let_3)
    else:
        print("The letter in the middle is", let_1)    
elif let_3 > let_1 and let_3 > let_2:
    if let_1 < let_2:
        print("The letter in the middle is", let_2)
    else:
        print("The letter in the middle is", let_1)  
