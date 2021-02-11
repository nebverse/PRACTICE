import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# index_col ="Name"
df = pd.read_csv("Project of IGNOU 1.csv", )
df = pd.DataFrame(df)
# print(df)

df=df.drop(["Timestamp", "Total score", "Name [Score]", "Name [Feedback]", "Name of School [Score]", "Name of School [Feedback]",
            "Class, Section and Roll No. [Score]", "Class, Section and Roll No. [Feedback]",
            "Q) What's the best way for you to study for a test? [Score]", "Q) What's the best way for you to study for a test? [Feedback]",
            "Q) When you are not sure how to spell a word, what are you most likely to do? [Score]", "Q) When you are not sure how to spell a word, what are you most likely to do? [Feedback]",
            "Q) What do you find most distracting when you are trying to study? [Score]", "Q) What do you find most distracting when you are trying to study? [Feedback]",
            "Q) What do you like to do to relax? [Score]", "Q) What do you like to do to relax? [Feedback]",
            "Q) What do you find most distracting when in class? [Score]", "Q) What do you find most distracting when in class? [Feedback]",
            "Q) You have to give a presentation to your Biology class, what do you do to make yourself comfortable? [Score]", "Q) You have to give a presentation to your Biology class, what do you do to make yourself comfortable? [Feedback]",
            "Q) You are briefly stumped by a question in a physics test, but you know that you know the answer. Would you think back to ........ [Score]", "Q) You are briefly stumped by a question in a physics test, but you know that you know the answer. Would you think back to ........ [Feedback]",
            "Q) How does your favourite teacher teach? [Score]", "Q) How does your favourite teacher teach? [Feedback]",
            "Q) You have been given a group assignment at school, would you... [Score]", "Q) You have been given a group assignment at school, would you... [Feedback]",
            "Q) How much time do you spend everyday on homework? [Score]", "Q) How much time do you spend everyday on homework? [Feedback]"], axis = 1)

# print(df.shape)

# create dict for all answers

d_1 = {"Read the book or your notes and review pictures or charts." : 20,
       "Have someone ask you questions that you can answer out loud." : 15,
       "Make up index cards that you can review" : 10}

d_2 = {"Write it down to see if it looks right." : 20,
       "Spell out loud to see if it sounds right." : 15,
       "Trace the letter in the air(finger spellng)." : 10}

d_3 = {"People walking past you" : 15,
       "Loud noises" : 20,
       "An uncomfortable chair" : 10}

d_4 = {"Read" : 10,
       "Listen to music" : 20,
       "Exersice (walk run, play, sports, etc)" : 15}

d_5 = {"Lights that are too bright or to dim." : 15,
       "Noises from the hallway or outside the building (like traffic or someone cutting the glass)." : 20,
       "The temperature being too hot or too cold." : 10}

d_6 = {"Write down the key points and practice what to say again and again." : 15,
       "Write your speech, word for word and read it over and over." : 10,
       "See if you can come up with an activity or a model of your subject to show to the class." : 20}

d_7 = {"What your teacher said to you during class." : 20,
       "Reading the paragraph in your textbook." : 15,
       "The activities that you did in class and how they relate to your question." : 10,
       "A diagram from your textbook or maybe one you drew yourself." : 5}

d_8 = {"They give really interesting 'lectures' on topics that stick in your head." : 10,
       "They write up notes on the blackboard and do work out of textbooks." : 5,
       "They use activites and hand-on demonstrations." : 15,
       "They use videos and draw diagrams on the board whenever they can." : 20}

d_9 = {"Have regular conversations with your group members, either on the phone or at school." : 20,
       "Make lists of what every group member has to do before you start." : 15,
       "Just let it work itself out as you all go along." : 5,
       "Imagine what it's going to end up looking like, and make sure everyone has the same vision." : 10}

d_10 = {"Less than 2 hours." : 15,
        "2 to 4 hours." : 20,
        "more than 4 hours." : 10}


# print(df["Name"])
i=0
tsl = []
dic = {}
while i<70:
    data = df.loc[i]

    for j in d_1:
        if j == data["Q) What's the best way for you to study for a test?"]:
            tsl.append(d_1[j])

    for j in d_2:
        if j == data["Q) When you are not sure how to spell a word, what are you most likely to do?"]:
            tsl.append(d_2[j])

    for j in d_3:
        if j == data["Q) What do you find most distracting when you are trying to study?"]:
            tsl.append(d_3[j])

    for j in d_4:
        if j == data["Q) What do you like to do to relax?"]:
            tsl.append(d_4[j])

    for j in d_5:
        if j == data["Q) What do you find most distracting when in class?"]:
            tsl.append(d_5[j])

    for j in d_6:
        if j == data["Q) You have to give a presentation to your Biology class, what do you do to make yourself comfortable?"]:
            tsl.append(d_6[j])

    for j in d_7:
        if j == data["Q) You are briefly stumped by a question in a physics test, but you know that you know the answer. Would you think back to ........"]:
            tsl.append(d_7[j])

    for j in d_8:
        if j == data["Q) How does your favourite teacher teach?"]:
            tsl.append(d_8[j])

    for j in d_9:
        if j == data["Q) You have been given a group assignment at school, would you..."]:
            tsl.append(d_9[j])

    for j in d_10:
        if j == data["Q) How much time do you spend everyday on homework?"]:
            tsl.append(d_10[j])

    dic[data["Name"]] = tsl
    tsl=[]
    i+=1


# print(dic)
dic2 = {}

for n in dic:
    total_score = np.sum(dic[n])
    dic2[n] = total_score

# print(dic2)

l1 = []
for v in dic2:
    l1.append(dic2[v])

# print(max(l1))
# print(pd.value_counts(l1))
# df["Total score"] = l1  (check from here)
z=0
while z<70:
    data = df.loc[i]
    data["Total score"]  = l1[z]
    z+=1

    # print(data)
# print(np.mean(l1))

# print(dic2)
l3=[]
for i in l1:
    if i>=150 and i<=170:
        l3.append(i)

# print(pd.value_counts(l3))
# for i in dic2:
#     print(f"{i} : {dic2[i]}")

print(dic2)