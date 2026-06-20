import streamlit as st

from agent import run_agent

st.set_page_config(page_title="Agent Observability Demo")
st.title("Agent Observability Demo")
st.caption("Every run here traces to LangSmith automatically (via env vars).")

break_mode = st.checkbox("Inject error (ask about Atlantis)")
default_query = "What's the weather in Atlantis?" if break_mode else "What's the weather in Paris?"
query = st.text_input("Ask the agent", value=default_query)

if st.button("Run agent"):
    with st.spinner("Running..."):
        try:
            response = run_agent(query)
            st.success(response)
        except Exception as e:
            st.error(f"Agent failed: {e}")
    st.info("Check your LangSmith project dashboard to see this run's trace.")
