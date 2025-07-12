import streamlit as st
from chatbot import chat
from image_captioner import get_image_caption

# 🌸 Page config
st.set_page_config(
    page_title="ChatPet Clubhouse💖",
    page_icon="🐾",
    layout="centered",
)

# 🎵 Background Music
st.markdown("""
    <iframe width="0" height="0" src="https://www.youtube.com/embed/w9sXGMQEKVg?autoplay=1&loop=1&playlist=w9sXGMQEKVg" 
    frameborder="0" allow="autoplay" allowfullscreen style="display:none;"></iframe>
""", unsafe_allow_html=True)

# 💖 Custom Pink CSS Styling
st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
        }
        .stApp {
            background-image: linear-gradient(135deg, #ffe6f0, #ffe6ff);
            color: #5b005b;
            font-family: 'Comic Sans MS', cursive;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: #ff1493;
            font-weight: bold;
            margin-bottom: 20px;
            text-shadow: 1px 1px #ffb6c1;
        }
        .user-input {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# 🐾 ChatPet Title
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3V3aWNjZmc3azJuMDViM3g0NzNyczlva2xyOG5pOXk4dnE2Yzc3YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/92YG8KKSjYhMc/giphy.gif" width="300">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="title">Talk to ChatPet 💬</div>', unsafe_allow_html=True)

# 🗣️ User input
user_input = st.text_input("🌸 What do you want to ask ChatPet?", key="input", value="", placeholder="Type your secrets here~ ✨")

# 🧠 Chat
if user_input:
    response = chat.run(user_input)
    
    # 📝 Save to diary
    with open("diary.txt", "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\nChatPet 💕: {response}\n\n")
    
    st.markdown(f"🐾 **ChatPet:** {response}")
    
    # 🧽 Auto-clear text input
    st.rerun()

# 📖 View full diary
with st.expander("📖 Open Chat Diary"):
    with open("diary.txt", "r", encoding="utf-8") as f:
        diary = f.read()
    st.text_area("Dear Diary...", diary, height=300)

#Image Captioner Section
st.header("📷 ChatPet Image Captioner")

uploaded_file = st.file_uploader("Upload your image cutie 💅", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save to temp
    image_path = "temp_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    # Step 1: BLIP caption
    caption = get_image_caption(image_path)

    # Step 2: Send to ChatPet for cutesy prompt
    prompt = f"""You are ChatPet 💕, a cutesy plushie AI that loves pink, sparkles, and good vibes.
Given the plain image caption: "{caption}", create a cute, aesthetic version with emojis and energy.

Be fun and girly but not too long!
"""

    cute_caption = chat.run(prompt)

    st.image(image_path, caption="You uploaded this 👆")
    st.markdown(f"✨ ChatPet’s Vibe: **{cute_caption}**")
