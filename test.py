import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5]

# Pandas (Sample Standard Deviation, N-1)
df_std = pd.Series(data).std()

# NumPy (Population Standard Deviation, N)
np_std = np.std(data)

print("Pandas Sample Std Dev:", df_std)  # Pandas: Normalized by N-1
print("NumPy Population Std Dev:", np_std)  # NumPy: Normalized by N


##Pandas Sample Std Dev: 1.5811388300841898
##NumPy Population Std Dev: 1.4142135623730951