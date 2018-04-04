import random

def scores_grades():
    print 'Scores and Grades'
    for value in range(10):
        grade = random.randint(59,101)
        if grade > 89:
            print 'Score: {}; Your grade is A'.format(str(grade))
        elif grade > 79:
            print 'Score: {}; Your grade is B'.format(str(grade))
        elif grade > 69:
            print 'Score: {}; Your grade is C'.format(str(grade))
        else:
            print 'Score: {}; Your grade is D'.format(str(grade))
    print 'End of the program. Bye!'

scores_grades()