from visualization import visualize
import pandas as pd
if __name__ == '__main__':
    gain_smooth_version = []
    channels = []
    t = []
    chi_square = []
    df_gain_monitoring = pd.read_csv("gain_monitoring_SR1_v6.csv")  # Load the data here
    for c in range(0,20):
        visualize(df_gain_monitoring, c, channels, gain_smooth_version, t, chi_square)
