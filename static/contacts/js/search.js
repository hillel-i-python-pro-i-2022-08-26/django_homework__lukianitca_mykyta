const searchInput = document.querySelector("[data-search]");
const contactCardSearch = document.querySelectorAll("[data-contact-div]")

searchInput.addEventListener("input", (event) => {
    const value = event.target.value.toLowerCase();
    contactCardSearch.forEach(contact => {
        const isVisible = contact.childNodes[1].textContent.toLowerCase().includes(value);
        contact.classList.toggle("hide", !isVisible);
    })
});