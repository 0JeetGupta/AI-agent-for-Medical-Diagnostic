import streamlit as st
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.agent import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam

st.set_page_config(page_title="AI-Powered Medical Review", layout="wide")

st.title("🧠 AI-Powered Medical Report Analyzer")
st.markdown("""
This application uses specialized AI agents (Cardiologist, Psychologist, Pulmonologist) to analyze a patient's medical report and provide a multidisciplinary diagnosis.
""")

uploaded_file = st.file_uploader("📄 Upload a Medical Report (.txt)", type="txt")

if uploaded_file is not None:
    medical_report = uploaded_file.read().decode("utf-8")

    st.subheader("📋 Medical Report Preview")
    st.text_area("Contents:", medical_report, height=200)

    if st.button("🔍 Analyze Report"):
        with st.spinner("Running specialist analysis..."):
            agents = {
                "Cardiologist": Cardiologist(medical_report),
                "Psychologist": Psychologist(medical_report),
                "Pulmonologist": Pulmonologist(medical_report)
            }

            responses = {}
            with ThreadPoolExecutor() as executor:
                futures = {executor.submit(agent.run): name for name, agent in agents.items()}
                for future in as_completed(futures):
                    name = futures[future]
                    responses[name] = future.result()

            st.success("✅ Individual Specialist Assessments Complete!")

            for name, result in responses.items():
                st.subheader(f"🩺 {name}'s Analysis")
                st.markdown(result if result else "*No response generated.*")

            st.subheader("🧑‍⚕️ Final Multidisciplinary Team Diagnosis")
            team_agent = MultidisciplinaryTeam(
                cardiologist_report=responses["Cardiologist"],
                psychologist_report=responses["Psychologist"],
                pulmonologist_report=responses["Pulmonologist"]
            )
            final_diagnosis = team_agent.run()
            st.markdown(final_diagnosis if final_diagnosis else "*No final diagnosis generated.*")

            # Save to file
            os.makedirs("results", exist_ok=True)
            with open("results/final_diagnosis.txt", "w") as f:
                f.write(final_diagnosis or "")
