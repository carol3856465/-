import streamlit as st

st.set_page_config(page_title="測測你是哪種理財星人？", page_icon="🔮", layout="centered")

# 偷偷注入一點 CSS 魔法來改造 UI (Google 表單卡片風格 + 星空琉璃藍按鈕)
# 偷偷注入一點 CSS 魔法來改造 UI (Google 表單卡片風格 + 星雲淺藍外框)
st.markdown("""
    <style>
    /* 1. 外層大背景 (左右兩邊的顏色) 
       ✨ 換成更明顯的「星雲淺藍色」，宇宙感 UP！ */
    [data-testid="stAppViewContainer"] {
        background-color: #C2D6ED !important; 
    }

    /* 2. 中間的主要內容區塊 (Google 表單的卡片本體) */
    .block-container {
        background-color: #F4F7F9 !important; /* 中間維持乾淨的淺灰色 */
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        border-radius: 20px !important; 
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08) !important; 
        max-width: 750px !important; 
        margin-top: 2rem !important; 
        margin-bottom: 2rem !important;
    }

    /* 3. 強制修改 Primary 按鈕的顏色為銀河星光藍 */
    button[kind="primary"] {
        background-color: #00509E !important;
        border-color: #00509E !important;
        color: white !important;
        border-radius: 10px !important;
        width: 100% !important;
        font-weight: bold !important;
        font-size: 18px !important;
        box-shadow: 0 4px 10px rgba(0, 80, 158, 0.4) !important; 
        transition: 0.3s !important;
    }
    
    /* 4. 滑鼠移過去時變成較亮的彗星藍 */
    button[kind="primary"]:hover {
        background-color: #006BB6 !important;
        border-color: #006BB6 !important;
        color: white !important;
        box-shadow: 0 6px 15px rgba(0, 107, 182, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI 皮囊：Banner 與開場白 ---
st.image("banner.png", use_container_width=True)

# 保留超有帶入感的引言文字
st.write("你常常買盲盒買到剁手手嗎？其實，你開盲盒的習慣，早就偷偷出賣了你的「真實理財性格」！來花 30 秒測測看吧！")
st.divider()

with st.form("quiz_form"):
    st.subheader("階段一：")
    
    # Q3
    q3 = st.selectbox(
        "1. 你目前主要在哪個領域呢？",
        ["商管 / 財金 / 法律 ", 
         "資訊 / 科技 / 工程 / 理農 ", 
         "人文 / 藝術 / 設計 / 教育 / 服務 / 其他 "]
    )
    
    # Q9
    q9 = st.radio(
        "2. 走進玩具店看到超可愛的公仔，但手邊預算有限，你會怎麼選？",
        ["100% 確定款式，直接帶走喜歡的「實用明盒」", 
         "內容未知，但有機會抽中隱藏款的「驚喜盲盒」"]
    )
    
    st.subheader("階段二：")
    
    # Q12
    q12 = st.slider(
        "3. 說到投資，你的心臟最多能承受多少比例的虧損？",
        min_value=0,   
        max_value=100, 
        value=15,      
        step=1,        
        format="%d%%"  
    )
    
    # Q13
    q13 = st.selectbox(
        "4. 你覺得買盲盒時的那種刺激感，最像哪一種投資行為？",
        [" 以小博大（拚隱藏款爆擊，買彩券概念）", 
         " 定期定額（每個月抽一盒，慢慢收集）", 
         " 分散風險（跟朋友合資包盒，保證不雷）"]
    )
    
    submit_btn = st.form_submit_button("送出！", type="primary")

# --- 後台大腦：加權計分演算法 ---
if submit_btn:
    st.divider()
    
    risk_score = 50  
    rationality_score = 50  
    
    # ⚠️ 這裡的文字與你的選項完全對應（含空格）
    if q3 == "商管 / 財金 / 法律 ":
        risk_score += 15
    elif q3 == "資訊 / 科技 / 工程 / 理農 ":
        rationality_score += 10
        
    if q9 == "100% 確定款式，直接帶走喜歡的「實用明盒」":
        rationality_score += 25
        risk_score -= 15
    else:
        risk_score += 25
        rationality_score -= 15
        
    if q12 == 0:
        risk_score -= 25
        rationality_score += 20
    elif 16 <= q12 <= 30:
        risk_score += 15
    elif q12 >= 31:
        risk_score += 25
        
    is_contradictory = False
    if q9 == "100% 確定款式，直接帶走喜歡的「實用明盒」" and q13 == " 以小博大（拚隱藏款爆擊，買彩券概念）":
        is_contradictory = True  
        
    if is_contradictory:
        persona = "🎭 口嫌體正直的『矛盾型玩家』"
        description = "嘴上說著想體驗心跳加速，但身體卻很誠實地不想虧錢。你很容易在投資時患得患失，在風險與保守之間反覆橫跳！"
        strategy = "💡 給你的專屬建議：適合 60% 穩健 ETF 打底，搭配 10% 的『盲盒停損實驗區』"
    elif risk_score >= 65:
        persona = "🔥 歐皇附體的『激進型獵人』"
        description = "你享受抽盲盒的刺激感，投資上也偏愛高風險高報酬。你具備強大的心理素質，只要看準了就敢衝！"
        strategy = "💡 給你的專屬建議：適合攻擊型配置，但一定要留至少 10% 的現金當作『風險防火牆』！"
    else:
        persona = "🛡️ 穩如泰山的『佛系收藏家』"
        description = "你喜歡確定的事物，買東西不靠運氣，投資也愛穩穩拿配息。是個超級理性、不容易被市場恐慌情緒煽動人！"
        strategy = "💡 給你的專屬建議：適合 70% 穩定配息 ETF 加上大型藍籌股定期定額，靠時間穩穩把錢養大！"

    # --- 前端呈現結果 (縮小置中優化版) ---
    st.balloons() 
    
    st.header(f"你的理財真實身分是：\n{persona}")
    
    # 置中縮小圖片
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if persona == "🎭 口嫌體正直的『矛盾型玩家』":
            st.image("type1.png", use_container_width=True)
        elif persona == "🔥 歐皇附體的『激進型獵人』":
            st.image("type2.png", use_container_width=True)
        else:
            st.image("type3.png", use_container_width=True)
        
    st.info(description)
    st.success(strategy)
    st.caption(f"⚙️ 系統運算指標：風險追求度 {risk_score}/100 ｜ 決策理性度 {rationality_score}/100 ｜ 容忍度 {q12}%")