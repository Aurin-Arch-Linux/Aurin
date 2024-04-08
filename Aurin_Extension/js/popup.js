document.addEventListener('DOMContentLoaded', function() {
  var searchInput = document.getElementById('searchInput');
  var searchButton = document.getElementById('searchButton');
  var searchResults = document.getElementById('searchResults');

  searchButton.addEventListener('click', function() {
    var query = searchInput.value.trim();
    if (query !== '') {
      chrome.runtime.sendMessage({ action: 'searchAUR', query: query }, function(response) {
        if (response.success) {
          handleSearchResults(response.data);
        } else {
          console.error('Error:', response.error);
        }
      });
    }
  });

function handleSearchResults(data) {
  var resultsContainer = document.getElementById('searchResults');
  resultsContainer.innerHTML = ''; // Clear previous results

  if (data.results && data.results.length > 0) {
    var ul = document.createElement('ul');
    data.results.forEach(function(package) {
      var li = document.createElement('li');

      // Create bold element for package name
      var name = document.createElement('strong');
      name.textContent = package.Name;

      // Create element for package description
      var description = document.createElement('span');
      description.textContent = ' - ' + package.Description;

      // Append name and description to list item
      li.appendChild(name);
      li.appendChild(description);

      // Append list item to the list
      ul.appendChild(li);
    });
    resultsContainer.appendChild(ul);
  } else {
    var message = document.createElement('p');
    message.textContent = 'No results found';
    resultsContainer.appendChild(message);
  }

  // Hide search box and button, show search results
  searchInput.style.display = 'none';
  searchButton.style.display = 'none';
  resultsContainer.style.display = 'block';
}


});
