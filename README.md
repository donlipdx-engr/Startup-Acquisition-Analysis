# Startup-Success-Prediction-Analysis/Classifier

## Introduction

According to [KPMG](https://kpmg.com/xx/en/media/press-releases/2025/01/2024-global-vc-investment-rises-to-368-billion-dollars.html#:~:text=Enterprise's%20Venture%20Pulse-,2024%20global%20VC%20investment%20rises%20to%20%24368%20billion%20as%20investor,KPMG%20Private%20Enterprise's%20Venture%20Pulse), global venture capital (VC) investments totaled almost $369 billion for 2024 alone. With both so much uncertainty regarding the future success (or failure) of a given startup and the sheer investment capital at-stake, it is critical for VC firms, for both investment success and risk management, to be able to gauge the likelihood of a startup succeeding. VC firms often gravitate towards investing in tech startups due to the higher scalability of a tech startup's products/services. 

I use [this Startup Success Prediction Dataset](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction) for my analysis. This analysis addresses the following three questions:

1. Given VC firms' preference for investing in tech startups, are tech startups more likely to be acquired (i.e., succeed) than non-tech startups?
2. VC firms can often overspend when investing in startups, resulting in losses for the VC firm. Using this dataset, can we identify a point of diminishing returns (or saturation point) whereby additional rounds of funding for a startup no longer significantly contributes to increased probability of acquisition (i.e., startup success)? Would such a point of diminishing returns be a function of startup sector/industry? Does a point of diminishing returns likewise exist with total funding (in USD)?
3. Can we build a binary classifier that can accurately predict whether a given startup will succeed or fail?

## Initial Data Pre-Processing & Exploratory Data Analysis (EDA)

I load the CSV file containing the startup dataset and first take an overview of the dataset:

<img width="694" alt="Screenshot 2025-07-05 at 3 08 10 PM" src="https://github.com/user-attachments/assets/470419e9-b485-43e0-be7d-5026d214cb60" />

Prior to any data pre-processing, our dataset contains 923 points with 49 columns -- there are, at least initially, 48 feature variables and 1 (binary) target variable, the latter of which is named "status" and has values of "acquired" (meaning succeeded) or "closed" (meaning failed).

The next step in the data pre-processing stage is to check for and handle missing values and/or duplicate rows in the dataset:

<img width="312" alt="Screenshot 2025-07-05 at 3 42 44 PM" src="https://github.com/user-attachments/assets/f21de3aa-69cd-41a9-9c68-ccf6436a0bcb" />

As can be seen from executing my source code for pre-processing this dataset, the "unnamed: 6", "closed_at", "age_first_milestone_year", and "age_last_milestone_year", and "state_code.1" have missing values. It is expected that the "closed_at" column of the dataset should have missing values because some of the startups represented in the dataset did not close and went on to become acquired (i.e., succeed). 

Because I eventually build a binary classifier, for pre-processing this dataset, I need to binarize this dataset. This entails dropping non-binary columns from the dataset and binarizing the "status" column using a one-hot encoding. 


