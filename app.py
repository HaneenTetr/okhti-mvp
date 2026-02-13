 def get_hero_transformation(struggle):
    import time
    time.sleep(1.5) # Fake thinking time
    
    struggle_lower = struggle.lower()
    
    # 1. Crochet / Handicrafts Scenario (Includes Typo support!)
    if "crochet" in struggle_lower or "crichet" in struggle_lower or "knit" in struggle_lower:
        return """
        ### 🎯 Analysis: Manufacturing & Product Design
        
        **Your Professional Title:** Textile Production Manager
        **Your Business Name:** **'Loop & Legacy Designs'**
        
        **🧠 The Logic:**
        Crocheting isn't just a hobby. You are executing **Algorithmic Patterns** (following a pattern is code!) and managing **Raw Material Constraints** (yarn usage).
        
        **🚀 Immediate Action Plan:**
        1. **Pattern Licensing:** Don't just sell the hat; sell the *instructions* (PDF) to people in the US.
        2. **Time-Motion Study:** Measure exactly how many minutes one piece takes to calculate your true hourly wage.
        3. **Niche Branding:** "Hand-made in Ghana" is a premium label. Let's design a tag.
        """

    # 2. Milk / Selling Scenario
    elif "milk" in struggle_lower or "sell" in struggle_lower:
        return """
        ### 🎯 Analysis: Supply Chain & Logistics
        
        **Your Professional Title:** Director of Operations
        **Your Business Name:** **'PureFlow Logistics'**
        
        **🧠 The Logic:**
        You aren't just selling milk. You are managing **perishable inventory** in a high-risk environment.
        
        **🚀 Immediate Action Plan:**
        1. **Branding:** Print 'PureFlow: Fresh Daily' stickers.
        2. **Pre-Orders:** Create a WhatsApp group for customers.
        3. **Digital Record:** Log every sale here.
        """
        
    # 3. Siblings Scenario
    elif "sibling" in struggle_lower or "kid" in struggle_lower:
        return """
        ### 🎯 Analysis: Human Resource Management
        
        **Your Professional Title:** Head of Operations & Team Lead
        **Your Business Name:** **'Harmony Guardians'**
        
        **🧠 The Logic:**
        Managing multiple stakeholders with competing needs requires **High-Level Negotiation**.
        
        **🚀 Immediate Action Plan:**
        1. **Delegation:** Assign roles to older siblings.
        2. **Incentive Structure:** Create a 'Star Chart' economy.
        """

    # Fallback
    else:
        return """
        ### 🎯 Analysis: Strategic Problem Solving
        **Identity:** Systems Analyst. 
        **Logic:** You are identifying bottlenecks in daily life.
        **Action:** Document the 3 hardest parts of this task and digitize them.
        """f
