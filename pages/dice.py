import streamlit as st
import random

st.markdown("# Dice Game ❄️")
st.sidebar.markdown("# Dice Game  ❄️")

import streamlit as st
import random
import os
from PIL import Image

current_directory = os.getcwd()

# Dictionary to map dice roll results to image URLs
dice_images = {
    0: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-0.png",
    1: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-1.png",
    2: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-2.png",
    3: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-3.png",
    4: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-4.png",
    5: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-5.png",
    6: "D:\MY WORK\PYTHON\Streamlit\steamlit-calcualtor-app\pages\images\dice\Dicey-6.png"
}
# Radio button to select the number of dice
dice_choice = st.radio("Select the number of dice", ["Single", "Double"])

# Function to roll a single die
def roll_single_die():
    dice_roll = random.randint(0, 6)
    image = Image.open(dice_images[dice_roll])
    st.image(image, caption=f"Dice {dice_roll}", width=200)
    if dice_roll == 1:
       st.balloons()

# Function to roll two dice
def roll_double_dice():
    col1, col2 = st.columns(2)
    dice_roll1 = random.randint(0, 6)
    dice_roll2 = random.randint(0, 6)
    c= dice_roll1 + dice_roll2
    #st.write(c)
    image1 = Image.open(dice_images[dice_roll1])
    image2 = Image.open(dice_images[dice_roll2])
    col1.image(image1, caption=f"Dice {dice_roll1}", width=200)
    col2.image(image2, caption=f"Dice {dice_roll2}", width=200)
    if c == 1:
       st.balloons()


# Button to roll the dice based on the user's choice
if st.button("Roll the Dice"):
    if dice_choice == "Single":
        roll_single_die()
    elif dice_choice == "Double":
        roll_double_dice()



st.write(
    "Select the number of dice and click the button to roll the dice."
)
