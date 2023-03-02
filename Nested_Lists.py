if __name__ == '__main__':
    s_grade=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s_grade.append([name,score])
    sorted_sc=sorted(list(set([x[1] for x in s_grade])))
    secound_low=sorted_sc[1]
    
    low_list=[]
    for students in s_grade:
        if secound_low==students[1]:
            low_list.append(students[0])
    
    for students in sorted(low_list):
        print(students)