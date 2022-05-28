const url = 'http://localhost:8000/api/v1/cars'

let headers = {}

console.log(fetch(url, {
    method : "GET",
    mode: 'cors',
    headers: headers
}))
