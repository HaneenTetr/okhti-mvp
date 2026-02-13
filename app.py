import streamlit as st
from openai import OpenAI
import os

# 1. Page Config (The Look)
st.set_page_config(page_title="Okhti: The Agency Console", page_icon="🌍", layout="wide")

# 2. The Sidebar (Your 7 Modules)
with st.sidebar:
    st.title("🚀 Okhti Console")
    st.write("*Talent is universal. Opportunity is not.*")
    selected_module = st.radio(
        "Choose your Module:", 
        ["1. The Hero Engine", "2. Test Prep & Mental Health", "3. Global Systems Navigator", 
         "4. Opportunity Door", "5. US Roadmap", "6. Mentorship Market", "7. Parents Initiative"]
    )
    st.info("Built by Haneen Elweresh in Ghana 🇬🇭")

# 3. API Setup (We will set this up in the cloud later)
# For now, we assume the key is in the secrets or environment variables
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_hero_transformation(struggle):
    """
    This function sends the struggle to the AI and returns the 'Hero' reframe.
    """
    # Placeholder for the actual API call logic
    # In the real app, we uncomment the API call below
    
    # response = client.chat.completions.create(
    #     model="gpt-4o",
    #     messages=[
    #         {"role": "system", "content": "You are the Okhti Agency Engine. Turn daily chores into high-level business logic. Output: 1. A Business Name. 2. A Professional Title. 3. Three immediate action steps to scale."},
    #         {"role": "user", "content": struggle}
    #     ]
    # )
    # return response.choices[0].message.content
    
    return f"""
    ### 🎯 Reframing: {struggle}
    
    **Your Professional Title:** Supply Chain & Logistics Director
    **Your Business Name:** 'The Daily Flow: Essential Logistics'
    
    **Why this is a business:**
    You aren't just selling milk. You are managing inventory, negotiating margins, and ensuring last-mile delivery.
    
    **🚀 Immediate Action Plan:**
    1. **Branding:** We need a logo. (AI generating...)
    2. **Sticker Strategy:** Print 50 stickers with your new name at the local shop.
    3. **Digital Ledger:** Stop using paper. Use this app to track every sale.
    """

# 4. Main Page Logic
st.title("🌍 Okhti: The Agency Engine")

if selected_module == "1. The Hero Engine":
    st.header("⚡ Turn Your Struggle into a Business")
    st.write("There is a hero inside you. Tell us what you do every day that feels like a burden.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        user_input = st.text_area("What is your daily struggle?", placeholder="Example: I help my mum sell milk every morning...")
        analyze_btn = st.button("Activate Hero Mode")
    
    with col2:
        if analyze_btn and user_input:
            with st.spinner("Reframing your reality..."):
                # Call the AI function
                result = get_hero_transformation(user_input)
                st.success("Agency Unlocked!")
                st.markdown(result)
                st.button("Generate Logo (Beta)")
                st.button("Download Business Plan")

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
        st.write("👻 **Anon_Egypt:** I got an interview! Check your spam folder.")

elif selected_module == "6. Mentorship Market":
    st.header("🤝 The Mentorship Economy")
    st.write("Book a call. Fund a sister. Learn the path.")
    st.metric(label="Mentor Split", value="80%", delta="Income for Student")
    
    st.markdown("""
    * **Haneen E.** (MBZUAI Applicant) - *Strategy & Essays* - [Book for $15]
    * **Sarah J.** (Stanford Physics) - *Research & STEM* - [Book for $20]
    """)

else:
    st.info(f"🚧 **{selected_module}** is currently under construction in the Ghana Lab.")
