import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 382319199 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x - 0.5
    alpha = 1 - p
    loc = x.mean()
    scale = 1
    return 2 * loc / 32 ** 2 - 2 * scale * norm.ppf(1 - alpha / 2) / 32 ** 2, \
           2 * loc / 32 ** 2 - 2 * scale * norm.ppf(alpha / 2) / 32 ** 2
