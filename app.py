import streamlit as st
import time

# 1. Page Config
st.set_page_config(page_title="Okhti: The Agency Console", page_icon="🌍", layout="wide")

# 2. The Sidebar
with st.sidebar:
    st.title("🚀 Okhti Console")
    st.write("*Talent is universal. Opportunity is not.*")
    selected_module = st.radio(
        "Choose your Module:", 
        ["1. The Hero Engine", "2. Test Prep & Mental Health", "3. Global Systems Navigator", 
         "4. Opportunity Door", "5. US Roadmap", "6. Mentorship Market", "7. Parents Initiative"]
    )
    st.success("System Status: Online 🟢")
    st.info("Built by Haneen Elweresh in Ghana 🇬🇭")

# 3. The 'Fake' AI Logic (The Simulator)
def get_hero_transformation(struggle):
    # This simulates AI thinking time
    time.sleep(2) 
    
    struggle_lower = struggle.lower()
    
    # Scenario A: The Milk Seller
    if "milk" in struggle_lower or "sell" in struggle_lower:
        return """
        ### 🎯 Analysis: Supply Chain & Logistics
        
        **Your Professional Title:** Director of Operations & Inventory Management
        **Your Business Name:** **'PureFlow Logistics'**
        
        **🧠 The Logic:**
        You aren't just selling milk. You are managing **perishable inventory** in a high-risk environment. You calculate margins, manage customer relations, and handle last-mile delivery.
        
        **🚀 Immediate Action Plan:**
        1. **Branding:** Print 'PureFlow: Fresh Daily' stickers at the local shop (Cost: 5 Cedis).
        2. **Optimization:** Create a WhatsApp group for your top 5 customers for 'Pre-Orders' to reduce waste.
        3. **Digital Record:** Use this app to log daily revenue.
        """
    
    # Scenario B: Taking care of siblings
    elif "sibling" in struggle_lower or "brother" in struggle_lower or "sister" in struggle_lower:
        return """
        ### 🎯 Analysis: Human Resource Management
        
        **Your Professional Title:** Head of Conflict Resolution & Team Lead
        **Your Business Name:** **'Harmony Guardians'**
        
        **🧠 The Logic:**
        Managing multiple stakeholders (siblings) with competing needs (food, attention) requires **High-Level Negotiation** and **Crisis Management**.
        
        **🚀 Immediate Action Plan:**
        1. **Delegation:** Assign specific roles to older siblings (Systematize the workforce).
        2. **Incentive Structure:** Create a 'Star Chart' economy for good behavior.
        3. **Skill Translation:** Add 'Conflict Mediation' to your Okhti Resume.
        """
        
    # Fallback for anything else
    else:
        return """
        ### 🎯 Analysis: Strategic Problem Solving
        
        **Your Professional Title:** Systems Analyst
        **Your Business Name:** **'Impact Solutions'**
        
        **🧠 The Logic:**
        You are identifying bottlenecks in daily life and finding resource-efficient solutions. This is the core of **Entrepreneurship**.
        
        **🚀 Immediate Action Plan:**
        1. **Document:** Write down the 3 hardest parts of this task.
        2. **Digitize:** How can a simple tool make this faster?
        3. **Scale:** Can you teach someone else to do it?
        """

# 4. Main Page Layout
st.title("🌍 Okhti: The Agency Engine")

if selected_module == "1. The Hero Engine":
    st.header("⚡ Turn Your Struggle into a Business")
    st.write("There is a hero inside you. Tell us what you do every day that feels like a burden.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Pre-fill the box so you don't even have to type in the video if you don't want to
        user_input = st.text_area("What is your daily struggle?", placeholder="Example: I help my mum sell milk every morning...")
        analyze_btn = st.button("Activate Hero Mode")
    
    with col2:
        if analyze_btn and user_input:
            with st.spinner("Connecting to Agency Engine..."):
                result = get_hero_transformation(user_input)
                st.success("Agency Unlocked!")
                st.markdown(result)
                st.button("Generate Logo (Beta)")

elif selected_module == "4. Opportunity Door":
    st.header("🚪 The Opportunity Door")
    st.write("Real-time, anonymous transparency for global scholarships.")
    tab1, tab2 = st.tabs(["Fully Funded Database", "Anonymous Chat"])
    with tab1:
        st.dataframe({"Scholarship": ["MBZUAI", "TAL Fellowship", "Rise Global"], "Deadline": ["Feb 28", "Rolling", "Jan 15"], "Status": ["Open", "Reviewing", "Closed"]})
    with tab2:
        st.text_input("Post anonymously:", placeholder="Has anyone heard back from TAL yet?")
        st.write("---")
        st.write("👻 **Anon_Ghana:** Still waiting. Rejection emails usually come on Fridays.")

elif selected_module == "7. Parents Initiative":
    st.header("👨‍👩‍👧 The Compound Initiative")
    st.write("Show your parents the ROI (Return on Investment) of Education.")
    investment = st.slider("Hours spent on Okhti per week:", 1, 20, 5)
    roi = investment * 52 * 15 
    st.metric(label="Projected Annual Earning Potential (Future)", value=f"${roi} USD")
    st.success(f"By investing {investment} hours a week, you increase future security by 300%.")

else:
    st.info(f"🚧 **{selected_module}** is currently being built in the Ghana Lab.")
