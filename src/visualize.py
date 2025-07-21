from PIL import ImageDraw

def visualize_boxes(image, boxes, color="red"):
    draw = ImageDraw.Draw(image)
    for box in boxes:
        draw.rectangle(box, outline=color, width=2)
    return image
