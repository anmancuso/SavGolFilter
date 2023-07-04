from utils import get_gain_smooth, get_avg_gain
import matplotlib.pyplot as plt
import numpy as np
def visualize(df_gain_monitoring, column, channels, gain_smooth_version, t, chi_square):
    plt.figure(figsize=(10, 6),dpi=200)
    for index in range(0,6):
        pmt = 6*column+index
        df_cut=df_gain_monitoring[df_gain_monitoring["Channel"]==pmt+2000]
        gain = np.array(df_cut["Gain"])
        score = np.array(df_cut["Score"])
        time = np.array(df_cut["Time_Unix"])
        weights=1/score
        time_string=np.array(df_cut["Time_String"])
        timestamp=[x-time[0] for x in time]
        
        gain_smooth, slope = get_gain_smooth(gain)
        
        plt.scatter(timestamp, gain , label =f"PMT {pmt}")
        plt.plot(timestamp, gain_smooth)
        t.extend(timestamp)
        gain_smooth_version.extend(gain_smooth)
        channels.extend([pmt for index in gain_smooth])
        chi_square.extend([0.0 for index in gain_smooth])
    
    plt.legend()
    ax=plt.gca()
    plt.xlabel('Time (days)')
    plt.xticks(timestamp[::3],[i[0:10] for i in time_string[::3]],rotation=45, ha='right',fontsize=10)    
    plt.tight_layout()
    plt.grid()
    plt.ylabel('ADC to PE')
    plt.title(f"Column {column+1}")
    plt.tight_layout()
    #plt.savefig(f"./NVGainSavGolFilter/overall/gain_monitoring_column{column+1}.png")
    plt.show()