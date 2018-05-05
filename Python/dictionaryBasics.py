my_object = {
        'name': 'Michael',
        'age': 24,
        'country of birth': 'usa',
        'favorite language': 'Python'
    }
def about_me(dict):
    for key, value in dict.items():
        print 'My {} is {}.'.format(key, value)

about_me(my_object)
