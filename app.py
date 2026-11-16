import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy 20th Birthday! 🎂 專屬妳的20歲驚喜",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {
            background: linear-gradient(135deg, #fff0f5 0%, #f3e7ff 50%, #ffe6fa 100%);
        }
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            border: none !important;
            width: 100vw !important;
            height: 100dvh !important;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# 注意：這裡必須是 r"""（raw string），否則 JavaScript 裡的 \n 會被 Python 提前轉成換行而壞掉
birthday_html = r"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <style>
    :root {
      --primary: #ff6b9d;
      --primary-dark: #d9457a;
      --secondary: #9b72cf;
      --gold: #c9973f;
      --bg-gradient: linear-gradient(135deg, #fff0f5 0%, #f3e7ff 50%, #ffe6fa 100%);
      --card-bg: rgba(255, 255, 255, 0.88);
      --text-main: #4a3b47;
      --text-sub: #7a6877;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Microsoft JhengHei", sans-serif;
    }

    body {
      min-height: 100dvh;
      background: var(--bg-gradient);
      color: var(--text-main);
      display: flex;
      justify-content: center;
      align-items: center;
      overflow-x: hidden;
      padding: 20px 16px;
      position: relative;
    }

    .floating-bg {
      position: fixed;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
      z-index: 0;
    }

    .floating-item {
      position: absolute;
      bottom: -40px;
      font-size: 20px;
      opacity: 0;
      animation: floatUp linear infinite;
    }

    @keyframes floatUp {
      0% { transform: translateY(0) rotate(0deg); opacity: 0; }
      15% { opacity: 0.45; }
      85% { opacity: 0.45; }
      100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
    }

    .container {
      width: 100%;
      max-width: 440px;
      background: var(--card-bg);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid rgba(255, 255, 255, 0.9);
      border-radius: 28px;
      padding: 28px 20px;
      box-shadow: 0 20px 50px rgba(186, 122, 169, 0.18);
      text-align: center;
      position: relative;
      z-index: 1;
      animation: fadeUp 0.7s ease both;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(18px) scale(0.98); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .hidden {
      display: none !important;
    }

    .lock-icon {
      font-size: 46px;
      margin-bottom: 10px;
      display: inline-block;
      animation: bounce 2s infinite;
    }

    @keyframes bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-8px); }
    }

    h1 {
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--text-main);
      letter-spacing: 0.5px;
    }

    .subtitle {
      font-size: 14px;
      color: var(--text-sub);
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .input-group {
      margin-bottom: 12px;
    }

    input[type="tel"] {
      width: 100%;
      padding: 13px 16px;
      font-size: 20px;
      text-align: center;
      letter-spacing: 10px;
      border: 2px solid #f0d6e8;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.95);
      color: var(--text-main);
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    input[type="tel"]::placeholder {
      font-size: 14px;
      letter-spacing: 2px;
      color: #c9b3c4;
    }

    input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 4px rgba(255, 107, 157, 0.15);
    }

    .shake {
      animation: shake 0.4s;
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-7px); }
      40%, 80% { transform: translateX(7px); }
    }

    .error-msg {
      color: #e63946;
      font-size: 13px;
      min-height: 20px;
      margin-bottom: 10px;
    }

    .btn {
      width: 100%;
      padding: 13px 20px;
      font-size: 15.5px;
      font-weight: 700;
      color: #fff;
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
      border: none;
      border-radius: 16px;
      cursor: pointer;
      box-shadow: 0 8px 20px rgba(255, 107, 157, 0.35);
      transition: transform 0.2s, opacity 0.2s;
      -webkit-tap-highlight-color: transparent;
    }

    .btn:active {
      transform: scale(0.97);
    }

    .btn:disabled {
      opacity: 0.75;
    }

    .btn-ghost {
      background: #fff;
      color: var(--primary-dark);
      border: 1.5px solid #f3cce3;
      box-shadow: none;
    }

    .badge-20 {
      display: inline-block;
      background: linear-gradient(135deg, #ff8fab, #b388eb);
      color: white;
      font-family: Georgia, serif;
      font-size: 12px;
      font-weight: 700;
      padding: 5px 14px;
      border-radius: 99px;
      margin-bottom: 10px;
      letter-spacing: 1.5px;
    }

    /* ---------- 蛋糕 ---------- */
    .cake-box {
      margin: 20px auto;
      position: relative;
      width: 160px;
      height: 145px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
    }

    .candles {
      display: flex;
      gap: 18px;
      margin-bottom: -4px;
      z-index: 2;
    }

    .candle {
      position: relative;
      font-family: Georgia, serif;
      font-size: 32px;
      font-weight: 700;
      color: #ff5c8a;
    }

    .flame {
      width: 12px;
      height: 18px;
      background: radial-gradient(circle at 50% 80%, #fff 10%, #ffd166 50%, #f77f00 100%);
      border-radius: 50% 50% 20% 20%;
      margin: 0 auto 2px;
      box-shadow: 0 0 12px #ffd166, 0 0 24px #f77f00;
      animation: flicker 0.6s infinite alternate;
      transition: opacity 0.4s ease, transform 0.4s ease;
    }

    .flame.out {
      opacity: 0;
      transform: scale(0.2) translateY(-10px);
    }

    @keyframes flicker {
      0% { transform: scale(1) rotate(-2deg); }
      100% { transform: scale(1.1) rotate(2deg); }
    }

    .cake-top {
      width: 120px;
      height: 36px;
      background: #fff0f3;
      border-radius: 16px 16px 6px 6px;
      border-bottom: 6px solid #ffccd5;
    }

    .cake-bottom {
      width: 150px;
      height: 46px;
      background: #ffb3c6;
      border-radius: 10px 10px 16px 16px;
      box-shadow: 0 8px 16px rgba(255, 143, 171, 0.3);
    }

    /* ---------- 音樂 ---------- */
    .music-control {
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid #f0d6e8;
      border-radius: 50%;
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      cursor: pointer;
    }

    .spinning {
      animation: spin 4s linear infinite;
    }

    @keyframes spin {
      100% { transform: rotate(360deg); }
    }

    /* ---------- 天數 ---------- */
    .days-line {
      font-size: 13.5px;
      color: var(--text-sub);
      margin: 6px 0 2px;
      line-height: 1.7;
    }

    .days-num {
      font-family: Georgia, serif;
      font-size: 26px;
      font-weight: 700;
      color: var(--primary-dark);
      margin: 0 4px;
      font-variant-numeric: tabular-nums;
    }

    /* ---------- 信 ---------- */
    .letter-box {
      background: rgba(255, 255, 255, 0.85);
      border-radius: 18px;
      padding: 16px 15px;
      margin: 12px 0 4px;
      text-align: left;
      font-size: 14.5px;
      line-height: 1.85;
      color: var(--text-main);
      border: 1px dashed #e5b3d6;
      min-height: 135px;
      white-space: pre-wrap;
      cursor: pointer;
    }

    .cursor {
      display: inline-block;
      width: 2px;
      height: 1em;
      background: var(--primary);
      margin-left: 2px;
      vertical-align: -2px;
      animation: blink 0.9s steps(1) infinite;
    }

    @keyframes blink {
      50% { opacity: 0; }
    }

    .tiny-hint {
      font-size: 11.5px;
      color: #b39cae;
      margin-bottom: 14px;
      min-height: 16px;
    }

    /* ---------- 區塊 ---------- */
    .section {
      background: linear-gradient(135deg, #fff9fc 0%, #f9f2ff 100%);
      border: 1.5px solid #f3cce3;
      border-radius: 20px;
      padding: 14px 12px;
      margin-bottom: 14px;
    }

    .section-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 4px;
    }

    .section-hint {
      font-size: 12px;
      color: var(--text-sub);
      margin-bottom: 12px;
      line-height: 1.5;
    }

    /* ---------- 20 個祝福 ---------- */
    .wish-card {
      background: #fff;
      border-radius: 16px;
      border: 1.5px solid #ffd3e1;
      padding: 16px 14px;
      min-height: 104px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      box-shadow: 0 6px 14px rgba(186, 122, 169, 0.12);
    }

    .wish-no {
      font-family: Georgia, serif;
      font-size: 12px;
      letter-spacing: 2px;
      color: var(--gold);
      margin-bottom: 6px;
    }

    .wish-text {
      font-size: 15.5px;
      font-weight: 600;
      line-height: 1.6;
      color: var(--text-main);
    }

    .wish-pop {
      animation: wishPop 0.45s ease both;
    }

    @keyframes wishPop {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .progress {
      height: 6px;
      background: #f6dcea;
      border-radius: 99px;
      margin: 12px 4px 10px;
      overflow: hidden;
    }

    .progress-bar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--primary), var(--secondary));
      border-radius: 99px;
      transition: width 0.4s ease;
    }

    /* ---------- 翻牌 ---------- */
    .cards-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      perspective: 1000px;
    }

    .flip-card {
      background-color: transparent;
      height: 112px;
      cursor: pointer;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1);
      transform-style: preserve-3d;
    }

    .flip-card.flipped .flip-card-inner {
      transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
      position: absolute;
      inset: 0;
      border-radius: 15px;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 8px;
      box-shadow: 0 6px 14px rgba(186, 122, 169, 0.14);
    }

    .flip-card-front {
      background: linear-gradient(135deg, #ff8fab 0%, #b388eb 100%);
      color: #fff;
      border: 2px solid rgba(255, 255, 255, 0.85);
    }

    .flip-card-front .card-emoji {
      font-size: 26px;
      margin-bottom: 4px;
    }

    .flip-card-front .card-label {
      font-size: 12.5px;
      font-weight: 700;
    }

    .flip-card-back {
      background: #ffffff;
      color: var(--text-main);
      border: 2px solid #ffb3c6;
      transform: rotateY(180deg);
    }

    .flip-card-back .prize-icon {
      font-size: 22px;
      margin-bottom: 3px;
    }

    .flip-card-back .prize-name {
      font-size: 13px;
      font-weight: 700;
      color: var(--primary-dark);
      line-height: 1.3;
    }

    .flip-card-back .prize-note {
      font-size: 10.5px;
      color: var(--text-sub);
      margin-top: 2px;
    }

    /* ---------- ---------- */
    .secret-box {
      background: linear-gradient(135deg, #fff5d9 0%, #ffe9f1 100%);
      border: 1.5px solid #f1d69a;
      border-radius: 20px;
      padding: 16px 14px;
      margin-bottom: 14px;
      animation: fadeUp 0.8s ease both;
    }

    .secret-title {
      font-size: 13px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 2px;
      margin-bottom: 6px;
    }

    .secret-text {
      font-size: 14.5px;
      line-height: 1.8;
      color: var(--text-main);
      white-space: pre-wrap;
    }
  </style>
</head>
<body>

  <div class="floating-bg" id="floatingBg"></div>

  <!-- 關卡一：生日通關密碼 -->
  <div class="container" id="step1">
    <div class="lock-icon">🎁</div>
    <h1>一份只屬於妳的 20 歲驚喜</h1>
    <p class="subtitle">這份禮物只有妳打得開<br>請輸入通關密碼（提示：妳的 4 碼生日）</p>
    <div class="input-group">
      <input type="tel" id="passwordInput" inputmode="numeric" maxlength="4" placeholder="請輸入 4 位數字" autocomplete="off" />
    </div>
    <div class="error-msg" id="errorMsg"></div>
    <button class="btn" onclick="checkPassword()">解鎖我的生日禮物 ✨</button>
  </div>

  <!-- 關卡二：許願吹蠟燭互動 -->
  <div class="container hidden" id="step2">
    <span class="badge-20">CHAPTER 20 • 11.16</span>
    <h1>生日快樂！妳滿 20 歲啦 🎉</h1>
    <p class="subtitle">閉上眼睛，在心裡許下三個 20 歲的願望<br>許完願後，點擊下方按鈕吹熄蠟燭吧！</p>

    <div class="cake-box">
      <div class="candles">
        <div class="candle">
          <div class="flame" id="flame1"></div>
          2
        </div>
        <div class="candle">
          <div class="flame" id="flame2"></div>
          0
        </div>
      </div>
      <div class="cake-top"></div>
      <div class="cake-bottom"></div>
    </div>

    <button class="btn" id="blowBtn" onclick="blowCandles()">🌬️ 點擊吹熄蠟燭並開啟祝福</button>
  </div>

  <!-- 關卡三：祝福信、20 個祝福、翻牌、隱藏彩蛋 -->
  <div class="container hidden" id="step3">
    <button class="music-control spinning" id="musicBtn" onclick="toggleMusic()" title="切換音樂">🎵</button>
    <span class="badge-20">HAPPY 20TH BIRTHDAY</span>
    <h1>致最閃耀的 20 歲女孩 ✨</h1>
    <p class="days-line">從出生到今天，妳已經閃耀了<br><span class="days-num" id="daysNum">0</span>天</p>

    <div class="letter-box" id="letterBox"><span id="letterText"></span><span class="cursor" id="letterCursor"></span></div>
    <div class="tiny-hint" id="letterHint">點一下信紙可以直接看完整封信</div>

    <div class="section">
      <div class="section-title">💝 送給 20 歲的 20 個祝福</div>
      <div class="section-hint" id="wishHint">每點一下，就收下一個祝福</div>
      <div class="wish-card" id="wishCard" onclick="nextWish()">
        <div class="wish-no" id="wishNo">TAP TO OPEN</div>
        <div class="wish-text" id="wishText">點我開始 🎈</div>
      </div>
      <div class="progress"><div class="progress-bar" id="wishBar"></div></div>
    </div>

    <div class="section">
      <div class="section-title">🃏 20 歲幸運翻牌抽驚喜</div>
      <div class="section-hint" id="flipHint">點擊下方卡片翻開，看看裡面藏了什麼生日禮物！</div>
      <div class="cards-grid" id="cardsGrid"></div>
    </div>

    <div class="secret-box hidden" id="secretBox">
      <div class="secret-title">— 隱藏彩蛋 —</div>
      <div class="secret-text" id="secretText"></div>
    </div>

    <button class="btn" onclick="fireConfetti()">🎊 再放一次生日煙火！</button>
  </div>

  <canvas id="confettiCanvas" style="position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:999;"></canvas>

  <script>
    // ==========================================
    // 【密碼設定區】
    // 1. 通關密碼（生日 1116）
    const SECRET_PASSWORD = "1116";

    // 2. 出生年月日（用來計算「已經閃耀了幾天」）
    const BIRTH_YEAR = 2006, BIRTH_MONTH = 11, BIRTH_DAY = 16;

    // 3. 祝福信內容
    const LETTER_CONTENT = `20 歲生日快樂！🎂\n\n歡迎正式邁入人生超棒的二字頭！20 歲是一個很特別的起點，代表著更多的自由、更廣闊的世界，以及無限的可能。\n\n希望妳在新的一歲裡，依然能做最真實、最快樂的自己。不用急著成為大人，願妳既有面對世界的底氣，也永遠保有相信美好的純真。\n\n願所有好運與驚喜都在未來的路上與妳不期而遇，天天開心，閃閃發光！`;

    // 4. 20 個祝福
    const WISHES = [
      "願妳每天醒來，都有一件期待的事",
      "願妳想吃的都吃得到，而且不會胖",
      "願妳熬的每個夜都值得",
      "願妳的努力，都被好好看見",
      "願妳遇見的人，都溫柔待妳",
      "願妳的錢包永遠比想像中厚",
      "願妳想去的地方，都能抵達",
      "願妳難過的時候，身邊總有人在",
      "願妳拍的每一張照片都好看",
      "願妳的直覺，永遠帶妳走向對的路",
      "願妳勇敢說不，也勇敢說要",
      "願妳的秘密，都有人好好守護",
      "願妳永遠被堅定地選擇",
      "願妳考試都過、報告都順",
      "願妳夜夜好眠，夢裡都是好事",
      "願妳的每一個 11/16，都被好好記得",
      "願妳永遠有任性的底氣",
      "願妳喜歡的事，可以做一輩子",
      "願妳在長大的路上，不弄丟自己",
      "願妳的 20 歲，比想像中更精彩"
    ];

    // 5. 四張翻牌卡片內容
    const FLIP_CARDS_DATA = [
      {
        frontEmoji: "🎀",
        frontLabel: "幸運卡 No.1",
        icon: "🍰",
        title: "專屬生日大餐一頓",
        note: "妳想吃什麼我請客！"
      },
      {
        frontEmoji: "✨",
        frontLabel: "幸運卡 No.2",
        icon: "🧋",
        title: "飲料甜點無限暢飲券",
        note: "心情好或想喝隨時兌換"
      },
      {
        frontEmoji: "🦋",
        frontLabel: "幸運卡 No.3",
        icon: "🌟",
        title: "實現一個小願望",
        note: "憑截圖隨時向我許願"
      },
      {
        frontEmoji: "💌",
        frontLabel: "神秘祝福卡",
        icon: "🍀",
        title: "20歲好運爆棚符",
        note: "願妳所有努力都開花結果"
      }
    ];

    // 6. 四張卡片全部翻開後才會出現的隱藏訊息
    const SECRET_MESSAGE = `謝謝妳出生在 11 月 16 日，\n讓這一天變成值得慶祝的日子。\n\n往後的每一年，也請多多指教 🤍`;
    // ==========================================

    // ---------- 背景飄浮 ----------
    const floatingBg = document.getElementById('floatingBg');
    const icons = ['✨', '🌸', '💖', '🎈', '🎂', '🦋'];
    for (let i = 0; i < 16; i++) {
      const el = document.createElement('div');
      el.className = 'floating-item';
      el.innerText = icons[i % icons.length];
      el.style.left = Math.random() * 100 + 'vw';
      el.style.animationDuration = (8 + Math.random() * 8) + 's';
      el.style.animationDelay = (Math.random() * 5) + 's';
      floatingBg.appendChild(el);
    }

    function showStep(id) {
      ['step1', 'step2', 'step3'].forEach(s => {
        document.getElementById(s).classList.toggle('hidden', s !== id);
      });
      window.scrollTo(0, 0);
    }

    // ---------- 關卡一：密碼 ----------
    const passwordInput = document.getElementById('passwordInput');

    passwordInput.addEventListener('input', function() {
      this.value = this.value.replace(/\D/g, '').slice(0, 4);
      document.getElementById('errorMsg').innerText = "";
      if (this.value.length === 4) checkPassword();
    });

    passwordInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') checkPassword();
    });

    function checkPassword() {
      const input = passwordInput.value.trim();
      const errorMsg = document.getElementById('errorMsg');

      if (input === SECRET_PASSWORD) {
        errorMsg.innerText = "";
        passwordInput.blur();
        showStep('step2');
      } else {
        errorMsg.innerText = "密碼好像不對喔，再想一下妳的生日 4 碼數字 😉";
        passwordInput.classList.remove('shake');
        void passwordInput.offsetWidth;
        passwordInput.classList.add('shake');
      }
    }

    // ---------- 關卡二：吹蠟燭 ----------
    function blowCandles() {
      document.getElementById('flame1').classList.add('out');
      document.getElementById('flame2').classList.add('out');
      const blowBtn = document.getElementById('blowBtn');
      blowBtn.innerText = "✨ 願望已送出！正在打開禮物...";
      blowBtn.disabled = true;

      startBirthdayMusic();
      fireConfetti();

      setTimeout(() => {
        showStep('step3');
        startDaysCounter();
        startTypewriter();
        renderFlipCards();
      }, 1300);
    }

    // ---------- 已經閃耀了幾天 ----------
    function startDaysCounter() {
      const birth = new Date(BIRTH_YEAR, BIRTH_MONTH - 1, BIRTH_DAY);
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const total = Math.max(0, Math.round((today - birth) / 86400000));
      const el = document.getElementById('daysNum');
      const startTime = performance.now();
      const duration = 1800;

      function tick(t) {
        const p = Math.min(1, (t - startTime) / duration);
        const eased = 1 - Math.pow(1 - p, 3);
        el.innerText = Math.round(total * eased).toLocaleString('en-US');
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }

    // ---------- 打字機信件 ----------
    const letterChars = Array.from(LETTER_CONTENT);
    let charIndex = 0;
    let typeTimer = null;

    function finishLetter() {
      clearTimeout(typeTimer);
      charIndex = letterChars.length;
      document.getElementById('letterText').textContent = LETTER_CONTENT;
      document.getElementById('letterCursor').classList.add('hidden');
      document.getElementById('letterHint').innerText = "";
    }

    function startTypewriter() {
      const target = document.getElementById('letterText');
      target.textContent = "";
      charIndex = 0;

      function type() {
        if (charIndex < letterChars.length) {
          const ch = letterChars[charIndex];
          target.textContent += ch;
          charIndex++;
          const pause = (ch === '\n' || ch === '。' || ch === '！') ? 260 : 45;
          typeTimer = setTimeout(type, pause);
        } else {
          finishLetter();
        }
      }
      type();
    }

    document.getElementById('letterBox').addEventListener('click', function() {
      if (charIndex < letterChars.length) finishLetter();
    });

    // ---------- 20 個祝福 ----------
    let wishIndex = 0;

    function nextWish() {
      const card = document.getElementById('wishCard');
      const no = document.getElementById('wishNo');
      const text = document.getElementById('wishText');
      const hint = document.getElementById('wishHint');

      if (wishIndex >= WISHES.length) {
        wishIndex = 0;
      }

      text.innerText = WISHES[wishIndex];
      wishIndex++;
      no.innerText = 'No. ' + String(wishIndex).padStart(2, '0') + ' / ' + WISHES.length;
      document.getElementById('wishBar').style.width = (wishIndex / WISHES.length * 100) + '%';

      card.classList.remove('wish-pop');
      void card.offsetWidth;
      card.classList.add('wish-pop');

      if (wishIndex === WISHES.length) {
        hint.innerText = "💝 20 個祝福全部送達！再點一下可以重看一次";
        fireConfetti();
      } else {
        hint.innerText = "每點一下，就收下一個祝福";
      }
    }

    // ---------- 翻牌 ----------
    let flippedCount = 0;

    function renderFlipCards() {
      const grid = document.getElementById('cardsGrid');
      grid.innerHTML = "";
      flippedCount = 0;

      FLIP_CARDS_DATA.forEach((item) => {
        const card = document.createElement('div');
        card.className = 'flip-card';
        card.innerHTML = `
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="card-emoji">${item.frontEmoji}</div>
              <div class="card-label">${item.frontLabel}</div>
            </div>
            <div class="flip-card-back">
              <div class="prize-icon">${item.icon}</div>
              <div class="prize-name">${item.title}</div>
              <div class="prize-note">${item.note}</div>
            </div>
          </div>
        `;

        card.addEventListener('click', () => {
          if (!card.classList.contains('flipped')) {
            card.classList.add('flipped');
            flippedCount++;
            fireConfetti();

            if (flippedCount === FLIP_CARDS_DATA.length) {
              document.getElementById('flipHint').innerText = "🎉 太棒了！妳已解鎖全部的 20 歲生日驚喜（記得截圖兌換喔）！";
              setTimeout(revealSecret, 900);
            } else {
              document.getElementById('flipHint').innerText = `已解鎖 ${flippedCount}/${FLIP_CARDS_DATA.length} 張卡片，全部翻開還有隱藏彩蛋 ✨`;
            }
          }
        });

        grid.appendChild(card);
      });
    }

    function revealSecret() {
      const box = document.getElementById('secretBox');
      document.getElementById('secretText').textContent = SECRET_MESSAGE;
      box.classList.remove('hidden');
      box.scrollIntoView({ behavior: 'smooth', block: 'center' });
      fireConfetti();
    }

    // ---------- 彩帶 ----------
    const confettiCanvas = document.getElementById('confettiCanvas');
    const confettiCtx = confettiCanvas.getContext('2d');
    const confettiColors = ['#ff6b9d', '#ffd166', '#9b72cf', '#4ecdc4', '#ff8fab', '#a2d2ff'];
    let particles = [];
    let confettiRunning = false;

    function confettiLoop() {
      confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
      particles = particles.filter(p => p.life > 0);

      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.45;
        p.vx *= 0.99;
        p.angle += p.spin;
        p.life--;

        confettiCtx.save();
        confettiCtx.translate(p.x, p.y);
        confettiCtx.rotate(p.angle * Math.PI / 180);
        confettiCtx.fillStyle = p.color;
        confettiCtx.globalAlpha = Math.max(0, Math.min(1, p.life / 60));
        if (p.round) {
          confettiCtx.beginPath();
          confettiCtx.arc(0, 0, p.size / 2.4, 0, Math.PI * 2);
          confettiCtx.fill();
        } else {
          confettiCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
        }
        confettiCtx.restore();
      });

      if (particles.length > 0) {
        requestAnimationFrame(confettiLoop);
      } else {
        confettiRunning = false;
        confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
      }
    }

    function fireConfetti() {
      confettiCanvas.width = window.innerWidth;
      confettiCanvas.height = window.innerHeight;

      for (let i = 0; i < 110; i++) {
        particles.push({
          x: confettiCanvas.width / 2,
          y: confettiCanvas.height * 0.65,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 1.1) * 16,
          size: Math.random() * 8 + 4,
          color: confettiColors[Math.floor(Math.random() * confettiColors.length)],
          angle: Math.random() * 360,
          spin: (Math.random() - 0.5) * 12,
          round: Math.random() < 0.3,
          life: 100
        });
      }

      if (!confettiRunning) {
        confettiRunning = true;
        requestAnimationFrame(confettiLoop);
      }
    }

    // ---------- 音樂 ----------
    let audioCtx = null;
    let isPlaying = false;
    let melodyTimer = null;

    const notes = [
      { f: 261.63, d: 0.35 }, { f: 261.63, d: 0.35 }, { f: 293.66, d: 0.7 }, { f: 261.63, d: 0.7 }, { f: 349.23, d: 0.7 }, { f: 329.63, d: 1.2 },
      { f: 261.63, d: 0.35 }, { f: 261.63, d: 0.35 }, { f: 293.66, d: 0.7 }, { f: 261.63, d: 0.7 }, { f: 392.00, d: 0.7 }, { f: 349.23, d: 1.2 },
      { f: 261.63, d: 0.35 }, { f: 261.63, d: 0.35 }, { f: 523.25, d: 0.7 }, { f: 440.00, d: 0.7 }, { f: 349.23, d: 0.7 }, { f: 329.63, d: 0.7 }, { f: 293.66, d: 1.2 },
      { f: 466.16, d: 0.35 }, { f: 466.16, d: 0.35 }, { f: 440.00, d: 0.7 }, { f: 349.23, d: 0.7 }, { f: 392.00, d: 0.7 }, { f: 349.23, d: 1.4 }
    ];

    let activeOscillators = [];

    function playMelodyLoop() {
      if (!isPlaying) return;
      let time = audioCtx.currentTime + 0.05;
      let totalDuration = 0;
      activeOscillators = [];

      notes.forEach(note => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(note.f * 2, time + totalDuration);

        gain.gain.setValueAtTime(0.001, time + totalDuration);
        gain.gain.exponentialRampToValueAtTime(0.14, time + totalDuration + 0.03);
        gain.gain.exponentialRampToValueAtTime(0.001, time + totalDuration + note.d + 0.25);

        osc.connect(gain);
        gain.connect(audioCtx.destination);

        osc.start(time + totalDuration);
        osc.stop(time + totalDuration + note.d + 0.3);
        activeOscillators.push(osc);
        totalDuration += note.d + 0.06;
      });

      melodyTimer = setTimeout(playMelodyLoop, totalDuration * 1000 + 900);
    }

    function startBirthdayMusic() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      if (!isPlaying) {
        isPlaying = true;
        document.getElementById('musicBtn').classList.add('spinning');
        playMelodyLoop();
      }
    }

    function toggleMusic() {
      const btn = document.getElementById('musicBtn');
      if (isPlaying) {
        isPlaying = false;
        clearTimeout(melodyTimer);
        activeOscillators.forEach(o => { try { o.stop(); } catch (e) {} });
        activeOscillators = [];
        btn.classList.remove('spinning');
        btn.innerText = "🔇";
      } else {
        btn.innerText = "🎵";
        startBirthdayMusic();
      }
    }
  </script>
</body>
</html>
"""

components.html(birthday_html, height=900, scrolling=True)
