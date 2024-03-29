##
## https://seaborn.pydata.org/examples/grouped_boxplot.html
##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)

plt.show()