BACKUP_DIR = 'datasets_backup'
DATASET_DIR = 'datasets'

CSVS = {
    'adult': {
        'filename': 'adult.csv',
        'scramble': {
            'field': 'sex',
            'in': {'m': ['Male'], 'f': ['Female']},
            'out': {'m': ['male', 'MALE', 'Male', 'M', 'm'], 'f': ['female', 'FEMALE', 'Female', 'F', 'f']}
        }
    },
    'boston_housing': {
        'filename': 'boston_housing.csv',
        'scramble': None
    },
    'heart': {
        'filename': 'heart.csv',
        'scramble': None
    },
    'house_data': {
        'filename': 'kc_house_data.csv',
        'scramble': None
    },
    'mushrooms': {
        'filename': 'mushrooms.csv',
        'scramble': {
            'field': 'odor',
            'in': {'a': ['a'], 'l': ['l'], 'c': ['c'], 'y': ['y'], 'f': ['f'],
                   'm': ['m'], 'n': ['n'], 'p': ['p'], 's': ['s']},
            'out': {
                'a': ['almond', 'ALMOND', 'Almond', 'a', 'A'],
                'l': ['anise', 'ANISE', 'Anise', 'l', 'L'],
                'c': ['creosote', 'CREOSOTE', 'Creosote', 'c', 'C'],
                'y': ['fishy', 'FISHY', 'Fishy', 'y', 'Y'],
                'f': ['foul', 'FOUL', 'Foul', 'f', 'F'],
                'm': ['musty', 'MUSTY', 'Musty', 'm', 'M'],
                'n': ['none', 'NONE', 'None', 'n', 'N'],
                'p': ['pungent', 'PUNGENT', 'Pungent', 'p', 'P'],
                's': ['spicy', 'SPICY', 'Spicy', 's', 'S']
            }
        }
    },
    'students': {
        'filename': 'students.csv',
        'scramble': {
            'field': 'sex',
            'in': {'m': ['M'], 'f': ['F']},
            'out': {'m': ['male', 'MALE', 'Male', 'M', 'm'], 'f': ['female', 'FEMALE', 'Female', 'F', 'f']}
        }
    },
    'titanic': {
        'filename': 'titanic.csv',
        'scramble': {
            'field': 'Sex',
            'in': {'m': ['male'], 'f': ['female']},
            'out': {'m': ['male', 'MALE', 'Male', 'M', 'm'], 'f': ['female', 'FEMALE', 'Female', 'F', 'f']}
        }
    },
    'wines': {
        'filename': 'wines.csv',
        'scramble': None
    },
}
