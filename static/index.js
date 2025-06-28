document.addEventListener('DOMContentLoaded', () => {
    if ("content" in document.createElement("template")) {
        const addButton = document.getElementById("new_pos_btn");

        // Handle Template Cloning
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

        // Handle form submit
        const invoiceForm = document.getElementById("invoice-form");
        invoiceForm.addEventListener("submit", async (e) => {
            e.preventDefault()

            const data = []

            const positionGroup = document.querySelectorAll('.position-group');
            positionGroup.forEach(group => {

                const commissionTypeInputValue = group.querySelector('[name=commission_type]').value;
                const priceInputValue = group.querySelector('[name=price]').value;
                const quantityInputValue = group.querySelector('[name=quantity]').value;

                const groupData = {
                    "Commission Type": commissionTypeInputValue,
                    "Price": priceInputValue,
                    "Quantity": quantityInputValue,
                }

                data.push(groupData);
            })


            const submit = await fetch("/create-invoice", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)

            })
            console.log(data)

        })


    } else {
        alert("Please enable Javascript for this app to function correctly");
    }

})

