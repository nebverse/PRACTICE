import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dic = {
    'Sujal kumar': 165,
    'Shashi Kumar Bhogta': 175,
    'Yash kumar': 150,
    'Ved Prakash': 175,
    'Sonu Kumar Bedia': 155,
    'SUJAL ANAND': 155,
    'Subroto Chatterjee': 170,
    'Piyush singh': 165,
    'Amrit Kumar': 170,
    'Abhay Kumar': 170,

    'Adil Ansari': 160,
    'Raja rai': 185,
    'Balvinder singh': 155,
    'Praveen Kumar ': 165,
    'Rishikesh Prasad': 170,
    'Sourav Goswami': 170,
    'Adarshbanerjee': 150,
    'Aman Poddar': 165,
    'Aarya Agrawal': 175,
    'Aakif Jawaid': 155,

    'Soyam Ranjan': 115,
    'Devanshu chatterjee': 175,
    'Shivam Kumar ': 140,
    'Nirbhay kumar singh': 160,
    'Jayesh Kumar': 170,

    'Aditi kumari': 160,
    'Vaishnavi Kumari': 170,
    'Anamika kumari': 155,
    'Nancy Perween ': 150,
    'Ishika': 155,
    'Pratiksha Singh ': 170,
    'Sweta Kumari': 180,
    'Chhaya Rani': 165,
    'Archita gangani': 155,
    'Shruti Arya ': 175,

    'Shivani Pandey': 165,
    'Saniya Ranjan ': 165,
    'Sneha shreya ': 180,
    'Shreya jha ': 160,
    'Neha Kumari': 170,
    'Khushi kumari': 170,
    'Vani sharma': 165,
    'Riya Kumari': 175,
    'Neha kumari': 170,
    'Muskan kumari': 170,

    'Suhana ray': 140,
    'Kumari kumud': 170,
    'Kriti Kumari': 185,
    'Shobha kumari': 165,
    'Parmeet Kaur Hora': 150}

# print(dic)

l1 = []
for i in dic:
    l1.append(dic[i])

# print(l1)
# print(np.max(l1))
count1 = pd.value_counts(l1)
print(count1)
Dataset2=plt.bar(count1.index,count1)
plt.xlabel("MARKS")
plt.ylabel("NO. OF STUDENTS")
plt.title("LEARNING STYLE OF 10th CLASS STUDENTS")
plt.show()
# print(np.mean(l1))