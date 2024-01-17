import pandas as pd
import matplotlib.pyplot as plt

sleep="ZZZZZ.xlsx"
Project = pd.read_excel(sleep)

siralama= ['Low','Medium','High']
Project['Stress Level'] = pd.Categorical(Project['Stress Level'], categories=siralama, ordered=True)

bins = [25, 30, 35, 40, 45, 50]
Project['Age Groups'] = pd.cut(Project['Age'], bins=bins)
CalısmaGrup=(Project.groupby(['Age Groups','Stress Level'], observed=False)['Age'].count().unstack(fill_value=0))
grafik= CalısmaGrup.plot(kind='barh',stacked=True,colormap='viridis')


plt.tick_params(axis='x', rotation=45)
plt.tick_params(axis='y', rotation=45)
plt.title('Stress Levels by Age Groups')
plt.ylabel('Stress Level')
plt.xlabel('Number of people')
plt.legend(title='Work Hours Grouped', labels=siralama,loc='upper right')
plt.show()