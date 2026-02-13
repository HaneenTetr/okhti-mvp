
import streamlit as st
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Okhti: Hero Engine", page_icon="⚡")

# --- THE HERO ENGINE LOGIC ---
def hero_engine(struggle):
    # This acts like the AI brain
    time.sleep(1) # Thinking time...
    
    # Logic for ANY input (Generic fallback that sounds smart)
    # We use this so it works even if you type something totally new
    return f"""
    ### ⚡ Agency Mode Activated
    
    **The Pivot:** You aren't just "{struggle}" — you are managing a complex operation.
    
    **1. Your New Title:** *Head of Operations & Resource Management*
    
    **2. The Business Case:** This task requires **inventory management**, **negotiation**, and **crisis resolution**. These are CEO-level skills.
    
    **3. Immediate Action:**
    * **Brand It:** Create a simple logo today.
    * **Track It:** Start a ledger to track your 'output'.
    * **Scale It:** Find one person to delegate the small tasks to.
    """

# --- THE APP INTERFACE ---
st.title("⚡ The Hero Engine")
st.write("Turn your daily struggle into a business asset.")

# The Input Box
user_input = st.text_area("What is your daily struggle?", placeholder="e.g., I help my mum sell milk...")

# The Button
if st.button("Generate Business Plan"):
    if user_input:
        result = hero_engine(user_input)
        st.success("Analysis Complete!")
        st.markdown(result)
    else:
        st.warning("Please type something first.")
