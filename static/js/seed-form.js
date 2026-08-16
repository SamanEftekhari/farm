document.addEventListener("DOMContentLoaded", function () {

    const cropSelect = document.getElementById("id_crop");
    const varietySelect = document.getElementById("id_variety");

    if (!cropSelect || !varietySelect) {
        return;
    }

    cropSelect.addEventListener("change", function () {

        const cropId = this.value;

        varietySelect.innerHTML = "";

        const defaultOption = document.createElement("option");

        defaultOption.value = "";
        defaultOption.textContent = "در حال بارگذاری...";

        varietySelect.appendChild(defaultOption);

        if (!cropId) {

            varietySelect.innerHTML = "";

            const option = document.createElement("option");

            option.value = "";
            option.textContent = "ابتدا محصول را انتخاب کنید";

            varietySelect.appendChild(option);

            return;
        }


        fetch(`/crops/api/varieties/${cropId}/`)
            .then(response => {

                if (!response.ok) {
                    throw new Error("خطا در دریافت ارقام");
                }

                return response.json();
            })

            .then(data => {

                varietySelect.innerHTML = "";

                const defaultOption = document.createElement("option");

                defaultOption.value = "";
                defaultOption.textContent = "انتخاب رقم";

                varietySelect.appendChild(defaultOption);


                if (data.length === 0) {

                    const option = document.createElement("option");

                    option.value = "";
                    option.textContent = "برای این محصول رقمی ثبت نشده است";

                    varietySelect.appendChild(option);

                    return;
                }


                data.forEach(function (variety) {

                    const option = document.createElement("option");

                    option.value = variety.id;

                    option.textContent =
                        variety.code
                            ? `${variety.name} (${variety.code})`
                            : variety.name;

                    varietySelect.appendChild(option);

                });

            })

            .catch(error => {

                console.error(error);

                varietySelect.innerHTML = "";

                const option = document.createElement("option");

                option.value = "";
                option.textContent = "خطا در دریافت ارقام";

                varietySelect.appendChild(option);

            });

    });

});