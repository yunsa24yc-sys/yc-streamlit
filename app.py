import streamlit as st
import datetime

# 1. 網頁基本設定 (需放在程式碼最上方)
st.set_page_config(
    page_title="互動體驗網頁",
    page_icon="✨",
    layout="centered"
)

# 2. 側邊欄 (Sidebar) 互動
with st.sidebar:
    st.header("⚙️ 控制面板")
    user_name = st.text_input("請輸入您的暱稱", "訪客")
    theme_color = st.color_picker("選擇一個代表今天的顏色", "#1E90FF")
    st.divider()
    st.info("這是一個展示 Streamlit 介面元件與互動設計的無資料庫版本。")

# 3. 主頁面標題與歡迎語
st.title("✨ 互動體驗網頁")
st.markdown(f"歡迎，**{user_name}**！在這裡試試各種有趣的 UI 互動。")

# 4. 使用分欄 (Columns) 進行排版
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 狀態評估")
    mood = st.selectbox(
        "你現在的狀態如何？",
        ["充滿幹勁 🔥", "平靜穩定 😌", "有點燒腦 😵‍💫", "需要休息 😴"]
    )
    energy_level = st.slider("當前能量指數 (%)", 0, 100, 80)

with col2:
    st.subheader("🎯 今日目標")
    focus_area = st.radio(
        "接下來打算專注在什麼事情上？",
        ["開發與解 Bug 💻", "學術與文獻整理 📚", "找點美食外送慰勞自己 🍔", "享受遊戲時光 🎮"]
    )
    date = st.date_input("選擇日期", datetime.date.today())

st.divider()

# 5. 摺疊面板 (Expander)
with st.expander("💡 點擊展開：系統專屬建議"):
    if energy_level > 70:
        st.write("你的能量非常充足！現在正是訓練複雜深度學習模型、或是處理龐大資料集的好時機。")
    elif energy_level > 40:
        st.write("保持穩定的節奏。可以處理一些例行性的排程任務，或是追蹤一下近期的學習進度。")
    else:
        st.write("能量偏低！建議先暫停手邊的開發工作，吃點好吃的，或是拿起手把玩個遊戲充充電再出發。")

# 6. 送出按鈕與互動特效
if st.button("🚀 送出狀態", use_container_width=True):
    st.success(f"太棒了 {user_name}！你的狀態已成功記錄。接下來就好好享受「{focus_area}」吧！")
    
    # 根據狀態觸發不同的視覺特效
    if "幹勁" in mood:
        st.balloons()
    elif "休息" in mood:
        st.snow()