function getCanvas() {
    const elem = document.querySelector('#gameCanvas');
    return elem.getContext('2d');
}

function drawObject(ctx, x, y, size) {
    ctx.beginPath();
    ctx.arc(x, y, size, 0, 2*Math.PI);
}
class Grid {
    constructor(x, y, height, width) {
        this.map = [];
        this.x = x;
        this.y = y;
        this.height = height;
        this.width = width;
        this.draw = function (c) {
            for (let i = 0; i < 50; i++) {
                for (let j = 0; j < 25; j++) {
                    c.beginPath();
                    c.strokeStyle = 'black';
                    c.rect(this.x * i, this.y * j, this.height, this.width);
                    c.stroke();
                }
            }
            this.createMap();
        };
        this.createMap = function () {
            this.map = new Array(50);
            for (let i = 0; i < 50; i++) {
                this.map[i] = new Array(25).fill(0);
            }
        };
    }
}
const ctx = getCanvas();
grid = new Grid(20, 20, 20, 20);
grid.draw(ctx);
drawObject(ctx, 30, 30, 10);
ctx.stroke();
