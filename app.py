import streamlit as st
from agent import CallAIAgent

# Initialize the agent
agent = CallAIAgent()

# Streamlit app
st.title("Code Quality Analyzer by DeepSeek")

# Sidebar for navigation
option = st.sidebar.selectbox(
    "Choose an option",
    ["Code Analyzer", "Code Summary", "Code Improvement", "Alternative Approach", "Full Code Analysis"]
)

if option == "Code Analyzer":
    st.header("Code Analyzer")
    code_text = st.text_area("Paste your code here:", height=300)
    if st.button("Analyze Code"):
        if code_text.strip():
            with st.spinner("Analyzing code..."):
                analysis_result = agent.analyze_code(code_text)
                st.success("Analysis Complete!")
                st.write(analysis_result)
        else:
            st.error("Please enter code to analyze.")

elif option == "Code Summary":
    st.header("Code Summary")
    code_text = st.text_area("Paste your code here:", height=300)
    if st.button("Summarize Code"):
        if code_text.strip():
            with st.spinner("Summarizing code..."):
                summary_result = agent.summarize_code(code_text)
                st.success("Summary Complete!")
                st.write(summary_result)
        else:
            st.error("Please enter code to summarize.")

elif option == "Code Improvement":
    st.header("Code Improvement")
    code_text = st.text_area("Paste your code here:", height=300)
    if st.button("Suggest Improvements"):
        if code_text.strip():
            with st.spinner("Generating suggestions..."):
                improvements = agent.suggest_improvements(code_text)
                st.success("Suggestions Generated!")
                st.write(improvements)
        else:
            st.error("Please enter code to improve.")

elif option == "Alternative Approach":
    st.header("Alternative Approach")
    code_text = st.text_area("Paste your code here:", height=300)
    if st.button("Suggest Alternative Approach"):
        if code_text.strip():
            with st.spinner("Suggesting alternative approach..."):
                alternative_approach = agent.suggest_alternative_approach(code_text)
                st.success("Alternative Approach Suggested!")
                st.write(alternative_approach)
        else:
            st.error("Please enter code to suggest an alternative approach.")

elif option == "Full Code Analysis":
    st.header("Full Code Analysis")
    input_text = st.text_area("Paste your code here:", height=300)
    if st.button("Run Full Code Analysis"):
        if input_text.strip():
            with st.spinner("Running full analysis..."):
                # Run all agents
                summary_result = agent.summarize_code(input_text)
                analysis_result = agent.analyze_code(input_text)
                improvements = agent.suggest_improvements(input_text)
                alternative_approach = agent.suggest_alternative_approach(input_text)

                # Display results in tabs
                tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Code Analysis", "Improvement Suggestions", "Alternative Approach"])

                with tab1:
                    st.subheader("Code Summary")
                    st.write(summary_result)

                with tab2:
                    st.subheader("Code Analysis")
                    st.write(analysis_result)

                with tab3:
                    st.subheader("Improvement Suggestions")
                    st.write(improvements)

                with tab4:
                    st.subheader("Alternative Approach")
                    st.write(alternative_approach)

                st.success("Full Code Analysis Complete!")
        else:
            st.error("Please enter code to analyze.")
