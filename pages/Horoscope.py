# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# publlic url  https://steamlit-calcualtor-app-kirg4qn0qn.streamlit.app/


import streamlit as st
from streamlit.logger import get_logger

st.markdown("# Horoscope ❄️")
st.sidebar.markdown("# Horoscope  ❄️")

import streamlit as st
import requests

# Streamlit UI elements
st.title("Daily Horoscope App")

# Select the zodiac sign
zodiac_sign = st.selectbox("Select Your Zodiac Sign", [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
])

# Retrieve the daily horoscope for the selected sign

# credits to https://rapidapi.com/Alejandro99aru/api/horoscope-astrology


url = "https://horoscope-astrology.p.rapidapi.com/horoscope"

querystring = {"day":"today","sunsign":"libra"}

headers = {
	"X-RapidAPI-Key": "xxxxx",
	"X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

 
if response.status_code == 200:
    horoscope_data = response.json()
    horoscope_text = horoscope_data['horoscope']

    # Display the daily horoscope
    st.subheader(f"Today's Horoscope for {zodiac_sign}")
    st.write(horoscope_text)
else:
    st.error("Failed to fetch the horoscope data. Please try again later.")

st.divider()

st.write(
    "This is a simple Streamlit app that provides daily horoscopes based on your zodiac sign."
)




