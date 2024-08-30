from PIL import Image, ImageDraw, ImageFont

# Set parameters
text = "Teguh"
binary_representation = ' '.join(format(ord(c), '08b') for c in text)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust font path as needed
font_size = 24

# Create image
width, height = 400, 150
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Load font
font = ImageFont.truetype(font_path, font_size)

# Draw text
text_position = (10, 10)
draw.text(text_position, text, font=font, fill=(0, 0, 0))

# Draw binary representation
binary_position = (10, 50)
draw.text(binary_position, binary_representation, font=font, fill=(0, 0, 0))

# Save image
image.save('/data/data/com.termux/files/home/logo_teguh.png')
