import streamlit as st
import random
from datetime import date

# --- CONFIGURATION ---
st.set_page_config(page_title="Okhti: Agency Console", page_icon="🌍", layout="wide")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🚀 Okhti Console")
    st.write("Your Gateway to Global Opportunity.")
    
    menu = st.radio(
        "Select Module:", 
        ["1. ACT/SAT & Mental Prep", 
         "2. Global Systems (IB/AP/A-Level)", 
         "3. English Skills Lab", 
         "4. The Opportunity Door", 
         "5. US Admissions Roadmap", 
         "6. Mentorship Market"]
    )
    st.info("Status: Online 🟢")

# --- MODULE 1: ACT/SAT & MENTAL PREP ---
if menu == "1. ACT/SAT & Mental Prep":
    st.header("🧠 Standardized Test & Mindset Hub")
    
    tab1, tab2 = st.tabs(["📚 Test Strategy", "🧘 Mental Breakdown Support"])
    
    with tab1:
        st.subheader("Daily Tip Generator")
        if st.button("Get SAT Tip of the Day"):
            tips = [
                "SAT Reading: Read the introduction blurb first. It gives context!",
                "ACT Science: Don't read the passage; go straight to the graphs.",
                "Math: Plug in the answer choices if you get stuck on algebra.",
                "Writing: Shorter is usually better. Avoid redundancy."
            ]
            st.success(random.choice(tips))
            
    with tab2:
        st.subheader("Panic Button")
        st.write("School is hard. If you are feeling overwhelmed, click below.")
        if st.button("I am having a breakdown"):
            st.warning("🛑 STOP. Take a deep breath.")
            st.markdown("""
            1. **Inhale** for 4 seconds.
            2. **Hold** for 7 seconds.
            3. **Exhale** for 8 seconds.
            
            *Remember: One test score does not define your worth. You are building a life, not just a resume.*
            """)

# --- MODULE 2: GLOBAL SYSTEMS NAVIGATOR ---
elif menu == "2. Global Systems (IB/AP/A-Level)":
    st.header("🌐 Global Education Decoder")
    st.write("Understand the difference between international tracks.")
    
    system = st.selectbox("Select a System to Analyze:", ["Select...", "A-Levels", "IB (International Baccalaureate)", "AP (Advanced Placement)", "National Curriculum"])
    
    if system == "A-Levels":
        st.info("**Structure:** Specialized. You choose 3-4 subjects.")
        st.write("**Best For:** Students who know exactly what they want to study (e.g., Medicine, Engineering).")
        st.write("**Schools in Ghana:** T.I. Ahmadiyya, Ghana International School.")
        
    elif system == "IB (International Baccalaureate)":
        st.info("**Structure:** Holistic. You take 6 subjects + Theory of Knowledge + CAS.")
        st.write("**Best For:** Students who want a broad, rigorous education and writing skills.")
        st.write("**Schools in Ghana:** Lincoln Community School, SOS-HGIC.")
        
    elif system == "AP (Advanced Placement)":
        st.info("**Structure:** US-style college courses taken in high school.")
        st.write("**Best For:** Applying to the US. Shows you can handle college rigor.")

# --- MODULE 3: ENGLISH SKILLS LAB ---
elif menu == "3. English Skills Lab":
    st.header("🗣️ English Mastery Center")
    
    level = st.select_slider("What is your estimated current level?", options=["A1", "A2", "B1", "B2", "C1", "C2"])
    
    if st.button("Generate Resource Pack"):
        st.subheader(f"Recommended Plan for {level}:")
        if level in ["A1", "A2"]:
            st.write("1. **Duolingo:** 15 mins/day (Strict Streak).")
            st.write("2. **YouTube:** Watch 'Easy English' cartoons.")
        elif level in ["B1", "B2"]:
            st.write("1. **BBC Learning English:** 1 article per day.")
            st.write("2. **Netflix:** Watch shows with English Subtitles.")
            st.write("3. **Exam:** Prepare for Duolingo English Test (DET).")
        else:
            st.write("1. **Podcasts:** Listen to 'The Daily' or 'TED Radio Hour'.")
            st.write("2. **Reading:** Read 1 New York Times article daily.")
            st.write("3. **Exam:** You are ready for the SAT Reading section.")

# --- MODULE 4: THE OPPORTUNITY DOOR ---
elif menu == "4. The Opportunity Door":
    st.header("🚪 Fully Funded Opportunities")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(" scholarship Database")
        st.dataframe({
            "Opportunity": ["Mastercard Foundation", "UWC Movement", "African Leadership Academy", "Yale Young African Scholars"],
            "Deadline": ["Sept 2026", "Nov 2026", "Jan 2027", "Feb 2027"],
            "Type": ["Full Ride University", "High School", "2-Year Program", "Summer Camp"]
        })
    
    with col2:
        st.subheader("💬 Anon Chat")
        st.text_input("Username (Hidden)", "Anon_Girl")
        msg = st.text_input("Ask a question...")
        if st.button("Post"):
            st.write(f"**You:** {msg}")
        st.markdown("---")
        st.caption("**Anon_Accra:** Did anyone get the ALA email yet?")
        st.caption("**Anon_Kumasi:** Not yet. They said Friday.")

# --- MODULE 5: US ADMISSIONS ROADMAP ---
elif menu == "5. US Admissions Roadmap":
    st.header("🗺️ The US Application Timeline")
    
    grade = st.selectbox("I am currently in:", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
    
    if st.button("Show My Roadmap"):
        if grade == "Grade 9":
            st.success("✅ **Goal:** Exploration")
            st.checkbox("Join 1 meaningful club")
            st.checkbox("Read books for pleasure (Build Vocab)")
            st.checkbox("Keep grades high (GPA starts now)")
        elif grade == "Grade 11":
            st.success("🔥 **Goal:** The Crucial Year")
            st.checkbox("Take the SAT/ACT (Spring)")
            st.checkbox("Ask 2 teachers for recommendations")
            st.checkbox("Start drafting the Common App Essay")
        elif grade == "Grade 12":
            st.success("🚀 **Goal:** Execution")
            st.checkbox("Submit Early Action (Nov 1)")
            st.checkbox("Complete CSS Profile (Financial Aid)")
            st.checkbox("Check email daily for interviews")

# --- MODULE 6: MENTORSHIP MARKET ---
elif menu == "6. Mentorship Market":
    st.header("🤝 Peer-to-Peer Mentorship")
    st.write("Book a sister who has walked this path. 80% of fee goes to her.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Felix", width=100)
        st.markdown("**Sarah (Stanford)**")
        st.caption("Expertise: Physics & Engineering")
        st.button("Book Sarah ($15)")
        
    with col2:
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Aneka", width=100)
        st.markdown("**Amina (Ashesi)**")
        st.caption("Expertise: Essays & Storytelling")
        st.button("Book Amina ($10)")
        
    with col3:
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Bella", width=100)
        st.markdown("**Fatima (Yale)**")
        st.caption("Expertise: Financial Aid (CSS)")
        st.button("Book Fatima ($20)")

# --- DEFAULT / WELCOME ---
else:
    st.write("Welcome to Okhti. Select a module from the sidebar.")
