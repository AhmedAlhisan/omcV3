const customloader = document.querySelector('.spinner-wrapper');
window.addEventListener('load' , ()=>{
    customloader.style.opacity = '0';
    setTimeout(() => {
        customloader.style.display = 'none'
    }, 2000);
})
