from PIL import Image
import numpy as np
import os

class ImageEncryptor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.encrypted_image = None

    def load_image(self):
        """Load the image from the specified path."""
        try:
            if not os.path.isfile(self.image_path):
                raise FileNotFoundError
            self.image = Image.open(self.image_path)
            print("Image loaded successfully.")
        except FileNotFoundError:
            print("Error: The specified image file was not found.")
        except Exception as e:
            print(f"An error occurred while loading the image: {e}")

    def encrypt(self):
        """Encrypt the image by manipulating pixel values."""
        if self.image is None:
            print("Error: No image loaded. Please load an image first.")
            return
        
        try:
            img_array = np.array(self.image)
            # Simple encryption by swapping pixel values
            if img_array.shape[0] > 1:  # Ensure there are at least 2 rows to swap
                img_array[0], img_array[1] = img_array[1], img_array[0]  # Swap first two rows
            self.encrypted_image = Image.fromarray(img_array)
            print("Image encrypted successfully.")
        except Exception as e:
            print(f"An error occurred during encryption: {e}")

    def decrypt(self):
        """Decrypt the image by reversing the encryption operation."""
        if self.encrypted_image is None:
            print("Error: No encrypted image available. Please encrypt an image first.")
            return
        
        try:
            encrypted_array = np.array(self.encrypted_image)
            if encrypted_array.shape[0] > 1:  # Ensure there are at least 2 rows to swap back
                encrypted_array[0], encrypted_array[1] = encrypted_array[1], encrypted_array[0]  # Swap back
            decrypted_image = Image.fromarray(encrypted_array)
            decrypted_image.show()  # Display the decrypted image
            print("Image decrypted successfully.")
        except Exception as e:
            print(f"An error occurred during decryption: {e}")

    def save_image(self, output_path):
        """Save the encrypted image to the specified output path."""
        if self.encrypted_image is None:
            print("Error: No encrypted image available to save.")
            return
        
        # Ensure the output path has a valid image extension
        valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
        if not any(output_path.lower().endswith(ext) for ext in valid_extensions):
            print("Error: The output path must have a valid image file extension (e.g., .png, .jpg).")
            return
        
        try:
            self.encrypted_image.save(output_path)
            print(f"Encrypted image saved successfully at {output_path}.")
        except Exception as e:
            print(f"An error occurred while saving the image: {e}")

# Example usage
if __name__ == "__main__":
    image_path = input("Enter the path of the image to encrypt: ")
    encryptor = ImageEncryptor(image_path)
    
    encryptor.load_image()
    encryptor.encrypt()
    
    output_path = input("Enter the output path for the encrypted image (with extension): ")
    encryptor.save_image(output_path)
    
    decrypt_choice = input("Would you like to decrypt the image? (y/n): ").strip().lower()
    if decrypt_choice == 'y':
        encryptor.decrypt()

