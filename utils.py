import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import seaborn as sns

from scipy.signal import savgol_filter


def get_gain_smooth(gain, min_window_size=5, max_window_size=11, step_size=1):
    window_size = min_window_size
    while True:
        gain_smooth = savgol_filter(gain, window_size, 1)
        slope = np.gradient(gain_smooth)
        left_median = np.median(slope[:window_size])
        right_median = np.median(slope[-window_size:])
        if (np.abs(left_median) < 0.1 and np.abs(right_median) < 0.1) or window_size >= max_window_size:
            break
        window_size = min(window_size + step_size, max_window_size)
    return gain_smooth, slope

def get_avg_gain(gain, gain_smooth, threshold_percentile=(5, 95), threshold_scale=0.025):
    diff = np.abs(gain - gain_smooth)
    threshold = threshold_scale * (np.percentile(diff, threshold_percentile[1]) - np.percentile(diff, threshold_percentile[0]))
    avg_gain = []
    start_idx = 0
    for i in range(1, len(gain)):
        if diff[i] > threshold:
            avg_gain.append(np.mean(gain[start_idx:i]))
            start_idx = i
    avg_gain.append(np.mean(gain[start_idx:]))
    return avg_gain