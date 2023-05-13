const swiperTrending = document.querySelector('.swiper__trending')
const swiperUpcoming = document.querySelector('.swiper__upcoming')
const sliderContainer = document.querySelector('.slider__container')
const sliderRightButton = document.querySelector('.slider__button.right')
const sliderLeftButton = document.querySelector('.slider__button.left')
const trendingButton = document.querySelector('.trending__switch')

async function getTrendingMovies(type='week') {
    const response = await fetch(`./movie/?resource=trending/movie&type_=${type}`)
    swiperTrending.innerHTML = ``
    const data = await response.json()
    data.forEach((movie) => {
    swiperTrending.innerHTML += `
      <div class='swiper-slide'>
        <img class='swiper-slide-img' src="${movie.poster}" alt="${movie.title}">
        <div class='swiper-slide-container'>
          <h4 class='swiper-slide-title'>${movie.title}</h4>
        </div>
      </div>
    `
    })
}

async function getUpcomingMovies() {
    const response = await fetch(`./movie/?resource=movie&type_=upcoming&region=ES`)
    const data = await response.json()
    data.forEach((movie) => {
      swiperUpcoming.innerHTML += `
      <div class='swiper-slide'>
        <img class='swiper-slide-img' src="${movie.poster}" alt="${movie.title}">
        <div class='swiper-slide-container'>
          <h4 class='swiper-slide-title'>${movie.title}</h4>
        </div>
      </div>
    `
    })
}

getTrendingMovies()
getUpcomingMovies()

const swiper = new Swiper('.swiper', {
  // Optional parameters
  slidesPerView: "auto",
  spaceBetween: 10,
  grabCursor: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

trendingButton.addEventListener('click', () => {
  trendingButton.classList.toggle('active')
  getTrendingMovies(type='day')
})
