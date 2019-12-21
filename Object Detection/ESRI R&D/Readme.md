- [Competition](#competition)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Test Images Results](#test-images-results)


# Competition

Hackerearth competition page: [Esri Data Science Challenge 2019](https://www.hackerearth.com/challenges/hiring/esri-data-science-challenge-2019/)

---

# Problem Statement

Given an aerial image, we have to identify two objects: Pool and Car.

Now Car is present in almost all Object Detection datasets, but Pool may be or may not be supported.

Hence, we need to fine tune pretrained models on given dataset.

---

# Dataset

Dataset :  [Link](https://s3-ap-southeast-1.amazonaws.com/he-public-data/ESRI%20DATAc8fe593.zip)

We are given 3748 training images and 2703 testing images each may contain two objects Pool and Car.

Training Col 1 | Training Col 2
--------------------------- | ---------------------------
![train_1](samples/ex_1.png "train_1") | ![train_2](samples/ex_2.png "train_2")
![train_3](samples/ex_3.png "train_3") | ![train_4](samples/ex_4.png "train_4")

Testing Col 1 | Testing Col 2
--------------------------- | ---------------------------
![test_1](samples/test_1.png "test_1") | ![train_2](samples/test_2.png "test_2")
![test_3](samples/test_3.png "test_3") | ![train_4](samples/test_4.png "test_4")
---

## Test Images Results

![prediction_1](results/result_1.png "Prediction_1")

![prediction_2](results/result_2.png "Prediction_2")

![prediction_3](results/result_3.png "Prediction_3")

![prediction_4](results/result_4.png "Prediction_4")

![prediction_5](results/result_5.png "Prediction_5")
