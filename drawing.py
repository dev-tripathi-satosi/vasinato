from sketchpy import canvas 
logo = canvas.sketch_from_image("./static/img/favicon.jpg")
logo.draw(threshold=127)