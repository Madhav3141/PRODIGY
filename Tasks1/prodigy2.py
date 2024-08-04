# Pixel Manipulation for Image Encryption

# Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.


from PIL import Image
import numpy as np
import os

while True:
    choice = input("Type 'encrypt' to encrypt an image, 'decrypt' to decrypt an image, or 'exit' to quit: ").lower()

    if choice == 'exit':
        print("Exiting the program.")
        break

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please choose 'encrypt', 'decrypt', or 'exit'.")
        continue

    image_path = input("Enter the path to the image: ").strip()
    key = input("Enter the encryption/decryption key (an integer or string): ")  
    output_path = input("Enter the path to save the output image: ").strip()

    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        continue

    try:
        image = Image.open(image_path)
        image_array = np.array(image)

        seed = abs(hash(str(key))) % (2**32 - 1)

        if choice == 'encrypt':

            np.random.seed(seed)
            flat_shape = image_array.shape[0] * image_array.shape[1], image_array.shape[2]
            flat_image = image_array.reshape(flat_shape)
            np.random.shuffle(flat_image)
            shuffled_array = flat_image.reshape(image_array.shape)

            encrypted_image = Image.fromarray(shuffled_array.astype('uint8'))
            encrypted_image.save(output_path)
            print(f"Encrypted image saved to {output_path}")

        elif choice == 'decrypt':

            np.random.seed(seed)
            flat_shape = image_array.shape[0] * image_array.shape[1], image_array.shape[2]
            flat_image = image_array.reshape(flat_shape)


            indices = np.arange(flat_image.shape[0])
            np.random.shuffle(indices)
            inverse_indices = np.argsort(indices)


            original_flat_image = flat_image[inverse_indices]
            original_image_array = original_flat_image.reshape(image_array.shape)


            decrypted_image = Image.fromarray(original_image_array.astype('uint8'))
            decrypted_image.save(output_path)
            print(f"Decrypted image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
