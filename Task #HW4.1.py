def get_data():
    return[
        {'name': "Alexey", 'rate': 2, 'course': "Python"},
        {'name': "Fedya", 'rate': 3, 'course': "C++"},
        {'name': "Roma", 'rate': 4, 'course': "Java"},
        {'name': "Omar", 'rate': 1, 'course': "Python"},
        {'name': "Kolya", 'rate': 3, 'course': "Python"},
        {'name': "Olga", 'rate': 1, 'course': "Java"},
        {'name': "Molya", 'rate': 4, 'course': "C++"},
        {'name': "Tolya", 'rate': 1, 'course': "C++"},
        {'name': "Ovi", 'rate': 2, 'course': "C++"},
        {'name': "Ivan", 'rate': 2, 'course': "Java"},
        {'name': "Um", 'rate': 3, 'course': "Java"}

    ]
def get_courses(data):
    return ({item['course'] for item in data})

def get_tops(data, courses):
    return (sorted([(item['name'],item['rate']) for item in data if item['course'] == courses],
                   key = lambda x: x[1]))

def get_top_table(courses):
    return 'COURSE {}\n'.format(courses.upper()) + \
        '\n'.join('{} takes {} place'.format(*top)
                  for top in get_tops(get_data(),courses))

if __name__ == '__main__':
    print('\n'.join(get_top_table(course) for course in get_courses(get_data())))

