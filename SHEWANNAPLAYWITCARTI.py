import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import the PIL (Pillow) library

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

# Create tkinter window (Only one Tk instance needed)
root = tk.Tk()
root.title("Playboi Carti to English Translator")
root.geometry("800x600")  # Set the window size

# Set up the image background
try:
    img_path = r"C:\Users\Andrew.Owotomo24\Downloads\your_image.jpg"  # Ensure it's an actual image file
    img = Image.open(img_path)
    
    # Convert the image to a Tkinter-compatible format
    bg_image = ImageTk.PhotoImage(img)

    # Add the image to a label and place it in the window
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Make the image cover the window
    
except Exception as e:
    print(f"Error loading image: {e}")

# Create input field for Carti's phrase
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
