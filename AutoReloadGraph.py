import streamlit as st
from random import randint
from time import sleep
"""
# Birthday Paradox
## let's see a graph!!

"""

def generate_class():
    return[randint(1,365) for _ in range(27)]

if "experiments" not in st.session_state:
    st.session_state["experiments"] = []

st.write(generate_class())

c = generate_class()

counter = 0 

count = [c.count(i) for i in range (1, 366)]

countmap = [[0 for _ in range (31)] for _ in range (12)]

for i in range (12):
    for y in range (30):
        countmap [i][y] = count [y+30*i]

import matplotlib.pyplot as plt
import numpy as np 

a = np.random.random((16,16))

plt.imshow(countmap, cmap='hot', interpolation='nearest')
st.pyplot(plt)

there_are_collision = not len(set(c)) == len(c)

if there_are_collision: 
    st.write("there are collisions!")
else:
    st.write("there are NOT collision")

st.session_state.experiments.append(there_are_collision)

estimated_prob = st.session_state.experiments.count(True)/len(st.session_state.experiments)

st.write(estimated_prob)

import matplotlib.pyplot as plt

labels = ['Collision', 'Not collisions']
sizes = [st.session_state.experiments.count(True), 
         st.session_state.experiments.count(False)]

explode = (0.05, 0.05)

fig, ax = plt.subplots()
ax.pie(sizes, labels= labels, autopct= '%1.1f%%', shadow = True, startangle = 90, explode = explode)
ax.axis('equal')
st.pyplot(fig)


sizes = st.session_state.experiments

st.write("number of experiments so far: ", len(st.session_state.experiments))

st.button("generate antoher class")

if st.button("reset"):
    st.session_state.experiments = []

reload = st.toggle("autoreload")

def p_at_time(t):
    exps = st.session_state.experiments[:t]
    return sum(exps)/t

estimates = [p_at_time(t) for t in range (1, len(st.session_state.experiments))]

if len(estimates): 
    st.line_chart(estimates)

if reload:
    sleep(0.1)
    st.rerun()
