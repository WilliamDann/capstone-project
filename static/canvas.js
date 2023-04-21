function getCanvas() {
    const elem = document.querySelector('#gameCanvas');
    return elem.getContext('2d');
}

function drawObject(ctx, x, y, size) {
    ctx.arc(x, y, size, 0, 2*Math.PI);
}

const ctx = getCanvas();
drawObject(ctx, 30, 30, 10);
ctx.stroke();
