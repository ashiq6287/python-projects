import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd=pd.read_csv("C:\country_wise_latest.csv")
print(pd)
pd.info()
res=sns.barplot(x='WHO Region',y='Confirmed',data=pd)
plt.show()





