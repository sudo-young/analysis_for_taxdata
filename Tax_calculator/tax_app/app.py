import streamlit as st
from tax_laws import TAX_LAWS
from tax_income import calculate_taxable_income, calculate_income_tax

st.set_page_config(page_title="Search Tax and the calculator",layout="centered")

st.title("Search Tax & the calculator")


# --- 세법 검색 ---
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



# --- 종합소득세 과세표준  & 세액 계산기 --
st.header("종합소득세 과세표준 계산기")

# input
total_income = st.number_input("총수입금액(원)",step=1000000,format="%d")
expenses = st.number_input("필요경비(원)",step=1000000,format="%d")
dependents = st.number_input("부양가족 수(본인제외)",min_value=0,step=1)

# income_account = total_income - expenses
# basic_deduction = 1500000 #기본공제
# personal_deduction = 1500000(1 + dependents) # 본인 + 가족당 150만원
# taxable_base = income_amount - personal_deduction


# calculate
if total_income>0 and expenses >= 0:
  taxable_base, income_amount, total_deduction = calculate_taxable_income(total_income, expenses, dependents)
  tax = calculate_income_tax(taxable_base)

  st.subheader("결과")
  st.write(f"소득금액: {income_amount:,.0f}원")
  st.write(f"소득공제 합계: {personal_deduction:,.0f}원")
  st.write(f"과세표준: {max(taxable_base,0):,.0f}원")
  st.success(F"예상종합소득세:{tax:,.0f} 원")
  st.info("이 계산 결과는 단순 참조용일뿐 법적인 공식적 효력은 가지지 않습니다. ")
  



