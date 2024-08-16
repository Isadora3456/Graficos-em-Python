import pandas as pd
import matplotlib.pyplot as plt
series = pd.read_csv(r"Aniversarios - Página1.csv", header=0,
index_col=0, parse_dates=True)
series.plot()
plt.show()