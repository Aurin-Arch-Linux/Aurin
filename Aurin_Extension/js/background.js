chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'searchAUR') {
    var endpoint = 'https://aur.archlinux.org/rpc/?v=5&type=search&arg=' + encodeURIComponent(request.query);
    fetch(endpoint)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        sendResponse({ success: true, data: data });
      })
      .catch(error => {
        sendResponse({ success: false, error: error.message });
      });
    return true; // Need to return true to indicate that we'll be responding asynchronously
  }
});
