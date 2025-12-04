import os
import pandas as pd
import numpy as np
np.set_printoptions(precision=16, suppress=False)

from scipy.signal import find_peaks
import matplotlib.pyplot as plt

file_path = os.path.join(os.path.dirname(__file__), "Data5_50mV_CV4.csv")
df = pd.read_csv(file_path)

E = df["Potential"].values
I = df["Current"].values

anodic_peaks, _ = find_peaks(I, height=np.mean(I))
anodic_peak_E = E[anodic_peaks]
anodic_peak_I = I[anodic_peaks]

cathodic_peaks, _ = find_peaks(-I, height=-np.mean(I))
cathodic_peak_E = E[cathodic_peaks]
cathodic_peak_I = I[cathodic_peaks]

print ("Anodic peak potentials:", anodic_peak_E)
print ("Cathodic peak potential:", cathodic_peak_E)
print ("Current Maxima:", anodic_peak_I)
print ("Current Minima:", cathodic_peak_I)

plt.plot(E, I, label="CV")
plt.scatter(anodic_peak_E, anodic_peak_I, color="red", label="Anodic Peaks")
plt.scatter(cathodic_peak_E, cathodic_peak_I, color="blue", label="Cathodic Peaks")
plt.xlabel("Potential (V)")
plt.ylabel("Current")
plt.legend()
plt.show()
