import tkinter as tk

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
        "gyat": "fatti",
        "fweh": "popular carti adlib",
        "CUTTI": "nickname of playboi Carti",
        "(￣(工)￣)": "freaky play boi carti",
        "＞﹏＜": "sad play boi carti",
        "(～￣▽￣)～": "happy play boi carti",
        "╰（‵□′）╯": "mad play boi carti",
        "(ˉ﹃ˉ)": "dumb play boi carti",
        "(•_•)": "scary play boi carti",
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

# Create tkinter window
root = tk.Tk()
root.title("Playboi Carti to English Translator")
root.geometry("800x600")  # Set the window size

# Set the background color of the window to black
root.configure(bg='maroon')

# Create input field for Carti's phrase entry with black background and white text
entry = tk.Entry(root, width=50, bg="red", fg="white")
entry.pack(pady=10)

# Create a button that triggers translation with black background and white text
translate_button = tk.Button(root, text="Translate", command=translate_to_english, bg="black", fg="white")
translate_button.pack(pady=10)

# Label to show translated text with black background and white text
result_label = tk.Label(root, text="Your translated text will appear here.", wraplength=400, bg="black", fg="white")
result_label.pack(pady=20)

# Run the application
root.mainloop()
