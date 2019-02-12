from random import choice


def scramble(x: str, input_classes: {str: [str]}, output_classes: {str: [str]}):
    x_cls = next(filter(lambda cls: x in input_classes[cls], input_classes), None)

    if x_cls is None:
        raise Exception('No class found for', x)

    return choice(output_classes[x_cls])


def main():
    import pandas as pd
    df = pd.read_csv('datasets/student-mat.csv')

    input_classes = {'m': ['M', 'm'], 'f': ['F', 'f']}
    output_classes = {'m': ['Male', 'mAle', 'maLe', 'malE', 'MALE'],
                      'f': ['Female', 'FEMALE']}

    df['sex'] = df['sex'].apply(lambda x: scramble(x, input_classes, output_classes))

    print(df.head(20))


if __name__ == '__main__':
    main()
