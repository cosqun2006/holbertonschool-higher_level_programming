const redHeaderDiv = document.querySelector('#red_header');

redHeaderDiv.addEventListener('click', function() {
    const headerElement = document.querySelector('header');
    
    headerElement.classList.add('red');
});
