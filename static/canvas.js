function getCanvas(elem) {
    return elem.getContext('2d');
}
function makeStars(count, xMin, xMax, yMin, yMax) {
    const out = [];
    for (let i = 0; i < count; i++) {
        const s = {
            x: Math.random() * (xMax - xMin) + xMin,
            y: Math.random() * (yMax - yMin) + yMin
        };
        out.push(s);
    }
    return out;
}
function star(s, c) {
    for (let i = 0; i < s.length; i++) {
        c.beginPath();
        c.fillStyle = 'white';
        const next = s[i];
        c.fillRect(next.x, next.y, 1, 1);
    }
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
        c.moveTo(objID.position.x*XMod + dir[0][0], objID.position.y*YMod + dir[0][1]);
        c.lineTo(objID.position.x*XMod + dir[1][0], objID.position.y*YMod + dir[1][1]);
        c.lineTo(objID.position.x*XMod + dir[2][0], objID.position.y*YMod + dir[2][1]);
        c.lineTo(objID.position.x*XMod + dir[3][0], objID.position.y*YMod + dir[3][1]);
     */
    c.fillStyle = "blue";
    c.beginPath();
    c.moveTo(objID.position.x * XMod + 10, objID.position.y * YMod);
    c.lineTo(objID.position.x * XMod + 20, objID.position.y * YMod + 20);
    c.lineTo(objID.position.x * XMod + 10, objID.position.y * YMod + 15);
    c.lineTo(objID.position.x * XMod, objID.position.y * YMod + 20);
    c.closePath();
    c.fill();
    c.stroke();
}
function station(objID, c) {
    c.fillStyle = "yellow";
    c.beginPath();
    c.moveTo(objID.position.x * XMod, objID.position.y * YMod);
    c.lineTo(objID.position.x * XMod + 10, objID.position.y * YMod + 5)
    c.lineTo(objID.position.x * XMod + 20, objID.position.y * YMod)
    c.lineTo(objID.position.x * XMod + 15, objID.position.y * YMod + 10)
    c.lineTo(objID.position.x * XMod + 20, objID.position.y * YMod + 20);
    c.lineTo(objID.position.x * XMod + 10, objID.position.y * YMod + 15);
    c.lineTo(objID.position.x * XMod, objID.position.y * YMod + 20);
    c.lineTo(objID.position.x * XMod + 5, objID.position.y * YMod + 10)
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
        c.moveTo(objID.position.x*XMod + dir[0][0], objID.position.y*YMod + dir[0][1]);
        c.lineTo(objID.position.x*XMod + dir[1][0], objID.position.y*YMod + dir[1][1]);
        c.lineTo(objID.position.x*XMod + dir[2][0], objID.position.y*YMod + dir[2][1]);
        c.lineTo(objID.position.x*XMod + dir[3][0], objID.position.y*YMod + dir[3][1]);
        c.moveTo(objID.position.x*XMod + dir[4][0], objID.position.y*YMod + dir[4][1]);
        c.lineTo(objID.position.x*XMod + dir[5][0], objID.position.y*YMod + dir[5][1]);
        c.lineTo(objID.position.x*XMod + dir[6][0], objID.position.y*YMod + dir[6][1]);
        c.lineTo(objID.position.x*XMod + dir[7][0], objID.position.y*YMod + dir[7][1]);
        c.lineTo(objID.position.x*XMod + dir[8][0], objID.position.y*YMod + dir[8][1]);
     */
    c.fillStyle = "rgb(214, 208, 193)";
    c.beginPath();
    c.moveTo(objID.position.x * XMod + 4, objID.position.y * YMod + 2);
    c.lineTo(objID.position.x * XMod + 10, objID.position.y * YMod)
    c.lineTo(objID.position.x * XMod + 17, objID.position.y * YMod + 4)
    c.lineTo(objID.position.x * XMod + 20, objID.position.y * YMod + 4)
    c.lineTo(objID.position.x * XMod + 20, objID.position.y * YMod + 9);
    c.lineTo(objID.position.x * XMod + 16, objID.position.y * YMod + 20);
    c.lineTo(objID.position.x * XMod + 10, objID.position.y * YMod + 17);
    c.lineTo(objID.position.x * XMod + 4, objID.position.y * YMod + 20);
    c.lineTo(objID.position.x * XMod + 0, objID.position.y * YMod + 10);
    c.closePath();
    c.fill();
    c.stroke();
}
function draw(data, tile, c) {
    //obj = Object.values(data.world.objects).filter(x => x.position.tileName == tileName);
    inTile = true;
    c.fillStyle = 'black';
    c.fillRect(0, 0, 1000, 500, c);
    let stars = Math.random() * 1000;
    let s = makeStars(stars, 0, XMax, 0, YMax);
    star(s, c);
    console.log('yay');
    console.log(tile);
    for (var objId of Object.values(data.world.objects)) {
        if (objId.objType == "Ship" && objId.position.tile == tile) {
            ship(objId, c);
        }
        if (objId.objType == "Station" && objId.position.tile == tile) {
            station(objId, c);
        }
        if (objId.objType == "Asteroid" && objId.position.tile == tile) {
            asteroid(objId, c);
        }
    }
}
function drawMapTile(tile, numTiles, c) {
    let xTiles = Math.ceil(numTiles / Math.floor(numTiles / 4)) + 1;
    let yTiles = Math.floor(numTiles / 4);
    let xStep = XMax / xTiles;
    let yStep = YMax / yTiles;
    let yPos = 0;
    let xPos = 0;
    if (mapTilePos.size >= xTiles) {
        yPos = 1;
        xPos = mapTilePos.size - xTiles;
    }
    else {
        yPos = 0;
        xPos = mapTilePos.size;
    }
    let x = 0;
    if (yPos != 0) {
        x = xPos * xStep + xStep;
    }
    else x = xPos * xStep + xStep / 2;
    let y = yPos * yStep + yStep / 2;
    let r = xStep / 3;
    mapTilePos.set(tile, {
        x: x,
        y: y,
        r: r
    });
    drawTile(tile, c)
}
function drawTile(tile, c) {
    c.beginPath();
    let temp = mapTilePos.get(tile);
    c.arc(temp.x, temp.y, temp.r, 0, Math.PI * 2);
    c.fillStyle = 'black';
    c.fill();
    let s = makeStars(25, temp.x - temp.r, temp.x + temp.r, temp.y - temp.r, temp.y + temp.r);
    star(s, c);
    c.font = "25px Caveat";
    c.fillText(tile.name, temp.x - temp.r, temp.y + 5);
}
const elem = document.querySelector('#gameCanvas');
const XMax = 1000;
const YMax = 500;
const XMod = XMax / 64;
const YMod = YMax / 64;
const c = getCanvas(elem);
const OffsetX = elem.offsetLeft;
const OffsetY = elem.offsetTop;
let mapTilePos = new Map();
let inTile = false;
fetch('/api/game').then(response => response.json()).then(json => {
    let data = json;
    console.log(data);
    let count = 0;
    for (let e of Object.values(data.world.edges)) {
        count++;
    }
    for (let e of Object.values(data.world.tiles)) {
        drawMapTile(e, count, c);
    }
    window.addEventListener('click', function (event) {
        if (!inTile) {
            x = parseInt(event.clientX - OffsetX);
            y = parseInt(event.clientY - OffsetY);
            console.log(x, y);
            for (let e of mapTilePos.keys()) {
                console.log(e.name);
                xMin = mapTilePos.get(e).x - mapTilePos.get(e).r;
                xMax = mapTilePos.get(e).x + mapTilePos.get(e).r;
                yMin = mapTilePos.get(e).y - mapTilePos.get(e).r;
                yMax = mapTilePos.get(e).y + mapTilePos.get(e).r;
                if ((x < xMax && x > xMin) && (y < yMax && y > yMin)) draw(data, e.name, c);
            }
        }
    })
    console.log(mapTilePos);
    //draw(data, c);
})

//TODO add map drawing function and onclick to select tiles.