const getBtnSubmit = document.querySelector(".login-form__btn");

getBtnSubmit.addEventListener("click", () => {
  const getAllInputs = document.querySelectorAll(".login-form__input");
  getAllInputs.forEach((input) => {
    if (
      input.value === null ||
      input.value === "" ||
      input.value.trim() === ""
    ) {
      document.querySelector(".error-box").style.top = "1.6rem";
      setTimeout(() => {
        document.querySelector(".error-box").style.top = "-30%";
      }, 3000);
    }
  });
});
