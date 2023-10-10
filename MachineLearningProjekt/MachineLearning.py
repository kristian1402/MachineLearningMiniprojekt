from sklearn.datasets import fetch_covtype
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

covertype = fetch_covtype()

print(covertype.head(5))


