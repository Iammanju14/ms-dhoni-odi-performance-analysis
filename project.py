import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_excel("D:\\Academic Extra\\Manju College project\\mca 3rd sem\\python\\dataset.xlsx")
df=pd.DataFrame(data)
# removing the first 2 characters in the opposition stringcle
df['opposition'] = df['opposition'].apply(lambda x: x[2:])
# creating a feature for match year
df['year'] = df['date'].dt.year.astype(int)
# creating a feature for being not out
df['score'] = df['score'].apply(str)

df['not_out'] = np.where(df['score'].str.endswith('*'), 1, 0)
# dropping the odi_number feature because it adds no value to the analysis
df.drop(columns='odi_number', inplace=True)
# dropping those innings where Dhoni did not bat and storing in a new DataFrame
df_new = df.loc[((df['score'] != 'DNB') & (df['score'] != 'TDNB')), 'runs_scored':]
# fixing the data types of numerical columns
df_new['runs_scored'] = df_new['runs_scored'].astype(int)
df_new['balls_faced'] = df_new['balls_faced'].astype(int)
df_new['strike_rate'] = df_new['strike_rate'].astype(float)
df_new['fours'] = df_new['fours'].astype(int)
df_new['sixes'] = df_new['sixes'].astype(int)
first_match_date = df['date'].dt.date.min().strftime('%B %d, %Y') # first match
print('First match:', first_match_date)
last_match_date = df['date'].dt.date.max().strftime('%B %d, %Y') # last match
print('nLast match:', last_match_date)
number_of_matches = df.shape[0] # number of mathces played in career
print('nNumber of matches played:', number_of_matches)
number_of_inns = df_new.shape[0] # number of innings
print('nNumber of innings played:', number_of_inns)
not_outs = df_new['not_out'].sum() # number of not outs in career
print('nNot outs:', not_outs)
runs_scored = df_new['runs_scored'].sum() # runs scored in career
print('nRuns scored in career:', runs_scored)
balls_faced = df_new['balls_faced'].sum() # balls faced in career
print('nBalls faced in career:', balls_faced)
career_sr = (runs_scored / balls_faced)*100 # career strike rate
print('nCareer strike rate: {:.2f}'.format(career_sr))
career_avg = (runs_scored / (number_of_inns - not_outs)) # career average
print('nCareer average: {:.2f}'.format(career_avg))
highest_score_date = df_new.loc[df_new.runs_scored == df_new.runs_scored.max(), 'date'].values[0]
highest_score = df.loc[df.date == highest_score_date, 'score'].values[0] # highest score
print('nHighest score in career:', highest_score)
hundreds = df_new.loc[df_new['runs_scored'] >= 100].shape[0] # number of 100s
print('nNumber of 100s:', hundreds)
fifties = df_new.loc[(df_new['runs_scored']>=50)&(df_new['runs_scored']<100)].shape[0] #number of 50s
print('nNumber of 50s:', fifties)
fours = df_new['fours'].sum() # number of fours in career
print('nNumber of 4s:', fours)
sixes = df_new['sixes'].sum() # number of sixes in career
print('nNumber of 6s:', sixes)
# number of matches played against different oppositions
df['opposition'].value_counts().plot(kind='bar', title='Number of matches against different oppositions', figsize=(8, 5));
plt.show()
runs_scored_by_opposition = pd.DataFrame(df_new.groupby('opposition')['runs_scored'].sum())
runs_scored_by_opposition.plot(kind='bar', title='Runs scored against different oppositions', figsize=(8, 5))
plt.xlabel(None);
plt.show()
innings_by_opposition = pd.DataFrame(df_new.groupby('opposition')['date'].count())
not_outs_by_opposition = pd.DataFrame(df_new.groupby('opposition')['not_out'].sum())
temp = runs_scored_by_opposition.merge(innings_by_opposition, left_index=True, right_index=True)
average_by_opposition = temp.merge(not_outs_by_opposition, left_index=True, right_index=True)
average_by_opposition.rename(columns = {'date': 'innings'}, inplace=True)
average_by_opposition['eff_num_of_inns'] = average_by_opposition['innings'] - average_by_opposition['not_out']
average_by_opposition['average'] = average_by_opposition['runs_scored'] / average_by_opposition['eff_num_of_inns']
average_by_opposition.replace(np.inf, np.nan, inplace=True)
major_nations = ['Australia', 'England', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka', 'West Indies']
plt.show()
plt.figure(figsize = (8, 5))
plt.plot(average_by_opposition.loc[major_nations, 'average'].values, marker='o')
plt.plot([career_avg]*len(major_nations), '--')
plt.title('Average against major teams')
plt.xticks(range(0, 7), major_nations)
plt.ylim(20, 70)
plt.legend(['Avg against opposition', 'Career average']);
plt.show()
df['year'].value_counts().sort_index().plot(kind='bar', title='Matches played by year', figsize=(8, 5))
plt.xticks(rotation=0);
plt.show()
df_new.groupby('year')['runs_scored'].sum().plot(kind='line', marker='o', title='Runs scored by year', figsize=(8, 5))
years = df['year'].unique().tolist()
plt.xticks(years)
plt.xlabel(None);
plt.show()
