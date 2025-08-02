const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const images = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"];

/* Declaring the alternative text for each image file */
const alts ={

"pic1.jpg": "close up of human eye ",

"pic2.jpg": "textured rock",

"pic3.jpg": "white and purple flowers",

"pic4.jpg": "Egyptian hieroglyphs",

"pic5.jpg": "brown moth on a leaf"
}

/* Looping through images */
for (let i = 0; i < images.length; i++) {
  const newImage = document.createElement('img');
  newImage.src = `./images/${images[i]}`;
  newImage.alt = alts[images[i]];
  thumbBar.appendChild(newImage);

  newImage.addEventListener('click', function() {
    displayedImage.src = this.src;
    displayedImage.alt = this.alt;
  });
}  

/* Wiring up the Darken/Lighten button */
btn.addEventListener('click',function(){
	if(btn.textContent === "Darken"){
		btn.textContent = "Lighten"
		overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
	}
	else{
		btn.txtContent = "Darken";
		overlay.style.backgroundColor = 'rgba(0,0,0,0)';
	}
});