import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Instagram Report Detector", layout="centered")

st.title("📸 Instagram Report Detector")
st.write("Simulate report violations from Instagram profiles or posts.")

# Username input
username = st.text_input("Instagram Username", placeholder="@example")

# Screenshot upload
uploaded_file = st.file_uploader("Upload Screenshot (Profile/Post)", type=["png", "jpg", "jpeg"])

# Simulate report types
all_reasons = ["Hate Speech", "Self-Harm", "Violence", "Spam", "Harassment", "Scam", "Adult Content"]

def generate_reports():
    # Choose 2–4 random reasons to show
    reasons_chosen = random.sample(all_reasons, k=random.randint(2, 4))
    report_result = {}
    for reason in reasons_chosen:
        report_result[reason] = random.randint(2, 7)
    return report_result

# Scan button
if st.button("🔍 Scan for Violations"):
    if not username.strip():
        st.warning("Enter a valid username.")
    elif not uploaded_file:
        st.warning("Upload a screenshot.")
    else:
        st.success(f"Analyzing {username}...")

        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Screenshot", use_column_width=True)

        st.write("### 🧾 Estimated Violation Report:")

        report_data = generate_reports()
        for reason, count in report_data.items():
            st.markdown(f"- ✅ **{count}× {reason}**")

        st.info("📌 This is a simulated report based on uploaded data. No actual account was reported.")
