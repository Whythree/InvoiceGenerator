document.addEventListener('DOMContentLoaded', () => {
    if ("content" in document.createElement("template")) {
        const addButton = document.getElementById("new_pos_btn");

        addButton.addEventListener("click", () => {
            const template = document.getElementById("invoice-position-template");
            const clone = template.content.cloneNode(true);
            const invoiceForm = document.getElementById("invoice-form");
            const positionGroup = clone.querySelector('.position-group');

            if (!positionGroup) {
                console.error("Error: .position-group not found in template");
                return;
            }

            const deletePosButton = clone.querySelector('.position-group button')

            deletePosButton.addEventListener('click', (e) => {
                positionGroup.remove();
            })
            invoiceForm.insertBefore(clone, addButton);


        })
    } else {
        alert("Please enable Javascript for this app to function correctly");
    }

})

