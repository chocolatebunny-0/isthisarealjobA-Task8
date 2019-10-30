try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def convert_image_to_test(filename):
    return pytesseract.image_to_string(Image.open(filename))


