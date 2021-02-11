import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dic = {
        "Aman chandra" : 170,
        "Prashant Kumar" : 165,
        "Rohit Kumar" : 180,
        "Gopal Prasad" : 160,
        "Rhythm kronch" : 160,
        "Aditya tiwari" : 185,
        "Rishav Raj" : 170,
        "Sami Kumar Singh"  : 175,
        "Satyam kumar" : 160,
        "Nikhil Kumar Gupta"  : 170,
        "Sumit Agarwal" : 165,
        "KAIF Khurshid"  : 170,
        "Vinit Pathak" : 165,
        "Rishi Raj" : 175,
        "Gaurav Kumar Singh" : 180,
        "Himanshu Kumar" : 150,
        "Lucky" : 170,
        "Mayank Jha" : 170,
        "Rahul singh" : 170,
        "Abhishek Kumar" : 165,
        "Gourav Kumar" : 175,
        "Harsh Anandan Nair" : 170,
        "Arnav Ashwin" : 165,
        "Utkarsh Singh" : 160,
        "Ayush priyadarshi" : 170,
        "Rashi Raj" : 170,
        "Muskan parween" : 175,
        "Ritika Raj" : 165,
        "Riddhi gupta" : 175,
        "Priya kumari"  : 140,
        "Shikha Singh" : 155,
        "Akanksha"  : 175,
        "Dhwani mishra" : 145,
        "Tanisha khandelwal" : 185,
        "Ritika" : 175,
        "Anjali sharma" : 165,
        "Soumya" : 150,
        "Anjali kumari"  : 150,
        "Riya kumari"  : 165,
        "Puja mehta" : 175,
        "Shreya kumari" : 165,
        "Priya Kumari" : 150,
        "Shrima Goswami"  : 160,
        "RIYA KUMARI" : 165,
        "Gauri upadhyay"  : 150,
        "Shruti" : 180,
        "Twasta kumari" : 185,
        "Soumya Gautam" : 140,
        "Anjali Kumari" : 170,
        "Ishita Kapoor" : 155}

# print(dic)

l1 = []
for i in dic:
    l1.append(dic[i])

# print(l1)
# print(np.max(l1))
count = pd.value_counts(l1)
print(count)
Dataset1 = plt.bar(count.index,count)
plt.xlabel("MARKS")
plt.ylabel("NO. OF STUDENTS")
plt.title("LEARNING STYLE OF 10th CLASS STUDENTS")
# plt.show()
# print(np.mean(l1))