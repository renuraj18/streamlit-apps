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

st.markdown("# Calculator ❄️")
st.sidebar.markdown("# calculator  ❄️")

a=st.number_input("Enter number 1")
b=st.number_input("Enter number 2")
def add(num1,num2):
  result= num1 + num2
  return result
def sub(num1,num2):
  result= num1 - num2
  return result
def mul(num1,num2):
  result= num1 * num2
  return result
def div(num1,num2):
    if num2 == 0:
      return "cannot be 0"
    else:
      result= num1 / num2
      return result
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1:
  if st.button("\+"):
      c=add(a,b)
      st.write(c)
with col2:
  if st.button("\-"):
      c=sub(a,b)
      st.write(c)
with col3:   
  if st.button("\*"):
      c=mul(a,b)
      st.write(c)
with col4:
  if st.button("/"):
      c=div(a,b)
      st.write
st.divider()

st.caption('Developed by Renuraj')
st.caption(':blue[renuraj18@gmail.com] :sunglasses:')
st.write("**Add your own comment:**")
form = st.form("comment")
name = form.text_input("Name")
comment = form.text_area("Comment")
submit = form.form_submit_button("Add comment")

