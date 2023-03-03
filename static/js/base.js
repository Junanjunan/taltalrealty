function togglePrice(event) {
    const divPrice = document.querySelector("#div_price");
    if (event.target.value == 'sell') {
        divPrice.setAttribute('style', 'display:inline;')
    } else {
        divPrice.setAttribute('style', 'display:none;')
    }
}