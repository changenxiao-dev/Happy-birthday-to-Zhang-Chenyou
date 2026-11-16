import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy 20th Birthday! 🎂 專屬你的20歲驚喜",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
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
      --primary-dark: #e04f80;
      --secondary: #9b72cf;
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
      opacity: 0.45;
      animation: floatUp linear infinite;
    }

    @keyframes floatUp {
      0% { transform: translateY(0) rotate(0deg); opacity: 0; }
      15% { opacity: 0.5; }
      85% { opacity: 0.5; }
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
      transition: all 0.5s ease;
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
      font-size: 18px;
      text-align: center;
      letter-spacing: 4px;
      border: 2px solid #f0d6e8;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.95);
      color: var(--text-main);
      outline: none;
    }

    input:focus {
      border-color: var(--primary);
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
      transition: transform 0.2s;
    }

    .btn:active {
      transform: scale(0.97);
    }

    .badge-20 {
      display: inline-block;
      background: linear-gradient(135deg, #ff8fab, #b5838d);
      color: white;
      font-family: Georgia, serif;
      font-size: 12px;
      font-weight: 700;
      padding: 5px 14px;
      border-radius: 99px;
      margin-bottom: 10px;
      letter-spacing: 1px;
    }

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

    .letter-box {
      background: rgba(255, 255, 255, 0.85);
      border-radius: 18px;
      padding: 15px 14px;
      margin: 12px 0;
      text-align: left;
      font-size: 14px;
      line-height: 1.75;
      color: var(--text-main);
      border: 1px dashed #e5b3d6;
      min-height: 135px;
    }

    .flip-section {
      background: linear-gradient(135deg, #fff9fc 0%, #f9f2ff 100%);
      border: 1.5px solid #f3cce3;
      border-radius: 20px;
      padding: 14px 12px;
      margin-bottom: 14px;
    }

    .flip-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 4px;
    }

    .flip-hint {
      font-size: 12px;
      color: var(--text-sub);
      margin-bottom: 12px;
    }

    .cards-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      perspective: 1000px;
    }

    .flip-card {
      background-color: transparent;
      height: 106px;
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
  </style>
</head>
<body>

  <div class="floating-bg" id="floatingBg"></div>

  <!-- 關卡一：生日通關密碼 -->
  <div class="container" id="step1">
    <div class="lock-icon">🎁</div>
    <h1>一份專屬你的 20 歲驚喜</h1>
    <p class="subtitle">在打開這份禮物之前，請先輸入通關密碼<br>（提示：你的 4 碼生日）</p>
    <div class="input-group">
      <input type="tel" id="passwordInput" maxlength="4" placeholder="請輸入 4 位數字" autocomplete="off" />
    </div>
    <div class="error-msg" id="errorMsg"></div>
    <button class="btn" onclick="checkPassword()">解鎖我的生日禮物 ✨</button>
  </div>

  <!-- 關卡二：許願吹蠟燭互動 -->
  <div class="container hidden" id="step2">
    <span class="badge-20">CHAPTER 20 • WELCOME TO ADULTHOOD</span>
    <h1>生日快樂！你滿 20 歲啦 🎉</h1>
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

  <!-- 關卡三：20歲祝福信與互動翻牌小遊戲 -->
  <div class="container hidden" id="step3">
    <button class="music-control spinning" id="musicBtn" onclick="toggleMusic()" title="切換音樂">🎵</button>
    <span class="badge-20">HAPPY 20TH BIRTHDAY</span>
    <h1>致最閃耀的 20 歲女孩 ✨</h1>

    <div class="letter-box" id="typewriterText"></div>

    <div class="flip-section">
      <div class="flip-title">🃏 20 歲幸運翻牌抽驚喜</div>
      <div class="flip-hint" id="flipHint">點擊下方卡片翻開，看看裡面藏了什麼生日禮物！</div>
      <div class="cards-grid" id="cardsGrid"></div>
    </div>

    <button class="btn" onclick="fireConfetti()">🎊 再放一次生日煙火！</button>
  </div>

  <canvas id="confettiCanvas" style="position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:999;"></canvas>

  <script>
    // ==========================================
    // 【你可以自訂修改的設定區】
    // 1. 設定通關密碼（生日1116)
    const SECRET_PASSWORD = "1116";

    // 2. 給她的20歲祝福信件內容
    const LETTER_CONTENT = `20 歲生日快樂！🎂\n\n歡迎正式邁入人生超棒的二字頭！20 歲是一個很特別的起點，代表著更多的自由、更廣闊的世界，以及無限的可能。\n\n希望妳在新的一歲裡，依然能做最真實、最快樂的自己。不用急著成為大人，願你既有面對世界的底氣，也永遠保有相信美好的純真。願所有好運與驚喜都在未來的路上與妳不期而遇，天天開心，閃閃發光！`;

    // 3. 四張翻牌卡片內容
    const FLIP_CARDS_DATA = [
      {
        frontEmoji: "🎀",
        frontLabel: "幸運卡 No.1",
        icon: "🍰",
        title: "專屬生日大餐一頓",
        note: "你想吃什麼我請客！"
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
        note: "願你所有努力都開花結果"
      }
    ];
    // ==========================================

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

    document.getElementById('passwordInput').addEventListener('keypress', function(e) {
      if (e.key === 'Enter') checkPassword();
    });

    function checkPassword() {
      const input = document.getElementById('passwordInput').value.trim();
      const errorMsg = document.getElementById('errorMsg');

      if (input === SECRET_PASSWORD) {
        errorMsg.innerText = "";
        document.getElementById('step1').classList.add('hidden');
        document.getElementById('step2').classList.remove('hidden');
      } else {
        errorMsg.innerText = "密碼好像不對喔，再想一下你的生日 4 碼數字 😉";
      }
    }

    function blowCandles() {
      document.getElementById('flame1').classList.add('out');
      document.getElementById('flame2').classList.add('out');
      const blowBtn = document.getElementById('blowBtn');
      blowBtn.innerText = "✨ 願望已送出！正在打開禮物...";
      blowBtn.disabled = true;

      startBirthdayMusic();
      fireConfetti();

      setTimeout(() => {
        document.getElementById('step2').classList.add('hidden');
        document.getElementById('step3').classList.remove('hidden');
        startTypewriter();
        renderFlipCards();
      }, 1300);
    }

    let charIndex = 0;
    function startTypewriter() {
      const target = document.getElementById('typewriterText');
      target.innerHTML = "";
      function type() {
        if (charIndex < LETTER_CONTENT.length) {
          const char = LETTER_CONTENT.charAt(charIndex);
          target.innerHTML += char === '\n' ? '<br>' : char;
          charIndex++;
          setTimeout(type, 45);
        }
      }
      type();
    }

    let flippedCount = 0;
    function renderFlipCards() {
      const grid = document.getElementById('cardsGrid');
      grid.innerHTML = "";

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
              document.getElementById('flipHint').innerText = "🎉 太棒了！你已解鎖全部的 20 歲生日驚喜（記得截圖兌換喔）！";
            } else {
              document.getElementById('flipHint').innerText = `已解鎖 ${flippedCount}/${FLIP_CARDS_DATA.length} 張卡片，繼續翻開其他張吧！✨`;
            }
          }
        });

        grid.appendChild(card);
      });
    }

    // 內建輕量彩帶撒花特效（不依賴任何外部 CDN，離線也能運作）
    function fireConfetti() {
      const canvas = document.getElementById('confettiCanvas');
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const colors = ['#ff6b9d', '#ffd166', '#9b72cf', '#4ecdc4', '#ff8fab', '#a2d2ff'];
      const particles = [];
      for (let i = 0; i < 110; i++) {
        particles.push({
          x: canvas.width / 2,
          y: canvas.height * 0.65,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 1.1) * 16,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          angle: Math.random() * 360,
          spin: (Math.random() - 0.5) * 12,
          life: 100
        });
      }

      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let active = false;
        particles.forEach(p => {
          if (p.life > 0) {
            active = true;
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.45;
            p.angle += p.spin;
            p.life--;

            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate(p.angle * Math.PI / 180);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = Math.max(0, p.life / 100);
            ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
            ctx.restore();
          }
        });
        if (active) requestAnimationFrame(animate);
        else ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
      animate();
    }

    let audioCtx = null;
    let isPlaying = false;
    let melodyTimer = null;

    const notes = [
      { f: 261.63, d: 0.35 }, { f: 261.63, d: 0.35 }, { f: 293.66, d: 0.7 }, { f: 261.63, d: 0.7 }, { f: 349.23, d: 0.7 }, { f: 329.63, d: 1.2 },
      { f: 261.63, d: 0.35 }, { f: 261.63, d: 0.35 }, { f: 293.66, d: 0.7 }, { f: 261.63, d: 0.7 }, { f: 392.00, d: 0.7 }, { f: 349.23, d: 1.2 },
      { f: 261.63, d: 0.35 }, { f: 261.63, d: 0.35 }, { f: 523.25, d: 0.7 }, { f: 440.00, d: 0.7 }, { f: 349.23, d: 0.7 }, { f: 329.63, d: 0.7 }, { f: 293.66, d: 1.2 },
      { f: 466.16, d: 0.35 }, { f: 466.16, d: 0.35 }, { f: 440.00, d: 0.7 }, { f: 349.23, d: 0.7 }, { f: 392.00, d: 0.7 }, { f: 349.23, d: 1.4 }
    ];

    function playMelodyLoop() {
      if (!isPlaying) return;
      let time = audioCtx.currentTime;
      let totalDuration = 0;

      notes.forEach(note => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(note.f, time + totalDuration);

        gain.gain.setValueAtTime(0.001, time + totalDuration);
        gain.gain.exponentialRampToValueAtTime(0.18, time + totalDuration + 0.04);
        gain.gain.exponentialRampToValueAtTime(0.001, time + totalDuration + note.d);

        osc.connect(gain);
        gain.connect(audioCtx.destination);

        osc.start(time + totalDuration);
        osc.stop(time + totalDuration + note.d);
        totalDuration += note.d + 0.06;
      });

      melodyTimer = setTimeout(playMelodyLoop, totalDuration * 1000 + 600);
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
