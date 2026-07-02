const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

const listMovies = document.querySelector('#list_movies');

fetch(url)
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    
    movies.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  });
  