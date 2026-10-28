
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Industrial Monitoring",
    layout="wide"
)

st.title("Industrial Machine Monitoring")
st.caption("Prototype dashboard — simulated data")

machines = pd.DataFrame({
    "Machine": ["M01", "M02", "M03", "M04", "M05"],
    "Status": ["Running", "Running", "Idle", "Running", "Stopped"],
    "Temperature (°C)": [65.2, 71.4, 42.1, 68.7, 35.0],
    "Motor Speed (RPM)": [1200, 1450, 0, 1350, 0]
})

running = (machines["Status"] == "Running").sum()
alarms = (machines["Status"] == "Stopped").sum()

c1, c2, c3 = st.columns(3)
c1.metric("Total Machines", len(machines))
c2.metric("Running Machines", running)
c3.metric("Stopped Machines", alarms)

st.subheader("Machine Status")
st.dataframe(machines, use_container_width=True)

st.subheader("Temperature by Machine")
st.bar_chart(
    machines.set_index("Machine")["Temperature (°C)"]
)

st.caption(
    f"Dashboard opened: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)
