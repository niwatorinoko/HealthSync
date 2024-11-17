const yogaSlides = document.querySelector('.yoga-slides');
const yogaDots = document.querySelectorAll('.yoga-dots span');
let yogaIndex = 0;

function updateYogaDots(index) {
  yogaDots.forEach((dot, i) => {
    dot.classList.toggle('active', i === index);
  });
}

setInterval(() => {
  yogaIndex = (yogaIndex + 1) % yogaDots.length; // Loop
  yogaSlides.style.transform = `translateX(-${yogaIndex * 600}px)`; // Slide
  updateYogaDots(yogaIndex);
}, 3000);

yogaDots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
    yogaIndex = index;
    yogaSlides.style.transform = `translateX(-${index * 600}px)`;
    updateYogaDots(index);
  });
});
