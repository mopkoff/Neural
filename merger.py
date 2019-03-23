import pandas as pd
import os
from settings import STUDENTS_FILENAME

d1 = pd.read_csv(os.path.join(os.curdir, 'datasets_backup', 'student-mat.csv'))
d2 = pd.read_csv(os.path.join(os.curdir, 'datasets_backup', 'student-por.csv'))

d = d1.append(d2)
d.to_csv(os.path.join(os.curdir, 'datasets', STUDENTS_FILENAME))
