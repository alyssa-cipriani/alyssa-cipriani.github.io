
const images = [
  "pic1.jpg",
  "pic2.jpg",
  "pic3.jpg",
  "pic4.jpg",
  "pic5.jpg"
];

const alts = {
  "pic1.jpg": "close up of human eye",
  "pic2.jpg": "textured rock",
  "pic3.jpg": "white and purple flowers",
  "pic4.jpg": "Egyptian hieroglyphs",
  "pic5.jpg": "brown moth on a leaf"
};

const displayedImage = document.querySelector(".displayed-img");
const thumbBar       = document.querySelector(".thumb-bar");
const btn            = document.querySelector("button");
const overlay        = document.querySelector(".overlay");

for (let i = 1; i <= images.length; i++) {
  const filename = `pic${i}.jpg`;
  const thumb    = document.createElement("img");

  thumb.src = `images/${filename}`;
  thumb.alt = alts[filename];
  thumbBar.appendChild(thumb);
  thumb.addEventListener("click", () => {
    displayedImage.src = thumb.src;
    displayedImage.alt = thumb.alt;
  });
}

btn.addEventListener("click", () => {
  const btnClass = btn.getAttribute("class");  

  if (btnClass === "dark") {
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    btn.textContent               = "Lighten";
    btn.setAttribute("class", "light");
  } else {
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0)";
    btn.textContent               = "Darken";
    btn.setAttribute("class", "dark");
  }
});
