import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Instagram Violation Scanner", layout="centered")

st.title("📸 Instagram Violation & Impersonation Detector")
st.write("Analyze IG profiles for simulated violations and impersonation attempts.")

# Input
username = st.text_input("Instagram Username", placeholder="@username")

uploaded_file = st.file_uploader("Upload Screenshot (Profile/Post)", type=["png", "jpg", "jpeg"])

# Violation reasons (ensure always 2–4 reports)
all_reasons = ["Hate Speech", "Self-Harm", "Violence", "Spam", "Harassment", "Scam", "Adult Content"]

def generate_violation_report():
    chosen = random.sample(all_reasons, k=random.randint(2, 4))
    report_data = {r: random.randint(2, 7) for r in chosen}
    return report_data

def check_impersonation(username):
    # Simple logic for impersonation percentage
    suspicious_keywords = ["real", "official", "backup", "admin", "celeb", "support", "help", "mod"]
    chance = 0
    for word in suspicious_keywords:
        if word in username.lower():
            chance += random.randint(15, 35)

    # Random base chance if nothing suspicious
    if chance == 0:
        chance = random.randint(5, 25)
    else:
        chance += random.randint(10, 30)

    # Cap chance
    chance = min(chance, 95)

    # Return label
    if chance > 70:
        label = "🛑 Likely impersonating a public figure or brand"
    elif chance > 40:
        label = "⚠️ Possible impersonation"
    else:
        label = "✅ No strong impersonation signs"

    return chance, label

# Button
if st.button("🔍 Scan Profile"):
    if not username.strip():
        st.warning("Please enter a username.")
    elif not uploaded_file:
        st.warning("Please upload a screenshot.")
    else:
        st.success(f"Scanning @{username}...")

        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Screenshot", use_column_width=True)

        st.markdown("### 📝 Detected Violations:")
        for reason, count in generate_violation_report().items():
            st.markdown(f"- ✅ **{count}× {reason}**")

        # Impersonation Detection
        st.markdown("---")
        st.markdown("### 🕵️ Impersonation Detection:")
        chance, result = check_impersonation(username)
        st.markdown(f"**Impersonation Probability:** `{chance}%`")
        st.markdown(result)

        st.info("📌 This is a simulated report. No actual data was sent to Instagram.")
