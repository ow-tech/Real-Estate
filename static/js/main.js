const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');

}, 3000);


// lightbox.option({
//     'fitImagesInViewport': false,
//     'maxWidth': 1000,
//     'maxHeight': 1000
//   })

// lightbox.option({
//     'fitImagesInViewport': false
//   })
