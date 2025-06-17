import streamlit as st
import pandas as pd

# --------------------- CONFIG -----------------

st.set_page_config(page_title="AI career Help Bot", layout="centered")
st.title("AI Career Help Bot")
st.write("Get personalised career suggestions, college predictions and more!")

# ------------------------- INPUT FIELDS -----------------------------

exam = st.selectbox("Exam Appeared", ["JEE", "NEET", "CUET", "CET"])
category = st.selectbox("category", ["GEN", "SC", "ST", "OBC"])
interest = st.selectbox("Field of Interest", ["Tech", "Med"])
marks = st.number_input("Marks Obtained", min_value=0.0, max_value=750.0, step=1.0)
percentile = st.number_input("Percentile (if known)", min_value=0.0, max_value=100.0, step=0.1)

marks = int(marks)


# -----------------------------------------------------CORE BOT LOGIC--------------------------------------------------------------

class Counsellor:
    def __init__(self, exam, category, interest, marks):
        self.exam = exam.lower()
        self.category = category.lower()
        self.interest = interest.lower()
        self.marks = marks



    def suggest(self):
            if(self.interest == "tech" and self.exam == "jee"):
                return self._suggest_for_jee()
            elif(self.interest == "med" and self.exam == "neet"):
                return self._suggest_for_neet()
            else:
                return "! Suggestion: Go for private colleges or Try again next year"

    def _suggest_for_jee(self):
                if(self.marks >= 90):
                    return "Suggestion: Go for IITs, NITs, IIITs or Top tier GFTIs"
                elif(self.marks <= 90 and self.category in ["sc", "st", "obc"]):
                    return "Suggestion: Go for Low tier GFTIs or if belong to category still try for top tier colleges, else try other tech related courses"
                else:
                    return "Suggestion: If possible go for private colleges, else try again next year"
            

    def _suggest_for_neet(self):
           if (self.marks >= 650):
                return "Suggestion: Go for MBBS from AIIMS or Top tier GMCs"
           elif (self.marks < 650 and self.category in ["sc", "st", "obc"]):
                 return "Suggestion: Go for BDS/BHMS/BAMS or if belong to category (SC/ST/OBC) still try for AIIMS"
           else:
                return "Suggestion: Try private colleges (if possible) else try again next year"


# ------------------------- BUTTON ACTION ----------------------

if st.button("Get Career Suggestion"):
     student = Counsellor(exam, category, interest, marks)
     result = student.suggest()
     st.success(result)


# -------------------------- COLLEGE PREDICTor --------------------------
st.markdown("---")
st.header("College predictor (for Exams)")

try:
     data = pd.read_csv("cet_cutoff_sample.csv")
     if percentile > 0:
          filtered = data[
               (data['Percentile'] <= percentile) & 
               (data['Category'].str.lower() == category.lower())].sort_values(by='Percentile', ascending=False)
          st.write("### Eligible Colleges:")
          st.dataframe(filtered[['College', 'Branch', 'Percentile']])
     else:
          st.info("Enter percentile tomsee eligible colleges.")
except FileNotFoundError:
     st.warning("Cutoff data not found. Please upload 'cet_cutoff_sample.csv' to enable college predicttion.")

# -------------------------------- ROADMAP FEATURE ------------------------------------

st.markdown("---")
st.header("Self - Learning Roadmap")

if interest.lower() == "tech":
     st.markdown("""
     **Learn these in order :**
     1. Python (basics + projects)
     2. DSA
     3. Gitgub + Version Control
     4. ML (Scikit-learn, Pandas)   
     5. deep Learning (TensorFlow)
     6. Build AI projects: Chatbots, Predictive Systems, Resume Analyzers""")
else:
     st.markdown("""
                 **Parallel Medical careers to Consider :**
                 - B.sc. Nursing / BPT 
                 - B.Pharm / D.Pharm
                 - Clinical Research / Lab Technology""")
     

# -------------------- FOOTER -----------------------
st.markdown("---")
st.caption("Built by Shubham | AI CAREER Help Bot")


    
          
          










    

    

