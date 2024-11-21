import tkinter as tk
import requests

# Function to translate Carti slang to modern English
def translate_to_english():
    # Get user input
    carti_text = entry.get()

    # Dictionary of Playboi Carti slang to modern English
    translation_dict = {
        "slatt": "slime love all the time",
        "yung": "young",
        "vvs": "Very Very Slightly (expensive diamonds)",
        "cash carti": "Playboi Carti's alter ego or self",
        "bih": "girl or woman",
        "flexin'": "showing off",
        "mood": "emotion or vibe",
        "lit": "exciting or fun",
        "drip": "style or clothing",
        "woke": "aware or enlightened",
        "ballin'": "living a luxurious life"
    }

    # Translate the text
    translated_text = []
    for word in carti_text.split():
        # Look up each word in the translation dictionary, if available
        translated_text.append(translation_dict.get(word.lower(), word))

    # Join the translated words and show in the result label
    result_text = " ".join(translated_text)
    result_label.config(text=result_text)

# Function to download the image
def download_image(url, save_path):
    try:
        # Send a GET request to the image URL
        response = requests.get(url)
        
        # Save the image content to a file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved to {save_path}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Create tkinter window
root = tk.Tk()
root.title("Playboi Carti to English Translator")
root.geometry("800x600")  # Set the window size

# Image URL for the background
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRR1qo2VBCIfe_KW2W8a4GCMnYA2otaClEWcD7E5gFys5KZaMb4F1elM3poMmqdGtMLJA&usqp=CAU"
image_path = "background_image.png"  # Local path to save the image

# Download and save the image
download_image(image_url, image_path)

# Load the background image using tkinter.PhotoImage (works with .png and .gif)
bg_image = tk.PhotoImage(file=image_path)

# Add the image to a label and place it in the window
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Make the image cover the window

# Create input field for Carti's phrase entry
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button that triggers translation
translate_button = tk.Button(root, text="Translate", command=translate_to_english)
translate_button.pack(pady=10)

# Label to show translated text
result_label = tk.Label(root, text="Your translated text will appear here.", wraplength=400, bg="white")
result_label.pack(pady=20)

# Run the application
root.mainloop()
   