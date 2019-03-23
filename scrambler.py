from random import choice
from os import curdir, path
from settings import *


def scramble(x: str, input_classes: {str: [str]}, output_classes: {str: [str]}):
    x_cls = next(filter(lambda cls: x in input_classes[cls], input_classes), None)

    if x_cls is None:
        raise Exception('No class found for', x)

    return choice(output_classes[x_cls])


def main():
    import pandas as pd

    for csv in CSVS.values():
        scramble_info = csv['scramble']

        b_path = path.join(curdir, BACKUP_DIR, csv['filename'])
        d_path = path.join(curdir, DATASET_DIR, csv['filename'])
        df = pd.read_csv(b_path)

        if scramble_info is not None:
            df[scramble_info['field']] = df[scramble_info['field']].apply(lambda x: scramble(x, scramble_info['in'],
                                                                                                scramble_info['out']))

        df.to_csv(d_path)


if __name__ == '__main__':
    main()
