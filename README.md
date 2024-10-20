# 463-Project-1

COMP SCI 463 Project 1

Steven Le

10/20/2024

Fall 2024

Professor Janghoon Yang

# Project Description
In this project, we are tasked with creating a program that can analyze large financial datasets to sort and detect anomalies. The techniques we are required to use are merge sort, divide and conquer and closest pair of points. For this specific project, merge sort will be our main source of algorithm that sorts the data from least to greatest. It will have to traverse and split the data multiple times to perform this algorithm correctly. Divide and conquer will be the algorithm that searches for the maximum gain and loss in the dataset. Fast closest pair will essentially find outliers within the dataset. 

# Code Structure
This code contains multiple aspects to accomplish the task at hand. The file loading function will read the file that is inserted and skips past the headers since we know that the program will only output the date timestamps and is sorting by closing stock prices. The merge sorting algorithm is used to recursively traverse and divide the array into subarrays to sort them back together. They will stored as a tuple, meaning that they will be stored as (date, close price). Merge sorting will function similarly to divide and conquer but it is a subset of that technique. The Kadane's algorithm will find and search for the maximum sum in the array in the stock price dataset. The closest pair function will find the closest points with the dataset and will return them. The analysis function will bring all the aspects together and form our report on the given dataset.


# How to use the system

In this bottom portion of the main code, all you have to do is insert any txt file you want to replace the "a.us.txt". This is a stock analyizer, it is reccommended to insert stock history files. Search on the web and find company stock files that contain, dates, opening prices and close prices to best use this system. You can find this by looking for the line that says: file_path = "a.us.txt"  # Add file here

![Screenshot 2024-10-20 170838](https://github.com/user-attachments/assets/eb4e2f9f-ad7b-4190-9aad-2bd336c91eac)

As for reading and understanding the results, here is a snippet and example below

![Screenshot 2024-10-20 171305](https://github.com/user-attachments/assets/c7898d77-36c9-4aeb-b7b6-32c4e22cbc40)

The system will simplify the output information significantly to make it easier to interpret for the user. So after the program reads the data and runs it through the algorithm, we will see that it is sorted by the closing prices of the stock on certain dates. It is an immensely large file containing approximately four thousand stock prices over a long period of time. We can clearly see that they slowly increased in price over time and the max price of this dataset is about $68.25. For finding out trends in the dataset, the system looks for the most amount of price increased over a extended period of time. The program compares price changes between consecutive timestamps and figures out which increas was the highest. The anomalies in this dataset are the two closest points that match each other. 

# Diagram for code
![Project1 Diagram drawio](https://github.com/user-attachments/assets/4ff68e25-95b0-44a2-ad90-67ce9aef6ce0)

# Findings discussion
From performing the necessary steps to accomplish this project. I was able to inform myself on a more applied approach of using algorithms on larger datasets. I can see this being useful if I worked at a large company and they wanted me to create a report on their financial status and if there are any trends. A challenge I faced during this process, was finding a decent dataset to work with. I was not sure about how stocks worked, so I looked at numerous websites until I stumbled upon Kaggle and they had many useful sources for huge stock dataset files. They had about half a gigabyte of just stock data so I just downloaded the whole set and picked one off the folder. If I were to improve this project in anyway, I would want to add more data into the system. Currently, I tried using the entire file but it was too large. The file I used here for this project, I had to cut down on about 25%-30% of the actual data. When I ran the program it would output an error saying that there is way too much data or it would crash. With the skills that I have now, I would want to know how to work with even larger datasets and analyze another industry to prepare myself for my future programmer career.
