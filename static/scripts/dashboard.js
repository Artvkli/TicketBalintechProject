const getMenuIcon = document.querySelector(".header__bars");
const getCloseMenuIcon = document.querySelector(".header-menu__close");
const getMenuItemModal = document.querySelector(".desktop-menu__item--modal");
const getModalClose = document.querySelector(".modal__close");

getMenuIcon.addEventListener("click", () => {
  document.querySelector(".header-menu").classList.add("header-menu__show");
  document.querySelector(".cover").classList.add("cover__show");
});

getCloseMenuIcon.addEventListener("click", () => {
  document.querySelector(".header-menu").classList.remove("header-menu__show");
  document.querySelector(".cover").classList.remove("cover__show");
});

getMenuItemModal.addEventListener("click", () => {
  document.querySelector(".cover-modal").classList.add("cover-modal--show");
});

getModalClose.addEventListener("click", () => {
  document.querySelector(".cover-modal").classList.remove("cover-modal--show");
});
