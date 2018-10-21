//events are actions done by the user on a webpage (like a button click)

// var button = document.getElementsByTagName("button")[0]; //selects button
// //make sure you add array so that it selects the first button
// button.addEventListener("click", function(){
//   console.log("CLICK!!!!");
// }); //listens for a button click (first paramenter), logs it (second parameter is)
// //is function
// button.addEventListener("mouseenter", function(){
//   console.log("ENTER!!!!");
// });
//
// button.addEventListener("mouseleave", function(){
//   console.log("LEAVE!!!!");
// });


//usually easier for web browsers to grab ids because there is only 1 of them
var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");
var listItem = document.querySelectorAll("li");

function inputLength() {
 return input.value.length;
};

function createListElement() {
  var li = document.createElement("li"); //creates a new list item when pressed
  li.appendChild(document.createTextNode(input.value));
  //creates a text node to add to list with the label that is supplied in input
  var delButton = document.createElement("button");
  delButton.innerHTML = "Delete";
  li.appendChild(delButton);
  delButton.classList.add("delbtn");
  ul.appendChild(li); //appends the list item to the unordered list
  input.value = ""; //makes the input section empty
  delButton.addEventListener("click", deleteTask);
}

function addListAfterClick() {
  if (inputLength() > 0){ //makes it so empty objects can't be added
    createListElement();
  }
}

function addListAfterKeypress(event) {
  if (inputLength() > 0 && event.keyCode === 13) {
    //event.keyCode makes it so that if the enter key (key code 13) is pressed
    //then the function executes
    createListElement();
  }
}

function itemDone(event){
  event.target.classList.toggle("done");
}

function addDelButton() {
  for (var i=0; i < listItem.length; i++) {
    var delButton = document.createElement("button");
    delButton.innerHTML = "Delete";
    listItem[i].appendChild(delButton);
    delButton.classList.add("delbtn");
  };
};

function binding() {
  function bindTaskEvents(taskListItem) {
    var delButton = document.querySelectorAll(".delbtn")[i];
    delButton.addEventListener("click", deleteTask);
  };

  for(var i=0; i < ul.children.length; i++) {
    bindTaskEvents(ul.children[i]);
  };
};

button.addEventListener("click", addListAfterClick);

input.addEventListener("keypress", addListAfterKeypress); //make sure this is input

ul.addEventListener("click", itemDone);

addDelButton();

function deleteTask() {
  var listItem = this.parentNode;
  var ul = listItem.parentNode;
  ul.removeChild(listItem);
};

function bindTaskEvents(taskListItem) {
  var delButton = document.querySelectorAll(".delbtn")[i];
  delButton.addEventListener("click", deleteTask);
};

for(var i=0; i < ul.children.length; i++) {
  bindTaskEvents(ul.children[i]);
};
