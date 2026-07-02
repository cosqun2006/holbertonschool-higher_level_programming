const url = 'https://swapi-api.alx-tools.com/api/people/4/';

fetch(url)
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  });
  