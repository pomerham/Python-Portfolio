# Write your solution here
attempts = 0
while True:
    code = input("PIN:")
    attempts += 1
    if attempts == 1 and code == "4321":
        success = True
        break
    if attempts > 1 and code == "4321":
        success = False
        break
    print("Wrong")
if success:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")