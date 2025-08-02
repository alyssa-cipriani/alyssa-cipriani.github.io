const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const images = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"];

/* Declaring the alternative text for each image file */
const alts = {
  "pic1.jpg": "Close up of a blue human eye",
  "pic2.jpg": "Textured rock surface",
  "pic3.jpg": "Purple and white flowers",
  "pic4.jpg": "Ancient Egyptian hieroglyphs on a wall",
  "pic5.jpg": "Brown moth on a green leaf"
};

/* Looping through images */
for (let i = 0; i < images.length; i++) {
  const newImage = document.createElement('img');
  newImage.setAttribute('src', `images/${images[i]}`); // Using template literal for cleaner path
  newImage.setAttribute('alt', alts[images[i]]);
  thumbBar.appendChild(newImage);

  newImage.addEventListener('click', function() {
    displayedImage.src = this.src;
    displayedImage.alt = this.alt;
  });
}

/* Wiring up the Darken/Lighten button */
btn.addEventListener('click', function() {
  if (btn.textContent === "Darken") {
    btn.textContent = "Lighten";
    overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
  } else {
    btn.textContent = "Darken";
    overlay.style.backgroundColor = 'rgba(0,0,0,0)';
  }
});