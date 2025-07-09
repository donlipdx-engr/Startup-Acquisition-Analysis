# Startup-Success-Prediction-Analysis/Classifier

## Introduction

According to [KPMG](https://kpmg.com/xx/en/media/press-releases/2025/01/2024-global-vc-investment-rises-to-368-billion-dollars.html#:~:text=Enterprise's%20Venture%20Pulse-,2024%20global%20VC%20investment%20rises%20to%20%24368%20billion%20as%20investor,KPMG%20Private%20Enterprise's%20Venture%20Pulse), global venture capital (VC) investments totaled almost $369 billion for 2024 alone. With both so much uncertainty regarding the future success (or failure) of a given startup and the sheer investment capital at-stake, it is critical for VC firms, for both investment success and risk management, to be able to gauge the likelihood of a startup succeeding. VC firms often gravitate towards investing in tech startups due to the higher scalability of a tech startup's products/services. 

I use [this Startup Success Prediction Dataset](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction) for my analysis. This analysis addresses the following three questions:

1. Given VC firms' preference for investing in tech startups, are tech startups more likely to be acquired (i.e., succeed) than non-tech startups?
2. VC firms can often overspend when investing in startups, resulting in losses for the VC firm. Using this dataset, can we identify a point of diminishing returns past which additional rounds of funding for a startup are no longer well-correlated to increased probability of acquisition (i.e., startup success)? Does a point of diminishing returns likewise exist with total funding?
3. Can we build a binary classifier that can accurately predict whether a given startup will succeed or fail?

## Initial Data Pre-Processing & Exploratory Data Analysis (EDA)

I load the CSV file containing the startup dataset and first take an overview of the dataset:


