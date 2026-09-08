import numpy as np
import pickle
import matplotlib.pyplot as plt
from PIL import Image


class ImageProcessor:
    def __init__(self):
        # Initialize an empty image processor object
        # _image will hold the pixel array, _color_map for indexed colors, _is_rgb tracks RGB mode
        self._image, self._color_map, self._is_rgb = None, None, True

    def is_RGB_mode(self):
        # Returns True if the image is in RGB mode, None if no image is loaded
        return None if self._image is None else self._is_rgb

    def get_color_map(self):
        # Returns the color map dictionary (used for indexed images)
        return self._color_map

    def get_array(self):
        # Returns the underlying numpy array of the image
        return self._image

    def shape(self):
        # Returns the height and width of the image
        if self._image is None:
            raise ValueError("No image loaded")
        return self._image.shape[:2]

    def load(self, filepath):
        # Load an image file (.png) or a pickled color-mapped image (.pkl)
        if filepath.endswith(".png"):
            img = Image.open(filepath).convert("RGB")
            # Convert the image to a numpy array and set as RGB
            self._image, self._color_map, self._is_rgb = np.array(img), None, True
        elif filepath.endswith(".pkl"):
            # Load a pickled color-mapped image
            with open(filepath, "rb") as f:
                self._image, self._color_map = pickle.load(f)
            self._is_rgb = False
        else:
            raise ValueError("Unsupported file format")

    def save(self, filepath):
        # Save the image to file: PNG if RGB, pickle if indexed
        if self._image is None:
            raise ValueError("No image loaded")
        ext = ".png" if self._is_rgb else ".pkl"
        # Automatically add file extension if missing
        filepath += ext if not filepath.endswith(ext) else ""
        if self._is_rgb:
            Image.fromarray(self._image).save(filepath)
        else:
            # Save color-mapped image as pickle
            with open(filepath, "wb") as f:
                pickle.dump((self._image, self._color_map), f)

    def change_image_format(self, to_rgb, bins=2):
        # Converts between RGB and indexed image with color splitting
        if self._image is None:
            raise ValueError("No image loaded")
        if to_rgb and not self._is_rgb:
            # Convert indexed image back to RGB using the color map
            rgb = np.vectorize(self._color_map.get, signature="()->(n)")(self._image)
            self._image, self._color_map, self._is_rgb = (rgb * 255).astype(np.uint8), None, True
        elif not to_rgb and self._is_rgb:
            # Convert RGB to indexed image by splitting each color channel
            img = self._image
            step = 256 // bins
            r, g, b = (img[..., i] // step for i in range(3))
            cube = r * bins * bins + g * bins + b
            uniq = np.unique(cube)
            ids = np.searchsorted(uniq, cube)
            # Create a color map for the new indexed colors
            self._color_map = {
                i: img[cube == u].reshape(-1, 3).mean(axis=0) / 255
                for i, u in enumerate(uniq)
            }
            self._image, self._is_rgb = ids.astype(np.uint8), False

    def rotate_colors(self):
        # Rotates the RGB channels or shifts color map for indexed images
        if self._image is None:
            raise ValueError("No image loaded")
        if self._is_rgb:
            self._image = self._image[..., [1, 2, 0]]  # shift channels: R→G, G→B, B→R
        else:
            # Shift indexed color map
            n = len(self._color_map)
            self._color_map = {i: self._color_map[(i - 1) % n] for i in range(n)}

    def blur_RGB_images(self, size=3):
        # Apply a simple blur to RGB images using a mean filter
        if self._image is None:
            raise ValueError("No image loaded")
        size = max(3, size | 1)  # Ensure size is odd and at least 3
        r, out = size // 2, self._image.copy()
        for y in range(self._image.shape[0]):
            for x in range(self._image.shape[1]):
                # Calculate mean of the surrounding pixels
                out[y, x] = self._image[
                    max(0, y - r):y + r + 1,
                    max(0, x - r):x + r + 1
                ].mean(axis=(0, 1))
        self._image = out.astype(np.uint8)

    def pixelate_images(self, area, size=10):
        # Pixelate a rectangular area of the image
        if self._image is None:
            raise ValueError("No image loaded")
        (xmin, xmax), (ymin, ymax) = area
        for y in range(ymin, ymax, size):
            for x in range(xmin, xmax, size):
                block = self._image[y:y + size, x:x + size]
                # For RGB: use mean color; for indexed: most common index
                val = block.mean(axis=(0, 1)) if self._is_rgb else np.bincount(block.ravel()).argmax()
                block[:] = val

    def show(self, filename=None):
        # Display the image or save it if a filename is provided
        if self._image is None:
            raise ValueError("No image loaded")
        img = self._image if self._is_rgb else np.vectorize(
            self._color_map.get, signature="()->(n)")(self._image)
        plt.imshow(img, interpolation="none")
        plt.axis("off")
        plt.savefig(filename + ".png") if filename else plt.show()


if __name__ == "__main__":
    # Demo script for pixelating a pumpkin
    ip = ImageProcessor()
    ip.load("pumpkin.png")  # Load the pumpkin image
    ip.pixelate_images(((55, 250), (115, 310)), size=10)  # Pixelate a rectangle
    ip.save("pumpkin_masked")  # Save result
    ip.show()  # Show result
