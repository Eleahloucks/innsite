'use strict';
console.log('js connected');

// BOOKING  AJAX

const button = document.querySelector('#book-now');

button.addEventListener('click', () => {
  //need to access the specific location url "/locations/<location_id>
  const locationId = document.querySelector('#location_id').value
  const url = `/locations/${locationId}`;
  //save the inputs to the session
  const bookingInputs = {
    //arrival and departure are going to be dates, do i use datetime to handle that?
    arrival: document.querySelector('#arrival').value,
    departure: document.querySelector('#departure').value,
    location: document.querySelector('#location').value
  }
  console.log(bookingInputs);
  fetch(url, {
      //post resquests to save inputs
      method: 'POST',
      body: JSON.stringify(bookingInputs),
      headers: {
        'Content-Type': 'application/json',
      },
  })
    //response from booking route server
    //Does this add my data to the session? do i need to import session?
    .then((response) => response.json())
    .then((bookingJson) => {
      //is this syntax correct?
      alert(bookingJson.status)
    });
});

