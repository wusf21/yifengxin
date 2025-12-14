<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blue Letter</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      height: 100vh;
      background: linear-gradient(135deg, #f4f9ff 0%, #e8f3ff 100%);
      overflow: hidden;
      font-family: 'Comic Sans MS', 'Segoe UI', sans-serif;
      transition: background 1.5s ease;
    }
    
    body.page-2 {
      background: linear-gradient(135deg, #e8f3ff 0%, #d4ebff 100%);
    }
    
    body.page-3 {
      background: linear-gradient(135deg, #d4ebff 0%, #5a8bc4 100%);
    }
    
    body.page-4 {
      background: linear-gradient(135deg, #2a3f5f 0%, #1a2332 100%);
    }

    .stage {
      position: relative;
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    /* Envelope */
    .envelope {
      position: absolute;
      width: 240px;
      height: 150px;
      background: #9ecfff;
      border-radius: 10px;
      cursor: pointer;
      animation: flyIn 1.8s ease-out forwards, wobble 3s ease-in-out infinite;
      left: -300px;
      box-shadow: 0 6px 0 #7fb6eb;
    }

    .envelope::before {
      content: '';
      position: absolute;
      inset: 0;
      background: #b7ddff;
      clip-path: polygon(0 0, 50% 55%, 100% 0, 100% 0, 0 0);
      border-radius: 10px;
    }

    .open-btn {
      position: absolute;
      bottom: 15px;
      left: 50%;
      transform: translateX(-50%);
      padding: 6px 18px;
      border: 2px solid #4a7fb8;
      border-radius: 6px;
      background: #ffffff;
      font-weight: bold;
      color: #4a7fb8;
      letter-spacing: 2px;
    }

    @keyframes flyIn {
      to { left: 50%; transform: translateX(-50%); }
    }

    @keyframes wobble {
      0%,100% { transform: translateX(-50%) rotate(0deg); }
      25% { transform: translateX(-50%) rotate(-3deg); }
      75% { transform: translateX(-50%) rotate(3deg); }
    }

    /* Paper */
    .paper {
      transform-origin: top;
      transition: all 0.6s ease;
      transform-origin: top;
      position: absolute;
      width: 92%;
      max-width: 420px;
      height: 82%;
      background: #ffffff;
      border-radius: 14px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.12);
      overflow-y: auto;
      padding: 30px 22px;
      display: none;
      animation: unfold 1s ease forwards;
    }

    @keyframes unfold {
      from { transform: scaleY(0); }
      to { transform: scaleY(1); }
    }

    @keyframes fold {
      0% { transform: scaleY(1) translateY(0); opacity: 1; }
      40% { transform: scaleY(0.7) translateY(30px); opacity: 0.95; }
      70% { transform: scaleY(0.35) translateY(80px); opacity: 0.85; }
      100% { transform: scaleY(0.08) translateY(140px); opacity: 0; }
    }

    @keyframes slideIntoEnvelope {
      0% { transform: translateY(140px) scaleY(0.08); opacity: 0; }
      30% { transform: translateY(100px) scaleY(0.2); opacity: 0.3; }
      60% { transform: translateY(50px) scaleY(0.5); opacity: 0.6; }
      100% { transform: translateY(0) scaleY(1); opacity: 1; }
    }

    .page {
      min-height: 100vh;
      padding: 40px 0 180px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .page h2 {
      color: #4a7fb8;
      font-size: 48px;
      margin: 20px 0;
    }
    
    body.page-4 .page h2 {
      color: #9ecfff;
    }

    .typed {
      font-size: 16px;
      line-height: 1.8;
      color: #333;
      white-space: pre-wrap;
    }

    .dog {
      margin: 20px auto;
      width: 80px;
    }

    .next-btn {
      margin: 28px auto 0;
      display: block;
      padding: 10px 22px;
      border: 2px solid #7fb6eb;
      border-radius: 20px;
      background: #e8f3ff;
      color: #4a7fb8;
      font-weight: bold;
      cursor: pointer;
      opacity: 0;
      animation: fadeInBtn 0.6s ease 2s forwards;
    }
    
    @keyframes fadeInBtn {
      to { opacity: 1; }
    }

    .final-btn {
      background: #9ecfff;
      color: white;
      border-color: #7fb6eb;
    }

    img.photo {
      width: 100%;
      border-radius: 12px;
      margin: 15px 0;
    }

    .paper.fold {
      animation: fold 1.4s ease forwards;
    }

    .envelope.receive {
      animation: slideIntoEnvelope 0.8s ease forwards;
    }
    
    .confetti {
      position: fixed;
      width: 10px;
      height: 10px;
      background: #9ecfff;
      top: -10px;
      opacity: 0;
      animation: confettiFall 4s ease-in infinite;
    }
    
    @keyframes confettiFall {
      0% { opacity: 1; transform: translateY(0) rotate(0deg); }
      100% { opacity: 0; transform: translateY(100vh) rotate(720deg); }
    }
  </style>
</head>
<body>
  <div class="stage">
    <div class="envelope" id="envelope">
      <div class="open-btn">打开</div>
    </div>

    <div class="paper" id="paper">
      <div class="page" id="page1">
        <h2>🎂</h2>
        <div class="typed" data-text="Happy Birthday 💙
This is page one."></div>
        <img class="dog" src="https://i.imgur.com/6X4F7kM.png" />
        <button class="next-btn" onclick="goTo(2)">Scroll Down</button>
      </div>

      <div class="page" id="page2">
        <h2>🐶</h2>
        <div class="typed" data-text="Page two text goes here."></div>
        <button class="next-btn" onclick="goTo(3)">Scroll Down</button>
      </div>

      <div class="page" id="page3">
        <h2>💌</h2>
        <div class="typed" data-text="Page three message."></div>
        <img class="photo" src="https://i.imgur.com/6X4F7kM.png" />
        <button class="next-btn" onclick="goTo(4)">Scroll Down</button>
      </div>

      <div class="page" id="page4">
        <h2>✨</h2>
        <div class="typed" data-text="This letter ends here."></div>
        <button class="next-btn final-btn" onclick="closeLetter()">藏在心里</button>
      </div>
    </div>
  </div>

  <script>
    const envelope = document.getElementById('envelope');
    const paper = document.getElementById('paper');
    let currentPage = 1;
    let confettiInterval;

    envelope.addEventListener('click', () => {
      envelope.style.display = 'none';
      paper.style.display = 'block';
      document.body.className = 'page-1';
      startTyping(1);
    });

    function goTo(page) {
      currentPage = page;
      
      // Update background gradient per page
      document.body.className = '';
      if (page === 1) document.body.classList.add('page-1');
      if (page === 2) document.body.classList.add('page-2');
      if (page === 3) document.body.classList.add('page-3');
      if (page === 4) document.body.classList.add('page-4');
      
      document.getElementById('page' + page).scrollIntoView({ behavior: 'smooth' });
      
      setTimeout(() => {
        startTyping(page);
      }, 600);
      
      if (page === 4) {
        startConfetti();
      } else {
        stopConfetti();
      }
    }

    function closeLetter() {
      stopConfetti();
      paper.classList.add('fold');

      // Step 1: Fold paper and hide it (1.6s)
      setTimeout(() => {
        paper.style.display = 'none';
        paper.classList.remove('fold');
        paper.scrollTop = 0;
        currentPage = 1;
        resetTyping();
      }, 1600);

      // Step 2: Change background back to original (after paper hidden)
      setTimeout(() => {
        document.body.className = '';
      }, 1700);

      // Step 3: Show envelope back with wobble (after background changed)
      setTimeout(() => {
        envelope.style.display = 'block';
        envelope.style.left = '50%';
        envelope.style.transform = 'translateX(-50%)';
        envelope.classList.remove('receive');
        envelope.style.animation = 'wobble 2s ease-in-out infinite';
      }, 2200);
    }

    function startTyping(page) {
      const el = document.querySelector(`#page${page} .typed`);
      if (!el) return;
      
      const text = el.getAttribute('data-text');
      let i = 0;
      el.textContent = '';
      const timer = setInterval(() => {
        el.textContent += text[i];
        i++;
        if (i >= text.length) clearInterval(timer);
      }, 50);
      
      const btn = document.querySelector(`#page${page} .next-btn, #page${page} .final-btn`);
      if (btn) {
        btn.style.animation = 'none';
        setTimeout(() => {
          btn.style.animation = 'fadeInBtn 0.6s ease forwards';
        }, 10);
      }
    }
    
    function resetTyping() {
      document.querySelectorAll('.typed').forEach(el => {
        el.textContent = '';
      });
    }
    
    function startConfetti() {
      const colors = ['#9ecfff', '#ffffff', '#b7ddff', '#7fb6eb'];
      confettiInterval = setInterval(() => {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 2 + 's';
        confetti.style.width = (Math.random() * 8 + 6) + 'px';
        confetti.style.height = confetti.style.width;
        document.body.appendChild(confetti);
        
        setTimeout(() => {
          confetti.remove();
        }, 4000);
      }, 200);
    }
    
    function stopConfetti() {
      if (confettiInterval) {
        clearInterval(confettiInterval);
        document.querySelectorAll('.confetti').forEach(c => c.remove());
      }
    }
  </script>
</body>
</html>
