# Predict Future Medical Events

# Problem Statement

Insurance Plus++, a premium payer, wants to use predictive modeling on healthcare data to predict the occurrence of future events among their covered patients. They want to use existing data about their patients’ previous medical events to predict future events in their patient journey. Events are recorded in the standardized ICD-9 format (details here). In this challenge, the goal is to predict the next 10 events in 2014 for each patient in order of occurrence.

# Data Description

There are three files available for download: train.csv, test.csv and sample_submission.csv

The “train.csv” file contains historical patient information from Jan 2011 to Dec 2013. The “test.csv” file contains a list of Patient IDs for which we aim to predict the next 10 events for in the year 2014. Event codes should be considered to be categorical in nature, not continuous.

Event Code (ICD-9 format, the target variable of this challenge)

To submit a valid entry, please submit a .csv file with a single row for each Patient ID, and the predicted ICD-9 coded events in separate variables ordered by recency (e.g. Event1 is the first to occur in 2014). A sample submission file (“sample_submission.csv”) is provided for reference as well as the example below.


In addition to the predicted events, please provide the following materials in .xls, .xlsx, or .ppt format:

   A 250 word write-up outlining your overall approach to the problem statement

   A list of steps taken in data cleaning, any errors you may have found in the data, and a description of any exclusions in your training dataset

   Details on any pre-processing steps, or any intermediary variables created for the solution

   A summary of any key observations and inferences you made from the data, as well as the most important variables in your model

   A technical explanation of your choice in models, and details on the steps you took to validate your results

   Add this file to the .zip file described below.

For further evaluation, please provide a .zip file containing:

   The code used to create your submission

   A readme document with any information required to reproduce your results from your code

   The code should be end-to-end, starting from the extraction of the original files provided to the final submission file.

# Model Evaluation

The evaluation matrix (final scoring) for this competition is mean NDCG (Normalized discounted cumulative gain)@K, where K=10.

# Submission Guidelines

Please remember to make your final submission based on the provided guidelines. Participants failing to follow these guidelines will not be short-listed for the next round.
