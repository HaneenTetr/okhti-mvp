import streamlit as st
from openai import OpenAI
import os

# --- 1. CONFIGURATION & STYLE ---
st.set_page_config(page_title="Okhti Agency", page_icon="🌍", layout="wide")

st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #2E86C1;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }
    .stTextArea>div>div>textarea {
        background-color: #ffffff;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    h1 {
        color: #1B4F72;
        font-family: 'Helvetica', sans-serif;
    }
    h2, h3 {
        color: #2874A6;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. THE BRAIN (OpenAI Connection) ---
api_key = st.secrets.get("OPENAI_API_KEY")
client = None

if api_key:
    client = OpenAI(api_key=api_key)
else:
    st.warning("⚠️ SYSTEM ALERT: OpenAI API Key not found. The AI Brain is offline.")

# --- 3. INTELLIGENCE FUNCTIONS ---
def ask_gpt(system_prompt, user_input):
    if not client:
        return "⚠️ **AI Offline:** Please add your API Key to Streamlit Secrets."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("OKHTI CONSOLE")
    st.markdown("**The Agency Operating System**")
    st.markdown("---")
    
    menu = st.radio(
        "Select Module:", 
        ["1. Hero Engine (Business)", 
         "2. SAT/ACT & Mental Prep", 
         "3. Global Systems Navigator", 
         "4. Opportunity Door", 
         "5. US Roadmap Generator", 
         "6. Mentorship Market"]
    )
    st.markdown("---")
    st.caption("v1.0 | Built in Ghana 🇬🇭")

# --- 5. MAIN APP LOGIC ---

# === MODULE 1: THE HERO ENGINE ===
if menu == "1. Hero Engine (Business)":
    st.title("⚡ The Hero Engine")
    st.subheader("Turn your daily struggle into a global business.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.info("💡 **Concept:** You don't need extracurriculars. Your life IS the business case.")
        struggle = st.text_area("What is your daily responsibility?", height=150, 
                              placeholder="e.g., I help my mum sell milk, I take care of 5 siblings, I crochet hats...")
        
        if st.button("Activate Agency Mode"):
            if struggle:
                with st.spinner("Analyzing Supply Chain & Economics..."):
                    prompt = """
                    You are a top-tier Venture Capitalist and Career Strategist. 
                    Take the user's daily struggle and reframe it as a sophisticated business operation.
                    
                    Output Structure:
                    1. **The Pivot:** One sentence changing the perspective.
                    2. **Professional Title:** Give them a corporate title based on the task.
                    3. **Business Logic:** Explain the hard skills involved (logistics, negotiation, etc.).
                    4. **3-Step Execution Plan:** Concrete steps to brand and scale this TODAY.
                    """
                    result = ask_gpt(prompt, struggle)
                    st.session_state['hero_result'] = result
            else:
                st.error("Please enter a struggle first.")

    with col2:
        if 'hero_result' in st.session_state:
            st.markdown("### 🚀 Your Agency Profile")
            st.markdown(st.session_state['hero_result'])
            st.success("Strategy Generated.")

# === MODULE 2: TEST PREP ===
elif menu == "2. SAT/ACT & Mental Prep":
    st.title("🧠 Test Prep & Mental Resilience")
    
    tab1, tab2 = st.tabs(["Study Strategy", "Mental Breakdown Support"])
    
    with tab1:
        topic = st.text_input("What specific topic are you stuck on?", placeholder="e.g., Quadratic Equations")
        if st.button("Generate Micro-Lesson"):
            prompt = "You are an expert tutor. Explain this concept simply for a student, then give 1 trick to remember it."
            st.markdown(ask_gpt(prompt, topic))
            
    with tab2:
        st.write("Feeling overwhelmed? Talk to the AI Counselor.")
        vent = st.text_area("How are you feeling?", placeholder="I'm panicking about the exam tomorrow...")
        if st.button("Get Support"):
            prompt = "You are a supportive, empathetic mental health companion. Validate their feelings and give one breathing exercise."
            st.markdown(ask_gpt(prompt, vent))

# === MODULE 5: US ROADMAP ===
elif menu == "5. US Roadmap Generator":
    st.title("🗺️ US Admissions Roadmap")
    
    col1, col2 = st.columns(2)
    with col1:
        grade = st.selectbox("Current Grade:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12/Gap Year"])
        english = st.selectbox("English Level:", ["Beginner", "Intermediate (B1/B2)", "Advanced (C1/C2)"])
        
    if st.button("Generate My Checklist"):
        with st.spinner("Mapping your future..."):
            prompt = f"Create a strict, bulleted checklist for a student in {grade} with {english} English level who wants to study in the US."
            st.markdown(ask_gpt(prompt, "Generate Roadmap"))

else:
    st.title(f"🚧 {menu}")
    st.write("This module is currently being engineered.")
