import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race =df['race'].squeeze()
    race_count = race.value_counts()

    # What is the average age of men?
    male = df.loc[df['sex']=='Male']
    average_age_men =round(male['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bc_total = df.loc[df['education']=='Bachelors'].shape[0]
    percentage_bachelors =round(bc_total/df.shape[0]*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    opt = ['Bachelors','Masters','Doctorate']
    adv_ed = df[df['education'].isin(opt)]
    mtf = adv_ed.loc[adv_ed['salary']=='>50K'].shape[0]
    p_mtf = round(mtf/adv_ed.shape[0]*100,1)
    # What percentage of people without advanced education make more than 50K?
    bsc_ed = df[~df['education'].isin(opt)]
    bscmtf= bsc_ed.loc[bsc_ed['salary']=='>50K'].shape[0]
    p_bscmtf = round(bscmtf/bsc_ed.shape[0]*100,1)
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = adv_ed.shape[0]
    lower_education = bsc_ed.shape[0]

    # percentage with salary >50K
    higher_education_rich = p_mtf
    lower_education_rich = p_bscmtf

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work = df.loc[df['hours-per-week']== min_work_hours]
    num_min_workers = min_work.shape[0]
    minhmtf = min_work.loc[min_work['salary']=='>50K'].shape[0]
    rich_percentage =  int(minhmtf/min_work.shape[0]*100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = ''
    highest_earning_country_percentage = 0
    for (country), sub_df in df.groupby(['native-country']):
      percentage = len(sub_df[(sub_df['salary'] == '>50K')])/ len(sub_df)
      if highest_earning_country_percentage < percentage:
        highest_earning_country_percentage = round(percentage,3)
        highest_earning_country = country
    highest_earning_country_percentage *= 100
    

    # Identify the most popular occupation for those who earn >50K in India.
    IN_mtf =  df.loc[(df['native-country']=='India')& (df['salary'] == '>50K')]
    pop_oc = df['occupation'].value_counts()
    top_IN_occupation = pop_oc.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
