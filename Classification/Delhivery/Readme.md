# Problem Statement

Delhivery seeks an automated solution to identify the fraudulent objects by classifying the x-ray images. 

Participants/teams are required to build a solution with the description of a product, and it's x-rayed image that predicts whether the given product description matches the x-ray image.

# Data inputs

Participants will receive the following data inputs for the challenge:

X_ray_images: All the x-ray images are available in the folder ‘x_ray_images.’ This folder further contains two subfolders:

`train_xray_images`: contains the x-ray images for train data  
`test_xray_images`: contains the x-ray images for test data

Training Data: The file `train.csv` comprises three columns. Each row represents a data point viz. the filename for each x-ray image, product description corresponding to each x-ray image, and ‘Status,’ i.e., whether the product description matches the x-ray image or not. The value of ‘Status’ can be “True” or “False” where “True” implies that the product description matches the x-ray image and “False” implies the product description does not match the x-ray image.
<br>

Test Data: File `test.csv` comprises two columns. Each row represents a data point viz. The filename for each x-ray image and the product description corresponding to each x-ray image. Your system will be required to predict whether the x-ray image matches the product description.

# Additional Training Data for recognizing product descriptions

File `product_description_only.csv` contains 3 columns with around 100 thousand rows. Each row represents a data point. The first column contains the product description of a given product, while the second and third columns contain the category and sub-category of the product. This file can be optionally used to make the algorithm more robust.
<br>

Please note, two different product descriptions may map to the same product. For example, “iPhone 7 Black 32GB” and "iPhone 732 gigabyte memory Black" are two different descriptions of the same product. Also note that when an x-ray image doesn’t match the corresponding product description, then the x-ray image may belong to any unseen product and is not bound to match any product already seen in the training data.

# Dataset

Updated Train Test images, Datasets, and Submission File on 8th March.

Images and Dataset: http://hck.re/0kNuTw 

Submission File: http://hck.re/OMogFJ

# Evaluation

Participants/teams will receive a training dataset and a test dataset, wherein training dataset will contain labels, and the test dataset will have no labels. Participants/teams will be required to build a system using the training dataset, run the system on the test dataset and upload the test dataset labels predicted by the system.
<br>

Participants/teams will be shortlisted basis their performance on this test dataset. After the competition closes, the performance of the system built will be measured with a new dataset. The final choice of the winner for the Delhivery problem will be basis the participant's/team's performance on this test data.
<br>

'F1 Score' will be used to evaluate the performance of system built by the participants/teams.
