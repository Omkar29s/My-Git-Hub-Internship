import cv2

def pencil_sketch(image_path):
    # Read the input image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray = 255 - gray_image

    # Apply Gaussian Blur to the inverted image
    blurred_inverted_gray = cv2.GaussianBlur(inverted_gray, (21, 21), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inverted_blurred = 255 - blurred_inverted_gray

    # Blend the grayscale image with the inverted blurred image using the "Color Dodge" blend mode
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    return pencil_sketch

if __name__ == "__main__":
    input_image_path = "C:/Users/omkar/OneDrive/Desktop/omkar.jpg"
    output_sketch_path = "C:/Users/omkar/OneDrive/Desktop/mysk.jpg"

    pencil_sketch_image = pencil_sketch(input_image_path)

    # Save the sketch image
    cv2.imwrite(output_sketch_path, pencil_sketch_image)

    # Display the original and sketch images side by side
    original_image = cv2.imread(input_image_path)
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Pencil Sketch", pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
