// Obtén referencias a elementos HTML
const openPopupButtons = document.querySelectorAll(".openPopupButton");
const popup = document.getElementById("popup");
const closePopupButtons = document.querySelectorAll(".closeButton");

function openPopup(eventId) {
    const popup = document.getElementById(`popup-${eventId}`);
    if (popup) {
        console.log("Abriendo popup:", eventId);
        popup.style.display = "block";
    }
}

function closePopup(eventId) {
    const popup = document.getElementById(`popup-${eventId}`);
    if (popup) {
        console.log("Cerrando popup:", eventId);
        popup.style.display = "none";
    }
}

// Asocia eventos a los botones
openPopupButtons.forEach(button => {
    const eventId = button.getAttribute("data-event-id");
    button.addEventListener("click", () => {
        openPopup(eventId);
    });
});

closePopupButtons.forEach(button => {
    const eventId = button.getAttribute("data-event-id");
    button.addEventListener("click", () => {
        closePopup(eventId);
    });
});