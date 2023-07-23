


const content = document.querySelector('.content');
const footer = document.querySelector('.footer');
const contentHeight = content.offsetHeight;
const windowHeight = window.innerHeight;
const footerHeight = footer.offsetHeight;

if (contentHeight + footerHeight < windowHeight) {
  footer.style.position = 'absolute';
  footer.style.bottom = 0;
}