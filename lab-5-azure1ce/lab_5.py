# Lab 5
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def transform_tuple(original_tuple: tuple) -> tuple[int, int]:
    #prepare 2 return result
    even_count = 0
    odd_count = 0
    #go over the elements in tuple
    for num in original_tuple:
        if num %2 == 0:
            even_count+=num
        else:
            odd_count+=num
    return (even_count,odd_count)
# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 2 -----------------
def grade_summary(student_grades: dict[str, list]) -> dict[str, dict]:
    new_dic = {}
    for studnet_name, grade_list in student_grades.items():
        new_dic[studnet_name] = {"average":round(sum(grade_list)/len(grade_list),2), "highest":max(grade_list)}
    return (new_dic)
# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 3 -----------------
def unique_letters(string1: str, string2: str) -> tuple[set, set]:
    set1 = set()
    set2 = set()
    for alpha in string1:
        set1.add(alpha)
    for alpha in string2: 
        set2.add(alpha)
    return (set1.difference(set2),set2.difference(set1))

# invoke the function with relevant args of your choice
# WRITE CODE HERE
