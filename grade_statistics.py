def user_input():
    score = input("Exam points and exercises completed: ")
    s_list = []
    tot_list = []
    while score != "":
        s_list = score.split()
        for i in s_list:
            tot_list.append(int(i))
        score = input("Exam points and exercises completed: ")
            
    #return tot_list
    return tot_list
        
def analyze_results(x: list):
    #tot_list = [1, 2, 3, 4, 5, 8]
    tot_list = x
    pt_avg = 0
    pascent = 0
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    pts = 0
    t_pts = 0
    
    for i in range(0, len(tot_list), 2):
        #(tot_list[i], tot_list[i+1])
        if tot_list[i] >= 10:
            pts = ((tot_list[i]) + (tot_list[i+1])//10)
 
            if pts >= 15 and pts <=17:
                one += 1
        
            elif pts >= 18 and pts <= 20:
                two += 1
            elif pts >= 21 and pts <= 23:
                three += 1
            elif pts >= 24 and pts <= 27:
                four += 1
            elif pts >= 28 and pts <= 30:
                five += 1
            elif pts < 15:
                zero += 1
        else:
            pts = ((tot_list[i]) + (tot_list[i+1])//10)
            zero += 1
            
        t_pts += pts
        p_avg = t_pts/(len(tot_list)/2)
        up = [one, two, three, four, five]
        down = [zero, one, two, three, four, five]
        up = sum(up)
        down = sum(down)
        if down == 0:
            p_cent = 0
        else:
            p_cent = (up/down) * 100
 
        #p_cent = up/down
    fi = five * "*"
    fo = four * "*"
    th = three * "*"
    tw = two * "*"
    on = one * "*"
    ze = zero * "*" 
    print("Statistics:")
    print(f"Points average: {p_avg:.1f}")
    print(f"Pass percentage: {p_cent:.1f}")
    print("Grade distribution:")
    print(f"  5: {fi}")    
    print(f"  4: {fo}")
    print(f"  3: {th}")
    print(f"  2: {tw}")
    print(f"  1: {on}")
    print(f"  0: {ze}")   
    
    
    #test to see if it prints out "0" grade distribution. ok!
    #return tot_list 
#if __name__ == "__main__":
grades = user_input()
analyze_results(grades)
#print(grades)