const searchInput = document.querySelector("[data-search]");
const contactCardSearch = document.querySelectorAll("[data-search-div]")

searchInput.addEventListener("input", (event) => {
    const value = event.target.value.toLowerCase();

    contactCardSearch.forEach(contact => {
        console.log(contact);
        const isVisible = contact.outerText.toLowerCase().includes(value);
        contact.classList.toggle("hide", !isVisible);
    })
});