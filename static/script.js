
cards.forEach(card => {

let title =
card.querySelector("h3")
.innerText
.toLowerCase();

if(title.includes(input)){

card.style.display = "block";

}

else{

card.style.display = "none";

}

});

function startScraping(){

let btn =
document.querySelector(".scrape-btn");

btn.innerHTML =
"🔄 Scraping Data...";

btn.disabled = true;

setTimeout(() => {

btn.innerHTML =
"✅ Scraping Completed";

setTimeout(() => {

location.reload();

},1000);

},2500);

}

function downloadCSV(){

window.location.href = "/products.csv";

}

function searchProducts(){

let input =
document.getElementById("searchInput")
.value
.toLowerCase();

let cards =
document.querySelectorAll(".card");

let noResults =
document.getElementById("noResults");

if(input === ""){

    cards.forEach(card => {
        card.style.display = "block";
    });

    noResults.style.display = "none";

    document.getElementById("suggestions").innerHTML = "";

    return;
}

let found = false;

cards.forEach(card => {

let text =
card.innerText.toLowerCase();

if(text.includes(input)){

card.style.display = "block";
found = true;

}
else{

card.style.display = "none";

}

});

noResults.style.display =
found ? "none" : "block";

}

document
.getElementById("searchInput")
.addEventListener("keypress",

function(event){

if(event.key==="Enter"){

searchProducts();

}

});

function filterProducts(category){

let cards =
document.querySelectorAll(".card");

cards.forEach(card => {

let cardCategory =
card.dataset.category;

if(
category === "all" ||
cardCategory === category
){

card.style.display = "block";

}
else{

card.style.display = "none";

}

});
updateCount();
}

function setActive(button){

document
.querySelectorAll(".filters button")
.forEach(btn => {

btn.classList.remove(
"active-filter"
);

});

button.classList.add(
"active-filter"
);

}

function updateCount(){

let visibleCards =
document.querySelectorAll(
'.card:not([style*="display: none"])'
);

document.getElementById("productCount").innerText =
`Showing ${visibleCards.length} Products`;

let count = visibleCards.length;

if(count === 0){

document.getElementById("noResults")
.innerText =
"❌ No Products Found";

}
else{

document.getElementById("noResults")
.innerText = "";

}
}

window.onscroll = function(){

const btn = document.getElementById("topBtn");

if(document.documentElement.scrollTop > 500){

btn.style.display = "block";

}
else{

btn.style.display = "none";

}

}

function topFunction(){

window.scrollTo({
top:0,
behavior:"smooth"
});

}

function showSuggestions(){

    let input =
    document.getElementById("searchInput")
    .value
    .toLowerCase();

    let cards =
    document.querySelectorAll(".card");

    let suggestions =
    document.getElementById("suggestions");

    suggestions.innerHTML = "";

    if(input.length < 1){

    suggestions.innerHTML = "";

    searchProducts();

    return;
}
    cards.forEach(card=>{

        let title =
        card.querySelector("h3")
        .innerText;

        if(
        title.toLowerCase()
        .includes(input)
        ){

            let item =
            document.createElement("div");

            item.className =
            "suggestion-item";

            item.innerText =
            title;

            item.onclick = function(){

                document.getElementById(
                "searchInput"
                ).value = title;

                searchProducts();

                suggestions.innerHTML="";
            }

            suggestions.appendChild(item);
        }

    });

}

document.getElementById("searchInput")
.addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        searchProducts();
    }

});

function openModal(
image,
title,
price,
category,
rating
){

document.getElementById(
"productModal"
).style.display = "block";

document.getElementById(
"modalImage"
).src = image;

document.getElementById(
"modalTitle"
).innerText = title;

document.getElementById(
"modalPrice"
).innerText = price;

document.getElementById(
"modalCategory"
).innerText =
"Category: " + category;

document.getElementById(
"modalRating"
).innerText =
"⭐ Rating: " + rating;

}

function closeModal(){

document.getElementById(
"productModal"
).style.display = "none";

}

function sortProducts(type){

let products =
document.querySelector(".products");

let cards =
Array.from(
document.querySelectorAll(".card")
);

if(type === "low"){

cards.sort((a,b)=>{

return parseInt(
a.dataset.price.replace("₹","")
)
-
parseInt(
b.dataset.price.replace("₹","")
);

});

}

if(type === "high"){

cards.sort((a,b)=>{

return parseInt(
b.dataset.price.replace("₹","")
)
-
parseInt(
a.dataset.price.replace("₹","")
);

});

}

if(type === "rating"){

cards.sort((a,b)=>{

return parseFloat(
b.dataset.rating
)
-
parseFloat(
a.dataset.rating
);

});

}

products.innerHTML = "";

cards.forEach(card=>{

products.appendChild(card);

});

}