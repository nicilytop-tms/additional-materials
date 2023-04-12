names = {
    1: 'Dima',
    2: 'Vitya',
    3: 'Tom'
}
print(names[3])  # Example how do we need to do

names0 = {
    1: 'some str',
    -34: [4, 'NAME', 4.8],
    (2, 45, -10): 'Tom',
    True: (2, 45, -10)
}
print('Tom should be here')

names1 = {
    True: 'Dima',
    False: 'Tom',
    'Who': 'knows',
    'data': 'data'
}
print('Tom should be here')

names2 = {
    'names': 'not here',
    'names1': not True,
    'names3': [1, 2, 3, {'hmm': 'Tom'}]
}
print('Tom should be here')

names3 = {
    123: [{'name': 'vitya'}, 'Dima', (22, 33, 23, 32)],
    'Tom here': {
        (1, 2, 3, 4, 5): {
            'deeper': {
                False: {
                    'even deeper': {
                        'you\'re almost there': False,
                        1: 2,
                        True: {
                            'YESS, found': names2
                        }
                    }
                },
                343: ['some', 'name']
            }
        }
    }
}
print('Tom should be here')
