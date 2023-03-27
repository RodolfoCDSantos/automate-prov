// Function to make API call
function search() {
    // Get search query from input field
    const searchQuery = $('#search-input').val();
    // Make API call with search query as parameter
    $.get(`https://example.com/api/search?q=${searchQuery}`, (data) => {
        // Update information section with API results
        $('#ramal').text(data.ramal);
        $('#serial').text(data.serial);
        $('#mac').text(data.mac);
        $('#ztp').text(data.ztp);
        $('#photo').attr('src', data.photo);
    });
}

// Bind search function to search button click event
$('#search-button').click(search);