document.addEventListener("DOMContentLoaded", () => {
  const prevBtn = document.querySelector(".unique-prev-btn");
  const nextBtn = document.querySelector(".unique-next-btn");
  const quotes = document.querySelectorAll(".unique-quote-card");

  if (!prevBtn || !nextBtn || quotes.length === 0) {
    console.error("必要な要素が見つかりません。HTMLを確認してください。");
    return;
  }

  let currentIndex = 0;

  function updateCarousel() {
    quotes.forEach((quote, index) => {
      quote.classList.toggle("active", index === currentIndex);
    });
  }

  prevBtn.addEventListener("click", () => {
    currentIndex = currentIndex === 0 ? quotes.length - 1 : currentIndex - 1;
    updateCarousel();
  });

  nextBtn.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % quotes.length;
    updateCarousel();
  });

  updateCarousel();
});
