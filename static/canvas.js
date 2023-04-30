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
function ship(objID, c) {
    /**
     *  var dir;
     *  let up = [[10,0],[20,20],[10,15],[0,20]];
        let left = [[0,10],[20,0],[15,10],[20,20]];
        let down = [[10,20],[0,0],[10,5],[20,0]];
        let right = [[20,10],[0,0],[5,10],[0,20]];
        if (objID.direction == "left") dir = left;
        if (objID.direction == "right") dir = right;
        if (objID.direction == "down") dir = down;
        else dir = up;
        c.moveTo(objID.position.x*xMod + dir[0][0], objID.position.y*yMod + dir[0][1]);
        c.lineTo(objID.position.x*xMod + dir[1][0], objID.position.y*yMod + dir[1][1]);
        c.lineTo(objID.position.x*xMod + dir[2][0], objID.position.y*yMod + dir[2][1]);
        c.lineTo(objID.position.x*xMod + dir[3][0], objID.position.y*yMod + dir[3][1]);
     */
    c.fillStyle = "blue";
    c.beginPath();
    c.moveTo(objID.position.x*xMod + 10, objID.position.y*yMod);
    c.lineTo(objID.position.x*xMod + 20, objID.position.y*yMod + 20);
    c.lineTo(objID.position.x*xMod + 10, objID.position.y*yMod + 15);
    c.lineTo(objID.position.x*xMod, objID.position.y*yMod + 20);
    c.closePath();
    c.fill();
    c.stroke();
}
function station(objID, c){
    c.fillStyle = "yellow";
    c.beginPath();
    c.moveTo(objID.position.x*xMod, objID.position.y*yMod);
    c.lineTo(objID.position.x*xMod + 10, objID.position.y*yMod + 5)
    c.lineTo(objID.position.x*xMod + 20, objID.position.y*yMod)
    c.lineTo(objID.position.x*xMod + 15, objID.position.y*yMod + 10)
    c.lineTo(objID.position.x*xMod + 20, objID.position.y*yMod + 20);
    c.lineTo(objID.position.x*xMod + 10, objID.position.y*yMod + 15);
    c.lineTo(objID.position.x*xMod, objID.position.y*yMod + 20);
    c.lineTo(objID.position.x*xMod + 5, objID.position.y*yMod + 10)
    c.closePath();
    c.fill();
    c.stroke();
}
function asteroid(objID, c) {
    /**
     *  var dir;
     *  let up = [[4,2],[10,0],[17,4],[20,4],[20,9],[16,20],[10,17],[4,20],[0,10]];
        let left = [[2,16],[0,10],[4,3],[4,0],[9,0],[20,4],[17,10],[20,16],[10,20]];
        let down = [[16,18],[10,20],[3,16],[0,16],[0,11],[4,0],[10,3],[16,0],[20,10]];
        let right = [[18,4],[20,10],[16,17],[16,20],[11,20],[0,16],[3,10],[0,4],[10,0]];
        if (objID.direction == "left") dir = left;
        if (objID.direction == "right") dir = right;
        if (objID.direction == "down") dir = down;
        else dir = up;
        c.moveTo(objID.position.x*xMod + dir[0][0], objID.position.y*yMod + dir[0][1]);
        c.lineTo(objID.position.x*xMod + dir[1][0], objID.position.y*yMod + dir[1][1]);
        c.lineTo(objID.position.x*xMod + dir[2][0], objID.position.y*yMod + dir[2][1]);
        c.lineTo(objID.position.x*xMod + dir[3][0], objID.position.y*yMod + dir[3][1]);
        c.moveTo(objID.position.x*xMod + dir[4][0], objID.position.y*yMod + dir[4][1]);
        c.lineTo(objID.position.x*xMod + dir[5][0], objID.position.y*yMod + dir[5][1]);
        c.lineTo(objID.position.x*xMod + dir[6][0], objID.position.y*yMod + dir[6][1]);
        c.lineTo(objID.position.x*xMod + dir[7][0], objID.position.y*yMod + dir[7][1]);
        c.lineTo(objID.position.x*xMod + dir[8][0], objID.position.y*yMod + dir[8][1]);
     */
    c.fillStyle = "rgb(214, 208, 193)";
    c.beginPath();
    c.moveTo(objID.position.x*xMod + 4, objID.position.y*yMod + 2);
    c.lineTo(objID.position.x*xMod + 10, objID.position.y*yMod)
    c.lineTo(objID.position.x*xMod + 17, objID.position.y*yMod+4)
    c.lineTo(objID.position.x*xMod + 20, objID.position.y*yMod + 4)
    c.lineTo(objID.position.x*xMod + 20, objID.position.y*yMod + 9);
    c.lineTo(objID.position.x*xMod + 16, objID.position.y*yMod + 20);
    c.lineTo(objID.position.x*xMod + 10, objID.position.y*yMod + 17);
    c.lineTo(objID.position.x*xMod + 4, objID.position.y*yMod + 20);
    c.lineTo(objID.position.x*xMod + 0, objID.position.y*yMod + 10);
    c.closePath();
    c.fill();
    c.stroke();
}
function draw(data, c) {
    c.fillStyle = 'black';
    c.fillRect(0, 0, 1000, 500, c);
    let stars = Math.random() * 1000;
    let s = makeStars(stars);
    for(let i = 0; i < s.length; i++){
        const next = s[i];
        var x = next.x;
        var y = next.y;
        star(x, y, c);
    }
    for (var objId of Object.values(data.world.objects)) {
        if(objId.objType == "Ship"){
            ship(objId, c);
        }
        if(objId.objType == "Station"){
            station(objId, c);
        }
        if(objId.objType == "Asteroid"){
            asteroid(objId, c);
        }
    }
}
const xMod = 1000/64;
const yMod = 500/64;
const c = getCanvas();
fetch('/api/game').then(response => response.json()).then(json => {
    let data = json;
    console.log(data);
    draw(data, c);
})
