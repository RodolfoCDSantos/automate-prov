// Function to make API call
function search() {
    // create and add the ramal element
    const clientElement = document.getElementById('client');
    if (!clientElement) {
      // create and add the client element
      const newClientElement = document.createElement('h2');
      newClientElement.id = 'client';
      newClientElement.className = 'text-center'
      newClientElement.innerHTML = 'Cliente teste';
    
      // add the new element to the result div
      const resultDiv = document.getElementById('result');
      resultDiv.appendChild(newClientElement);
    }

    addInfo('1234', 'ABCD1234', '00:11:22:33:44:55', true, 'https://example.com/photo.jpg');
  }


function addInfo(ramal, serial, mac, ztp, photo_url) {
    // create a new div element
    const div = document.createElement('div');
    div.className = 'info-div';

    // create and add the ramal element
    const ramalElement = document.createElement('p');
    ramalElement.innerHTML = `<strong>Ramal:</strong> <span>${ramal}</span>`;
    div.appendChild(ramalElement);
  
    // create and add the serial element
    const serialElement = document.createElement('p');
    serialElement.innerHTML = `<strong>Serial:</strong> <span>${serial}</span>`;
    div.appendChild(serialElement);
  
    // create and add the mac element
    const macElement = document.createElement('p');
    macElement.innerHTML = `<strong>MAC:</strong> <span>${mac}</span>`;
    div.appendChild(macElement);
  
    // create and add the ztp element
    const ztpElement = document.createElement('p');
    ztpElement.innerHTML = `<strong>ZTP:</strong> <span>${ztp}</span>`;
    div.appendChild(ztpElement);
  
    // create and add the photo element
    const photoElement = document.createElement('img');
    photoElement.id = 'photo';
    photoElement.src = photo_url;
    photoElement.alt = 'Photo';
    photoElement.className = 'img-fluid mb-3';
    div.appendChild(photoElement);
  
    // add the new div to the result div
    const resultDiv = document.getElementById('result');
    resultDiv.appendChild(div);
    console.log(resultDiv)
  }

  // Bind search function to search button click event
$('#search-button').click(search);