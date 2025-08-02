import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Instagram Violation & Impersonation Detector", layout="centered")

st.title("📸 Instagram Violation & Impersonation Detector")
st.write("Analyze IG profiles for simulated violations and impersonation attempts.")

# Inputs
username = st.text_input("Instagram Username", placeholder="@username")

uploaded_ss = st.file_uploader("Upload Profile Screenshot", type=["png", "jpg", "jpeg"])
uploaded_pp = st.file_uploader("Optional: Upload Profile Photo", type=["png", "jpg", "jpeg"])

# Violation simulation
all_reasons = ["Hate Speech", "Self-Harm", "Violence", "Spam", "Harassment", "Scam", "Adult Content"]

def generate_violation_report():
    chosen = random.sample(all_reasons, k=random.randint(2, 4))
    return {r: random.randint(2, 7) for r in chosen}

def check_impersonation(username, has_photo=False):
    suspicious_keywords = ["real", "official", "backup", "admin", "celeb", "support", "help", "mod"]
    chance = 0
    for word in suspicious_keywords:
        if word in username.lower():
            chance += random.randint(15, 35)

    if has_photo:
        # Slight boost if a profile photo is used (simulating detection)
        chance += random.randint(10, 20)
    else:
        chance += random.randint(5, 15)

    # Random fallback if nothing found
    if chance == 0:
        chance = random.randint(10, 30)

    chance = min(chance, 98)

    if chance > 75:
        label = "🛑 Likely impersonating a public figure or brand"
    elif chance > 40:
        label = "⚠️ Possible impersonation"
    else:
        label = "✅ No strong impersonation signs"

    return chance, label

# Run analysis
if st.button("🔍 Scan Profile"):
    if not username.strip():
        st.warning("Please enter a username.")
    elif not uploaded_ss:
        st.warning("Upload a screenshot.")
    else:
        st.success(f"Analyzing @{username}...")

        # Show images side-by-side
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(uploaded_ss), caption="Profile Screenshot", use_column_width=True)
        with col2:
            if uploaded_pp:
                st.image(Image.open(uploaded_pp), caption="Profile Photo", use_column_width=True)
            else:
                st.info("No profile photo uploaded.")

        st.markdown("### 📝 Detected Violations:")
        report_data = generate_violation_report()
        for reason, count in report_data.items():
            st.markdown(f"- ✅ **{count}× {reason}**")

        st.markdown("---")
        st.markdown("### 🕵️ Impersonation Detection:")
        chance, result = check_impersonation(username, has_photo=uploaded_pp is not None)
        st.markdown(f"**Impersonation Probability:** `{chance}%`")
        st.markdown(result)

        st.info("📌 This is a simulated tool. No real Instagram accounts are accessed.")
