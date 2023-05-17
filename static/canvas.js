// seeded random allows things to be random but the same for every tile
// https://stackoverflow.com/questions/424292/seedable-javascript-random-number-generator
function RNG(seed) {
    // LCG using GCC's constants
    this.m = 0x80000000; // 2**31;
    this.a = 1103515245;
    this.c = 12345;

    this.state = seed ? seed : Math.floor(Math.random() * (this.m - 1));
}
RNG.prototype.nextInt = function() {
  this.state = (this.a * this.state + this.c) % this.m;
  return this.state;
}

function getCanvas() {
    const elem = document.querySelector('#gameCanvas');
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
function drawTile(data, tile, c) {
    //obj = Object.values(data.world.objects).filter(x => x.position.tileName == tileName);
    canvasState = 'tile';
    c.clearRect(0, 0, 9999, 9999);
    c.stroke();

    c.fillStyle = 'black';
    c.fillRect(0, 0, 1000, 500, c);
    let stars = Math.random() * 1000;
    let s = makeStars(stars, 0, XMax, 0, YMax);
    star(s, c);
    console.log('yay');
    console.log(tile);
    for (var obj of Object.values(data.world.objects)) {
        const objType = obj.objType._value_[0]; // extract ship type from python enum structure

        if (objType == "Ship" && obj.position.tile == tile) {
            ship(obj, c);
        }
        if (objType == "Station" && obj.position.tile == tile) {
            station(obj, c);
        }
        if (objType == "Asteroid" && obj.position.tile == tile) {
            asteroid(obj, c);
        }
    }
}

function drawMapTileConnection(x, y, toX, toY)
{
    let c =  getCanvas();

    c.beginPath();
    c.moveTo(x, y);
    c.lineTo(toX, toY);
    c.stroke();
}

function drawMapTile(x, y, radius, name) {
    let c = getCanvas();

    c.beginPath();
    c.arc(x, y, radius, 0, Math.PI * 2);
    c.fillStyle = 'black';
    c.fill();

    let s = makeStars(25, x - radius, x + radius, y - radius, y + radius);

    star(s, c);
    c.font = "15px Caveat";
    c.fillText(name, x - radius, y + 5);
}

function drawMapGraph(radius, edges) {
    const set = {};
    const c   = getCanvas();
    c.clearRect(0, 0, 9999, 9999);

    // add tile to the set
    let union = (tile) => 
    {
        let angle       = Math.random()*Math.PI*2;
        let tileRadius  = (Math.random() * radius) + (radius / 3);
        let x           = (Math.cos(angle)*tileRadius) + (radius * 2);
        let y           = (Math.sin(angle)*tileRadius) + (radius * 2);

        let drawnTileRadius = 20;
        drawMapTile(x, y, drawnTileRadius, tile)
        set[tile] = {name: tile, x: x, y: y, r: drawnTileRadius}
        mapTilePos.set(tile, set[tile]); // update click map
    }

    for (let tile in edges)
    {
        if (!set[tile])
            union(tile);

        for (let edge of edges[tile])
        {
            if (set[edge])
            {
                drawMapTileConnection(set[tile].x, set[tile].y, set[edge].x, set[edge].y);
                // TODO pull tiles closer togther
                continue;
            }

            union(edge)
        }
    }
}

let canvasState = 'map'; // 'map', 'tile'
let currentTile    = null;

const elem = document.querySelector('#gameCanvas');
const XMax = 1000;
const YMax = 500;
const XMod = XMax / 64;
const YMod = YMax / 64;
const c = getCanvas();
const OffsetX = elem.offsetLeft;
const OffsetY = elem.offsetTop;
let mapTilePos = new Map();

// Update game data every second
// TODO use Websockets to allow realtime communication
setInterval(() => {
    fetch('/api/game').then(response => response.json()).then(json => {
        console.log('refresh');
        let data = json;

        if (canvasState == 'map')
            drawMapGraph(200, data.world.edges)
        else
            drawTile(data, currentTile, c);

        window.addEventListener('click', function (event) {
            if (canvasState == 'map') {
                x = parseInt(event.clientX - OffsetX);
                y = parseInt(event.clientY - OffsetY);
                console.log(x, y);
                for (let e of mapTilePos.keys()) {
                    console.log(mapTilePos.get(e).name);
                    xMin = mapTilePos.get(e).x - mapTilePos.get(e).r;
                    xMax = mapTilePos.get(e).x + mapTilePos.get(e).r;
                    yMin = mapTilePos.get(e).y - mapTilePos.get(e).r;
                    yMax = mapTilePos.get(e).y + mapTilePos.get(e).r;
                    if ((x < xMax && x > xMin) && (y < yMax && y > yMin))
                    {
                        console.log(`drawing tile ${mapTilePos.get(e).name}`);
                        currentTile = mapTilePos.get(e).name;
                        canvasState = 'tile';
                        drawTile(data, mapTilePos.get(e).name, c);
                    }
                }
            }
        })
    })
}, 1000)


//TODO add map drawing function and onclick to select tiles.