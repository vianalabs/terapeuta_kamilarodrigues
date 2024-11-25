//Menu hamburguer

const hamburger = document.querySelector('.hamburger');
const menuItens = document.querySelector('.menu-itens');

hamburger.addEventListener('click', () => {
    menuItens.classList.toggle('open');
});