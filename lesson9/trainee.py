from functools import reduce
from operator import gt


courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                        'title': 'Object-Oriented Python',
                        'prereqs': [{'count': 1,
                                     'title': 'Python Collections',
                                     'prereqs': [{'count': 0,
                                                  'title': 'Python Basics',
                                                  'prereqs': []}]},
                                    {'count': 0,
                                     'title': 'Python Basics',
                                     'prereqs': []},
                                    {'count': 0,
                                     'title': 'Setting Up a Local Python Environment',
                                     'prereqs': []}]},
                       {'count': 0,
                        'title': 'Flask Basics',
                        'prereqs': []}]}


def prereqs(data, pres=None):
    pres = pres or set()
    for prereq in data['prereqs']:
        pres.add(prereq['title'])

        prereqs(prereq, pres)
    return pres


# print(prereqs(courses))
# print(courses)


strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven know and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]
longest = reduce(lambda x, y: x if x>y else y, strings)
print(len(longest))
# print(list(map(lambda x: len(x), strings)))
