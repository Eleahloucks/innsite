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

    function ShowReviewForm() {
      // function GetReviewInputs(){
      //   fetch('/new-review')
      //   .then((response) => response.json())
      //   .then((data) => {
      //     alert(`The weather will be ${data.forecast}`);
      //   });
        // }
      return (
        <form action="/new-review" method="POST">
          <p>
            Name<input type="text" name="name"/>
          </p>
          <p>
            Email <input type="text" name="email"/>
          </p>
          <p>
            Location <input type="text" name="location"/>
          </p>
          <p>
            Rating <input type="text" name="score"/>
          </p>
          <p>
            Title <input type="text" name="title"/>
          </p>
          <p>
            Description <input type="text" name="body"/>
          </p>

          <p>
            <input id ="new-review" type="submit"/>
          </p>
        </form>
        );
       }

    ReactDOM.render(
      <div>
        <ShowReviewForm />
      </div>,
      document.querySelector('#review-form'),
    );
