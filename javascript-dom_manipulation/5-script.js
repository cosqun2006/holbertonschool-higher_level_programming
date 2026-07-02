const updateHeaderDiv = document.querySelector('#update_header');

updateHeaderDiv.addEventListener('click', function() {
    
    const headerElement = document.querySelector('header');
    headerElement.textContent = 'New Header!!!';
});
