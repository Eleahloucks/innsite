// jsx has to be compiled into javascript because it has HTML in it.
// add a dynamic route where customer leaves review
// user gets a react front end
  //area to write review
  //button to submit
  //edit
  //see current reviews
//event handler with ajax request that send text
   //going to post that contains text
    //create route to reviews page form
    //input area form

// do i want to update whole page
// if no, what info do i need?
//add event listener
    function ShowReviewForm() {

      return (
        <form action="/new-review" method="POST">
          <h5>
            Name:<input type="text" name="name"/>
          </h5>
          <h5>
            Email: <input type="text" name="email"/>
          </h5>
          <h5>
            Location: <input type="text" name="location"/>
          </h5>
          <h5>
            Rating: <input type="text" name="score"/>
          </h5>
          <h5>
            Title: <input type="text" name="title"/>
          </h5>
          <h5>
            Description: <input type="text" name="body"/>
          </h5>


          <h4>
            <input class="btn innsite-button-green"id ="new-review" type="submit"/>
          </h4>
        </form>
        );
       }

    ReactDOM.render(
      <div>
        <ShowReviewForm />
      </div>,
      document.querySelector('#review-form'),
    );
