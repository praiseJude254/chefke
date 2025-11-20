// scroll-animations.js

// Add 'visible' class to feature cards on scroll
document.addEventListener('DOMContentLoaded', () => {
    const featureCards = document.querySelectorAll('.feature-card');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });

    featureCards.forEach(card => observer.observe(card));
});


document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".testimonial-slider");
    const cards = Array.from(slider.children);
    const visibleCount = 3;
    const cardGap = 20; // must match CSS gap
    const cardWidth = cards[0].offsetWidth + cardGap;

    // Wrap slider in a container to hide overflow
    slider.style.display = "flex";
    slider.style.transition = "transform 0.6s ease";

    let offset = 0;

    function moveSlider() {
        offset += cardWidth;
        slider.style.transform = `translateX(-${offset}px)`;

        // After transition, move the first card to the end and reset offset
        slider.addEventListener("transitionend", function handler() {
            slider.style.transition = "none";
            slider.appendChild(slider.children[0]); // move first card to end
            offset -= cardWidth;
            slider.style.transform = `translateX(-${offset}px)`;
            slider.style.transition = "transform 0.6s ease";
            slider.removeEventListener("transitionend", handler);
        });
    }

    setInterval(moveSlider, 4000);
});

document.addEventListener('DOMContentLoaded', () => {
    const videoItems = document.querySelectorAll('.video-item');
    const modal = document.getElementById('video-modal');
    const modalVideo = document.getElementById('modal-video');
    const closeBtn = document.querySelector('.close-btn');

    videoItems.forEach(item => {
        const video = item.querySelector('video');
        const playBtn = item.querySelector('.play-btn');

        playBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            modal.style.display = 'flex';
            modalVideo.src = video.src;
            modalVideo.muted = false;
            modalVideo.play();
        });
    });

    const closeModal = () => {
        modalVideo.pause();
        modalVideo.currentTime = 0;
        modalVideo.src = '';
        modal.style.display = 'none';
    };

    closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', (e) => {
        if(e.target === modal) {
            closeModal();
        }
    });
});


// Select all FAQ items
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
  const question = item.querySelector('.faq-question');
  
  question.addEventListener('click', () => {
    const isActive = item.classList.contains('active');
    
    // Close all items
    faqItems.forEach(i => {
      i.classList.remove('active');
      i.querySelector('.faq-answer').style.maxHeight = null;
      i.querySelector('.faq-answer').style.opacity = 0;
    });
    
    // Toggle the clicked item
    if(!isActive) {
      item.classList.add('active');
      const answer = item.querySelector('.faq-answer');
      answer.style.maxHeight = answer.scrollHeight + "px";
      answer.style.opacity = 1;
    }
  });
});
