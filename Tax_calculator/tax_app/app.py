import streamlit as st
from tax_laws timport TAX_LAWS

st.set_page_config(page_title="Search Tax and the calculator",layout="centered")

st.title("Search Tax & the calculator")


# --- Searching tax law ---
st.header("search tax")
keyword =st.text_input("Type your keywords (e.g. 간주임대료, 의제매입세액공제 등)")
if keyword:
  result = TAX_LAWS.get(keyword.strip())
  if reult:
    st.success(result)
  else:
    st.warning("해당 키워드에 대한 설명이 없습니다.")


# ---  Calculator for 간주임대료 ---
st.header("A calculator for 간주임대료")
deposit = st.number_input("보증금 (원)", step=100000, format="%d")
days = st.number_input("보유일수",step=1)
rate 0.031 #2025년 기준 이자율

if deposit>0 and days>0:
  income = deposit * rate * (days/365)
  st.info(f"간주임대료: {income:,.0f} 원")
  
          
