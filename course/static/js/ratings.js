const rate = (rating, course) => {
    console.log("RATING: ", rating)
    console.log("COURSE: ", course)
    fetch(`/rating/${rating}/${course}` , {
        method : 'GET',
        headers : {
            'Content-Type' : "application/json"
        }
    }).then(res => {
        window.location.reload()
    })
}