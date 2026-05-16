import asyncio
import streamlit as st
from runner import run_query

st.set_page_config(
    page_title="Travel Intelligence",
    page_icon="",
    layout="centered"
)

st.title(" Multi-Agent Travel Intelligence")
st.divider()

col1, col2, col3 = st.columns(3)
col1.metric(" Orchestrator", "1 agent")
col2.metric(" Weather", "wttr.in")
col3.metric(" Budget ·  Transport", "Free APIs")

st.divider()
st.markdown("**Try an example:**")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button(" Tokyo 5 days"):
        st.session_state.query = \
        "I'm traveling from Frankfurt to Tokyo for 5 days. What's the weather, budget and local transport?"
with col2:
    if st.button(" Iceland 10 days"):
        st.session_state.query = \
        "What's the minimum budget to travel from Germany to Iceland for 10 days? Also local transport?"
with col3:
    if st.button(" Morocco 7 days"):
        st.session_state.query = \
        "I want to travel from Germany to Morocco for 7 days. Give me weather, budget and local transport."

st.divider()

query = st.text_input(
    "Or type your own question:",
    value=st.session_state.get("query", ""),
    placeholder="e.g. Plan my 5 day trip from Frankfurt to Tokyo"
)

if st.button(" Get Travel Intelligence", type="primary") and query:
    with st.spinner("Agents working..."):
        st.info(" Orchestrator →  Weather ·  Budget ·  Transport")
        result = asyncio.run(run_query(query))
    st.success(" Done!")
    st.markdown("###  Travel Report")
    st.markdown(result)
    st.divider()
    st.caption("Agents: Orchestrator | Weather Agent | Budget Agent | Transport Agent")