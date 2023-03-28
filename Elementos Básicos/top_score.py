"""
Consider the following scenario about using if-elif-else statements: 

Students in a class receive their grades as Pass/Fail. 
Scores of 60 or more (out of 100) mean that the grade is "Pass". 
For lower scores, the grade is "Fail". 
In addition, scores above 95 (not included) are graded as "Top Score". 

Fill in the blanks in this function so that it returns the appropriate "Pass",  "Fail", or "Top Score" grade.

"""

def exam_grade(score):
    if exam_grade > 95:
        grade = "Top Score"
    elif exam_grade >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65)) # Should print Pass
print(exam_grade(55)) # Should print Fail
print(exam_grade(60)) # Should print Pass
print(exam_grade(95)) # Should print Pass
print(exam_grade(100)) # Should print Top Score
print(exam_grade(0)) # Should print Fail