var b1 = document.getElementById("b1")
var b3 = document.getElementById("b3")

/*for quantity*/
b1.addEventListener('click', () => {
    var quantity = document.getElementById("quantity")
    var b2 = document.getElementById("b2")
    var q = parseInt(b2.innerText)

    if (q === 1) {
        b2.textContent = 1
        quantity.setAttribute('value', 1)
    } else {
        b2.textContent = q - 1
        quantity.setAttribute('value', q - 1)
    }
});


b3.addEventListener('click', () => {
    var quantity = document.getElementById("quantity")
    var b2 = document.getElementById("b2")
    var q = parseInt(b2.innerText)
    b2.textContent = q + 1
    quantity.setAttribute('value', q + 1)
});


/*for size*/
var s1 = document.getElementById("s1")
var s2 = document.getElementById("s2")
var s3 = document.getElementById("s3")
var s4 = document.getElementById("s4")


s1.addEventListener('click', () => {
    var size = document.getElementById("size")
    size.setAttribute('value', 's')
});


s2.addEventListener('click', () => {
    var size = document.getElementById("size")
    size.setAttribute('value', 'm')
});


s3.addEventListener('click', () => {
    var size = document.getElementById("size")
    size.setAttribute('value', 'l')
});


s4.addEventListener('click', () => {
    var size = document.getElementById("size")
    size.setAttribute('value', 'xl')
});