import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_FILE_PATH = "./data/train_V2.csv"
data = pd.read_csv(CSV_FILE_PATH)

# Check the basic info of training dataset
data.info()
print(data.head(5))

