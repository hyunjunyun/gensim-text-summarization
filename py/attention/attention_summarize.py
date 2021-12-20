import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import urllib.request

np.random.seed(seed=0)

data = pd.read_csv("datas/", nrows=100000)
print('전체 리뷰 개수 :', (len(data)))
