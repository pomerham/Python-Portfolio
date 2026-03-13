# Write your solution here
import  math
students = int(input("How many students on the course?"))
d_groups = int(input("Desired group size?"))
groups = (students / d_groups)
groups = math.ceil(groups)
print(f"Number of groups formed: {groups}")