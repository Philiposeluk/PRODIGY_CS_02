# Image Encryption Tool

Image Encryption Tool is a simple Python application that allows you to load, encrypt, and decrypt images using basic pixel manipulation techniques. The encryption is performed by swapping the first two rows of the image, making it an easy-to-understand example of image processing.

## Features

- Load images from local storage.
- Encrypt images by manipulating pixel values.
- Decrypt images to retrieve the original data.
- Save encrypted images to your desired location.

## Requirements

- Python 3.x
- Pillow library (`PIL`)
- NumPy library

You can install the required libraries using pip:

    pip install Pillow numpy
## Usage

 1. ### Clone the repository:
   
        git clone https://github.com/yourusername/ImageEncryptor.git

        cd image_encryption_tool
 2. ### Run the script:
 
        python image_encryptor.py
  
  3. ### Follow the prompts:

       - Enter the path of the image you want to encrypt.

      - Specify the output path for the encrypted image (ensure it has a valid image file extension).
  
     - Optionally, choose to decrypt the image after encryption.
    
   
  > Example

           Enter the path of the image to encrypt: path/to/your/image.jpg
           Image loaded successfully.
           Image encrypted successfully.
           Enter the output path for the encrypted image (with extension): path/to/output/encrypted_image.png
           Encrypted image saved successfully at path/to/output/encrypted_image.png.
           Would you like to decrypt the image? (y/n): y
           Image decrypted successfully.

## Limitations 

  - The encryption method used is very basic and should not be considered secure for sensitive data.

  - The application only manipulates the first two rows of the image for encryption and decryption.

     



    
