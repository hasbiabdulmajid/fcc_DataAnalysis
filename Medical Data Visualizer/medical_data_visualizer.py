import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

#df['bmi'] = df.apply(lambda x: (x.weight/(x.height**2)), axis=1)
#condlist = [df["bmi"] <= 25,df["bmi"] > 25]
#condchoice = [0, 1]
# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height']/100)**2).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

condlist_chol = [df["cholesterol"] == 1,
            df["cholesterol"] > 1]
condchoice_chol = [0, 1]
df['cholesterol'] = np.select(condlist_chol,condchoice_chol)

condlist_gluc = [df["gluc"] == 1,
            df["gluc"] > 1]
condchoice_gluc = [0, 1]
df['gluc'] = np.select(condlist_gluc,condchoice_gluc)

# fast way 
# df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
# df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
# Draw Categorical Plot
def draw_cat_plot():
  
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,id_vars = 'cardio', value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
  df_cat['total']=0


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).count().reset_index()
    
    # Draw the catplot with 'sns.catplot()'
  bar = sns.catplot(x='variable', y = 'total', hue = 'value', col = 'cardio', data = df_cat, kind = 'bar')
  fig = bar.fig



    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
             (df['height'] >= (df['height'].quantile(0.025))) & 
             (df['height'] <= (df['height'].quantile(0.975))) & 
             (df['weight'] >= (df['weight'].quantile(0.025))) & 
             (df['weight'] <= (df['weight'].quantile(0.975)))]
  

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    #mask = np.triu(np.ones(corr.shape)).astype(np.bool)


    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, 
                mask=mask, 
                vmax=.3, 
                square=True,
                linewidths=.5,
                annot = True,
                fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
