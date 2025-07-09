# Startup-Success-Prediction-Analysis/Classifier

## Introduction

According to [KPMG](https://kpmg.com/xx/en/media/press-releases/2025/01/2024-global-vc-investment-rises-to-368-billion-dollars.html#:~:text=Enterprise's%20Venture%20Pulse-,2024%20global%20VC%20investment%20rises%20to%20%24368%20billion%20as%20investor,KPMG%20Private%20Enterprise's%20Venture%20Pulse), global venture capital (VC) investments totaled almost $369 billion for 2024 alone. With both so much uncertainty regarding the future success (or failure) of a given startup and the sheer investment capital at-stake, it is critical for VC firms, for both investment success and risk management, to be able to gauge the likelihood of a startup succeeding. VC firms often gravitate towards investing in tech startups due to the higher scalability of a tech startup's products/services. 

I use [this Startup Success Prediction Dataset](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction) for my analysis -- each data point in this dataset represents a startup and, along with other feature variable data, has a labeled target variable of either "acquired" or "closed" (i.e., for the purpose of this analysis, succeeded or failed). This analysis addresses the following three questions:

1. Given VC firms' preference for investing in tech startups, are tech startups more likely to be acquired (i.e., succeed) than non-tech startups?
2. VC firms can often overspend when investing in startups, resulting in losses for the VC firm. Using this dataset, can we identify a point of diminishing returns past which additional rounds of funding for a startup are no longer well-correlated to increased probability of acquisition (i.e., startup success)? Does a point of diminishing returns likewise exist with total funding?
3. Can we build a binary classifier that can accurately predict whether a given startup will succeed or fail?

## Initial Data Pre-Processing & Exploratory Data Analysis (EDA)

I load the CSV file containing the startup dataset and first take an overview of the dataset:

## Question 1: Are Tech Startups Historically More Likely to Be Acquired than Non-Tech Startups?

I perform exploratory data analysis (EDA) to address the question of whether tech startups are historically more likely to be acquired than non-tech startups. As I noted in the introduction, VC firms often gravitate towards investing in tech startups due to the higher scalability of a tech startup's products/services. Looking at past data contained in the dataset, we can gauge how viable this premise may be with respect to past outcomes (i.e., either if a startup is acquired or closed) on a per industry/sector basis.

The code I wrote to address Question 1 is contained in the `eda1_startup.py` file which is available in the src folder of this repo. My approach for Question 1 is to produce a barplot with acquisition rates on the y-axis and the industries/sectors represented in the dataset on the x-axis.

<img width="707" alt="eda1_main" src="https://github.com/user-attachments/assets/cb7ee2bb-45c9-4e55-83f6-a096fbc16519" />

The image above shows the main function of `eda1_startup.py`. I first read in the CSV file which contains the dataset for this project and cast it as a Pandas dataframe. Glancing at the CSV file that contains the dataset, we can see that it is already one-hot-encoded based on startup industry/sector, containing the columns `is_software`, `is_web`, `is_mobile`, `is_enterprise`, `is_advertising`, `is_gamesvideo`, `is_ecommerce`, `is_biotech`, `is_consulting`, and `is_othercategory` -- I use these one-hot-encoded columns as the bins of the bar plot I eventually produce. 

While the aforementioned columns are already one-hot-encoded, I need to one-hot-encode the `status` column of the dataset, which is the (labeled) target variable of the dataset. This is done in the subsequent lines of code in the main function, which one-hot-encodes the `status` column, which, in the dataset's original form, is comprised of values of either "acquired" or "closed" (i.e., string values) to `status_acquired` and `status_closed` (i.e., two distinct binarized columns).

The next step is to pass this now properly one-hot-encoded dataframe to a function I initialize, called `make_barplot`, which splices the whole dataframe into distinct dataframes per industry/sector and then calls another function I initialize, called `compute_acquisition_rate`, which, as the function's name suggests, computes the acquisition rate for whatever dataframe is passed as an argument into the `compute_acquisition_rate` function (see `eda1_startup.py` in the src folder for the full Python file). I compute the resulting acquisition rates for each of the aforementioned industries/sector categories represented in the dataset:

<img width="679" alt="acquisitionRates_result" src="https://github.com/user-attachments/assets/bca3963c-3c7f-479f-beba-68c18e9993f6" />

Moreover, I also produce a Seaborn bar plot for the results displayed above, which follows:

<img width="1440" alt="eda1_plot" src="https://github.com/user-attachments/assets/58941d51-614c-4a45-a95c-6f6cbec09cf7" />

I find a mean, cross-industry/sector acquisition rate of 64.2%.

## Questions 2.1 & 2.2: Does There Exist Diminishing Returns for Funding Rounds and/or Total Funding?

## Question 3: Can We Build a Binary Classifier that Can Accurately Predict Whether a Startup Will Be Acquired or Closed?


