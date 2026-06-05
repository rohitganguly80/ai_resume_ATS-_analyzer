import streamlit as st

from parser.resume_parser import extract_resume_text
from parser.jd_parser import extract_jd_text
from reports.pdf_generator import generate_resume_pdf
from ai.ats_service import generate_ats_report
from ai.interview_service import generate_interview_questions
from ai.roadmap_service import generate_roadmap
from ai.cover_letter_service import generate_cover_letter
from ai.resume_rewriter_service import rewrite_resume
from database.db import (
    create_table,
    save_analysis,
    get_all_analysis
)

from services.dashboard_service import (
    calculate_insights
)

import plotly.express as px
import re


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Resume ATS Analyzer",
    layout="wide"
)
create_table()

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.stButton > button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-weight:bold;
}

.stTabs [data-baseweb="tab"]{
    font-size:16px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("AI Resume ATS Analyzer")
st.markdown(
    "Upload your Resume and Job Description to get ATS insights, interview questions, roadmap, resume improvements and cover letter generation."
)

# ---------------------------------------------------
# RESUME UPLOAD
# ---------------------------------------------------

st.subheader("📄 Resume Upload")

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if resume_file:
    resume_text = extract_resume_text(resume_file)

# ---------------------------------------------------
# JD INPUT
# ---------------------------------------------------

st.subheader("Job Description")

jd_option = st.radio(
    "Choose JD Input Method",
    ["Upload PDF", "Paste JD Text"],
    horizontal=True
)

jd_text = ""

if jd_option == "Upload PDF":

    jd_file = st.file_uploader(
        "Upload Job Description PDF",
        type=["pdf"],
        key="jd_upload"
    )

    if jd_file:
        jd_text = extract_jd_text(jd_file)

        if not jd_text.strip():
            st.warning(
                "Could not extract text from PDF. Please paste the Job Description manually."
            )

elif jd_option == "Paste JD Text":

    jd_text = st.text_area(
        "Paste Job Description Here",
        height=300
    )

# ---------------------------------------------------
# MAIN FEATURES
# ---------------------------------------------------

if resume_text:

    tabs = st.tabs([
    " ATS Analysis",
    " Resume Rewrite",
    " Interview Questions",
    " Improvement Roadmap",
    " Cover Letter",
    " Insights Dashboard"
])

    # ---------------------------------------------------
    # ATS ANALYSIS
    # ---------------------------------------------------

    with tabs[0]:
        st.subheader("ATS Analysis")

        if st.button("Analyze Resume", key="ats"):

            if not jd_text.strip():

                st.error(
                    "Please upload or paste a Job Description."
                )

            else:

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    result = generate_ats_report(
                        resume_text,
                        jd_text
                    )

                st.success(
                    "Analysis Completed"
                )

                st.markdown(result)

                ats_score = 0
                match_percentage = 0

                ats_match = re.search(
                    r'ATS Score.*?(\d+)',
                    result,
                    re.IGNORECASE
                )

                match_match = re.search(
                    r'(Match|Skill Match).*?(\d+)',
                    result,
                    re.IGNORECASE
                )

                if ats_match:
                    ats_score = int(
                        ats_match.group(1)
                    )

                if match_match:
                    match_percentage = int(
                        match_match.group(2)
                    )

                save_analysis(
                    resume_file.name,
                    ats_score,
                    match_percentage
                )

    # ---------------------------------------------------
    # RESUME REWRITE
    # ---------------------------------------------------

    with tabs[1]:
        st.subheader("Resume Rewriter")

        if st.button("Rewrite Resume", key="rewrite"):

            with st.spinner("Improving Resume..."):
                rewritten_resume = rewrite_resume(resume_text)

            st.success("Resume Improved")
            st.markdown(rewritten_resume)

            pdf_file = generate_resume_pdf(rewritten_resume)

            st.download_button(
                label="Download Improved Resume PDF",
                data=pdf_file,
                file_name="improved_resume.pdf",
                mime="application/pdf"
            )

    # ---------------------------------------------------
    # INTERVIEW QUESTIONS
    # ---------------------------------------------------

    with tabs[2]:
        st.subheader("Interview Questions")

        if st.button("Generate Questions", key="interview"):

            if not jd_text.strip():
                st.error("Please upload or paste a Job Description.")

            else:
                with st.spinner("Generating Questions..."):
                    result = generate_interview_questions(resume_text, jd_text)

                st.success("Questions Generated")
                st.markdown(result)

    # ---------------------------------------------------
    # ROADMAP
    # ---------------------------------------------------

    with tabs[3]:
        st.subheader("Improvement Roadmap")

        if st.button("Generate Roadmap", key="roadmap"):

            if not jd_text.strip():
                st.error("Please upload or paste a Job Description.")

            else:
                with st.spinner("Generating Roadmap..."):
                    result = generate_roadmap(resume_text, jd_text)

                st.success("Roadmap Generated")
                st.markdown(result)

    # ---------------------------------------------------
    # COVER LETTER
    # ---------------------------------------------------

    with tabs[4]:
        st.subheader("Cover Letter Generator")

        if st.button("Generate Cover Letter", key="cover"):

            if not jd_text.strip():
                st.error("Please upload or paste a Job Description.")

            else:
                with st.spinner("Generating Cover Letter..."):
                    result = generate_cover_letter(resume_text, jd_text)

                st.success("Cover Letter Generated")
                st.markdown(result)

    with tabs[5]:
        st.subheader("ATS Insights Dashboard")

        df = get_all_analysis()

        if not df.empty:
            insights = calculate_insights(df)

            c1, c2, c3, c4, c5 = st.columns(5)

            c1.metric(
                "Total Analyses",
                insights["total"]
            )

            c2.metric(
                "Average ATS",
                insights["avg_ats"]
            )

            c3.metric(
                "Average Match %",
                insights["avg_match"]
            )

            c4.metric(
                "Best ATS",
                insights["best_ats"]
            )

            c5.metric(
                "Predicted Next ATS",
                insights["prediction"]
            )

            st.divider()

            fig1 = px.line(
                df,
                x="analysis_date",
                y="ats_score",
                markers=True,
                title="ATS Score Trend"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

            fig2 = px.bar(
                df,
                x="resume_name",
                y="match_percentage",
                color="match_percentage",
                title="Match Percentage Comparison"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

            fig3 = px.scatter(
                df,
                x="ats_score",
                y="match_percentage",
                color="resume_name",
                size="ats_score",
                title="ATS Score vs Match Percentage"
            )

            st.plotly_chart(
                fig3,
                use_container_width=True
            )

            st.subheader("Analysis History")

            st.dataframe(
                df,
                use_container_width=True
            )

        else:
            st.info(
                "No ATS history available yet."
            )

else:
    st.info("Please upload your Resume to begin.")