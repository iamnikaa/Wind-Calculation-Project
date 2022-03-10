// set canvas id to variable
var canvas = document.getElementById("draw");

// get canvas 2D context and set it to the correct size
var ctx = canvas.getContext("2d");

// resize canvas when window is resized
function resize() {
  ctx.canvas.width = 1500; // window.innerWidth
  ctx.canvas.height = 800; // window.innerHeight
}

resize();

// var gridSize = document.getElementById("gridSpacing").value;  //gridsize = 50 inititally
var gridSize = 50;
var count = 0;  // to count how many objects are drawn

// draw grid on the canvas
function drawBoard(){

  // get grid size from DOM
  // gridSize = document.getElementById("gridSpacing").value;

  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  
  for (var x = 0; x <= ctx.canvas.width; x += gridSize) {
      ctx.moveTo(0.5 + x, 0);
      ctx.lineTo(0.5 + x, ctx.canvas.height);
  }

  for (var x = 0; x <= ctx.canvas.height; x += gridSize) {
      ctx.moveTo(0, 0.5 + x);
      ctx.lineTo(ctx.canvas.width, 0.5 + x);
  }

  count = 0; // reset point count to 0
  ctx.lineWidth = 0.2; // width of line
  ctx.lineCap = "butt"; // butt end cap
  ctx.strokeStyle = "grey";
  ctx.stroke();
  // ctx.fillText(gridSize, 500, 500)  // checking if gridsize is changing
}

drawBoard();  // call function to draw grid

// last known position
var pos = { x: 0, y: 0 };

// new position from mouse events
function setPosition(e) {
  pos.x = Math.round((e.clientX - 5)/gridSize) * gridSize;
  pos.y = Math.round((e.clientY - 30)/gridSize) * gridSize;
}

// draw lines on mouse events
function draw(e) {
    if (e.buttons !== 1) return; // if mouse is not clicked, do not go further
 
    var color = document.getElementById("hex").value;

    ctx.beginPath(); // begin the drawing path
    
    // line properties
    ctx.lineWidth = 5; // width of line
    ctx.lineCap = "round"; // rounded end cap
    ctx.strokeStyle = color; // hex color of line
    ctx.fillStyle = '#00F';
    ctx.font = 'Italic 20px Sans-Serif';
    ctx.textBaseline = 'top';

    // draw line
    ctx.moveTo(pos.x, pos.y); // from position
}

// stroke lines on mouseup
function drawline(e) {
    count += 1;
    setPosition(e);
    if (pos.y > 0) {
      ctx.lineTo(pos.x, pos.y); // to position
      ctx.fillText(pos.y, pos.x, pos.y)
    }
    // ctx.fillText(count, pos.x, pos.y);  // add text at draw nodes
    ctx.stroke(); // draw it!
}

// add window event listener to trigger when window is resized
window.addEventListener("resize", resize);

// add event listeners to trigger on different mouse events
document.addEventListener("mousemove", draw);
document.addEventListener("mousedown", setPosition);
document.addEventListener("mouseup", drawline);
document.addEventListener("mouseenter", setPosition);

// function to generate random numbers
function getRndNum(min, max) {
  return ((Math.random() * (max - min + 1)) + min).toFixed(2);
}

// function to display results
function calc() {
  ctx.clearRect(ctx.canvas.width - 350, 0, ctx.canvas.width, ctx.canvas.height);
  ctx.fillStyle = "black"
  ctx.font = 'Bold 30px Aerial';
  for (i=1; i<=12; i++) {
    textPrint = "Direction " + i + ": " + getRndNum(1,2) + " Units";
    ctx.fillText(textPrint, ctx.canvas.width - 350, i*30);
  }
}

