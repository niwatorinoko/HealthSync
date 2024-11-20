document.addEventListener("DOMContentLoaded", () => {
  const prevBtn = document.querySelector(".unique-prev-btn");
  const nextBtn = document.querySelector(".unique-next-btn");
  const quotes = document.querySelectorAll(".unique-quote-card");
  
  if (!prevBtn || !nextBtn || quotes.length === 0) {
    console.error("必要な要素が見つかりません。HTMLを確認してください。");
    return;
  }

  let currentIndex = 0;
  let isAnimating = false;

  function updateCarousel(direction) {
    if (isAnimating) return;
    isAnimating = true;

    // 現在のカードを取得
    const currentQuote = quotes[currentIndex];
    
    // 新しいインデックスを計算
    const newIndex = direction === 'next' 
      ? (currentIndex + 1) % quotes.length 
      : (currentIndex - 1 + quotes.length) % quotes.length;
    
    // 新しいカードを取得
    const nextQuote = quotes[newIndex];

    // 現在のカードをアニメーション
    currentQuote.classList.remove('active');
    currentQuote.classList.add(direction === 'next' ? 'prev' : 'next');

    // 新しいカードをアニメーション
    nextQuote.classList.remove('prev', 'next');
    nextQuote.classList.add('active');

    // インデックスを更新
    currentIndex = newIndex;

    // アニメーション完了後にフラグをリセット
    setTimeout(() => {
      currentQuote.classList.remove('prev', 'next');
      isAnimating = false;
    }, 500);
  }

  // イベントリスナーを設定
  prevBtn.addEventListener("click", () => updateCarousel('prev'));
  nextBtn.addEventListener("click", () => updateCarousel('next'));

  // 自動再生を設定（オプション）
  setInterval(() => updateCarousel('next'), 5000);

  // 初期状態を設定
  quotes[currentIndex].classList.add('active');
});