function generateGameHTML(game) {
  return `
            <div class="game-container">
                <h2>${game.Title}</h2>
                <a href="${game.Link}" target="_blank">
                    <img src="${game["Image URL"]}" alt="${game.Title} Image">
                </a>
            </div>
        `;
}

function renderGames(jsonData) {
  var gamesContainer = document.getElementById("games-container");
  jsonData.forEach(function (game) {
    gamesContainer.innerHTML += generateGameHTML(game);
  });
}

fetch("games_data.json")
  .then((response) => response.json())
  .then((data) => renderGames(data))
  .catch((error) => console.error("Error fetching JSON:", error));
