# 1st EDA Question: Given VC firms' preference for investing in tech startups, are tech 
# startups more likely to be acquired (i.e., succeed) than non-tech startups?
#
# Approach: Output Seaborn barplot for is_software, is_web, is_mobile, is_enterprise, is_advertising	
# is_gamesvideo, is_ecommerce, is_biotech, is_consulting, is_othercategory on x-axis, and percentage
# of startups that ultimately are acquired (succeed) on y-axis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

from sklearn.preprocessing import OneHotEncoder

def compute_acquisition_rate(df):
    total_sector_startups = df.shape[0]
    sector_acquisitions = df[df['status_acquired'] == 1.0]
    num_sector_acquisitions = sector_acquisitions.shape[0]
    acquisition_rate = (num_sector_acquisitions / total_sector_startups) * 100
    acquisition_rate = round(acquisition_rate, 1)

    return acquisition_rate
    
def make_barplot(df_encoded):
    # Software Startups
    software_startups = df_encoded[df_encoded['is_software'] == 1]
    software_success_rate = compute_acquisition_rate(software_startups)
    print(f"The historical acquisition rate for software startups is {software_success_rate}%")

    # Web Startups
    web_startups = df_encoded[df_encoded['is_web'] == 1]
    web_success_rate = compute_acquisition_rate(web_startups)
    print(f"The historical acquisition rate for web startups is {web_success_rate}%")

    # Mobile Startups
    mobile_startups = df_encoded[df_encoded['is_mobile'] == 1]
    mobile_success_rate = compute_acquisition_rate(mobile_startups)
    print(f"The historical acquisition rate for mobile startups is {mobile_success_rate}%")

    # Enterprise Startups
    enterprise_startups = df_encoded[df_encoded['is_enterprise'] == 1]
    enterprise_success_rate = compute_acquisition_rate(enterprise_startups)
    print(f"The historical acquisition rate for enterprise startups is {enterprise_success_rate}%")

    # Advertising Startups
    advertising_startups = df_encoded[df_encoded['is_advertising'] == 1]
    advertising_success_rate = compute_acquisition_rate(advertising_startups)
    print(f"The historical acquisition rate for advertising startups is {advertising_success_rate}%")

    # Video Game Startups
    video_game_startups = df_encoded[df_encoded['is_gamesvideo'] == 1]
    gamesvideo_success_rate = compute_acquisition_rate(video_game_startups)
    print(f"The historical acquisition rate for video game startups is {gamesvideo_success_rate}%")

    # E-Commerce Startups
    ecommerce_startups = df_encoded[df_encoded['is_ecommerce'] == 1]
    ecommerce_success_rate = compute_acquisition_rate(ecommerce_startups)
    print(f"The historical acquisition rate for e-commerce startups is {ecommerce_success_rate}%")

    # Biotech Startups
    biotech_startups = df_encoded[df_encoded['is_biotech'] == 1]
    biotech_success_rate = compute_acquisition_rate(biotech_startups)
    print(f"The historical acquisition rate for biotech startups is {biotech_success_rate}%")

    # Consulting Startups
    consulting_startups = df_encoded[df_encoded['is_consulting'] == 1]
    consulting_success_rate = compute_acquisition_rate(consulting_startups)
    print(f"The historical acquisition rate for consulting startups is {consulting_success_rate}%")

    # Miscellaneous/Non-Specified Startups
    isother_startups = df_encoded[df_encoded['is_othercategory'] == 1]
    isother_success_rate = compute_acquisition_rate(isother_startups)
    print(f"The historical acquisition rate for startups of non-specified industry/sector is {isother_success_rate}%")

    # Compile list of success rates for startup industry/sector categories
    startup_data = [software_success_rate, web_success_rate, mobile_success_rate, enterprise_success_rate, 
                    advertising_success_rate, gamesvideo_success_rate, ecommerce_success_rate, 
                    biotech_success_rate, consulting_success_rate, isother_success_rate]
    
    # Cast startup_data Python list to NumPy array to find mean and standard deviation
    numpy_startup_data = np.array(startup_data)
    
    # Find mean startup success/acquisition rate 
    mean_acquisition_rate = numpy_startup_data.mean()
    mean_acquisition_rate = round(mean_acquisition_rate, 1)
    print(f"The mean startup success/acquisition rate across all industries/sectors in our dataset is {mean_acquisition_rate}%")

    # Output bar plot with startup sectors on x-axis and acquisition/success rate on y-axis
    # Create dictionary for bar plot data
    bar_plot_data = {
        'Industry/Sector': ['Software', 'Web', 'Mobile', 'Enterprise', 'Advertising', 'Video Games', 
                   'E-Commerce', 'Biotech', 'Consulting', 'Other'],
        'Acquisition/Success Rate (%)': startup_data
    }
    # Cast dictionary to Pandas dataframe
    df_bar_plot_data = pd.DataFrame(bar_plot_data)
    # Create Seaborn bar plot
    plot = sns.barplot(x = 'Industry/Sector', y = 'Acquisition/Success Rate (%)', data = df_bar_plot_data, palette='Set2')
    plt.figure(figsize=(14, 10))
    plot.set_title('Historical Acquisition/Success Rates for Startups by Industry/Sector')
    plt.show()

def main():
    df = pd.read_csv('startup_data.csv')

    # One Hot Encoding for "Status" Column (Target Variable)
    ohe_column = df[['status']]
    encoder = OneHotEncoder(sparse_output=False, drop=None)
    encoded_array = encoder.fit_transform(ohe_column)
    encoded_df = pd.DataFrame(encoded_array,columns=encoder.get_feature_names_out(['status']))
    df_encoded = pd.concat([df.drop('status', axis=1), encoded_df], axis=1)
    
    make_barplot(df_encoded)
    
if __name__ == "__main__":
    main()