function getCanvas() {
    const elem = document.querySelector('#gameCanvas');
    return elem.getContext('2d');
}
function makeStars(count) {
    const out = [];
      for (let i=0;i<count;i++){
        const s = {
          x: Math.random()*1000,
          y: Math.random()*500
        };
      out.push(s);
    }
    return out;
}
function star(x, y, c){
    c.fillStyle = 'white';
    c.fillRect(x, y, 1, 1);
}
function draw(data) {
    let c = getCanvas();
    c.fillStyle = 'black';
    c.fillRect(0, 0, 1000, 500, c);
    let stars = Math.random() * 1000;
    let s = makeStars(stars);
    let xMod = 1000/64;
    let yMod = 500/64;
    for(let i = 0; i < s.length; i++){
        const next = s[i];
        var x = next.x;
        var y = next.y;
        star(x, y, c);
    }
    for (var objId of Object.values(data.world.objects)) {
        if(objId.objType == "Ship"){
            c.fillStyle = "blue";
            c.beginPath();
            c.moveTo(objId.position.x*xMod + 10, objId.position.y*yMod);
            c.lineTo(objId.position.x*xMod + 20, objId.position.y*yMod + 20);
            c.lineTo(objId.position.x*xMod + 10, objId.position.y*yMod + 15);
            c.lineTo(objId.position.x*xMod, objId.position.y*yMod + 20);
            c.closePath();
            c.fill();
            c.stroke();
        }
        if(objId.objType == "Station"){
            c.fillStyle = "yellow";
            c.beginPath();
            c.moveTo(objId.position.x*xMod, objId.position.y*yMod);
            c.lineTo(objId.position.x*xMod + 10, objId.position.y*yMod + 5)
            c.lineTo(objId.position.x*xMod + 20, objId.position.y*yMod)
            c.lineTo(objId.position.x*xMod + 15, objId.position.y*yMod + 10)
            c.lineTo(objId.position.x*xMod + 20, objId.position.y*yMod + 20);
            c.lineTo(objId.position.x*xMod + 10, objId.position.y*yMod + 15);
            c.lineTo(objId.position.x*xMod, objId.position.y*yMod + 20);
            c.lineTo(objId.position.x*xMod + 5, objId.position.y*yMod + 10)
            c.closePath();
            c.fill();
            c.stroke();
        }
        if(objId.objType == "Asteroid"){
            c.fillStyle = "rgb(214, 208, 193)";
            c.beginPath();
            c.moveTo(objId.position.x*xMod + 4, objId.position.y*yMod + 2);
            c.lineTo(objId.position.x*xMod + 10, objId.position.y*yMod)
            c.lineTo(objId.position.x*xMod + 17, objId.position.y*yMod+4)
            c.lineTo(objId.position.x*xMod + 20, objId.position.y*yMod + 4)
            c.lineTo(objId.position.x*xMod + 20, objId.position.y*yMod + 9);
            c.lineTo(objId.position.x*xMod + 16, objId.position.y*yMod + 20);
            c.lineTo(objId.position.x*xMod + 10, objId.position.y*yMod + 17);
            c.lineTo(objId.position.x*xMod + 4, objId.position.y*yMod + 20);
            c.lineTo(objId.position.x*xMod + 0, objId.position.y*yMod + 10);
            c.closePath();
            c.fill();
            c.stroke();
        }
    }
}

fetch('/api/game').then(response => response.json()).then(json => {
    let data = json;
    console.log(data);
    draw(data);
})
