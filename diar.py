# ChatGPT Coding Diary
# Project Name: [opium]
# Date: [11/17/24]
# 1. Task/Problem Description
# Briefly describe the problem you're trying to solve or the task you're working on.

# I  need to write a program that taakes words carti says Aand translates them to English

# 2. Initial Approach/Code
# Describe the initial approach you took to solving the problem. If you started writing code, include it here.

# def translate_to_english():
    # carti_text = entry.get()
    # translation_dict = {
    #     "slatt": "slime love all the time",
    #     "yung": "young",
    #     "vvs": "Very Very Slightly (expensive diamonds)",
    #     "cash carti": "Playboi Carti's alter ego or self",
    #     "bih": "girl or woman",
    #     "flexin'": "showing off",
    #     "mood": "emotion or vibe",
    #     "lit": "exciting or fun",
    #     "drip": "style or clothing",
    #     "woke": "aware or enlightened",
    #     "ballin'": "living a luxurious life"
# What was your plan for solving the problem?
#mAKE a dictionay 
# Did you have any initial thoughts or strategies before using ChatGPT?
#Make a dictionay and use tkinter to make backround
# 3. Interaction with ChatGPT
# Questions/Requests to ChatGPT

# Write down the questions or requests you made to ChatGPT. Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. For example:
# write a program that taakes words carti says Aand translates them to English
#Add backround
#Make backround without using pip
#how do i use pip
# 4. ChatGPT's Suggestions/Code Changes
# Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.
""" import tkinter as tk
import requests
pip install requests

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
    """
#This is wha it gave me everytime sometimes it just remove pip and their was no backround
# What was ChatGPT's solution or suggestion?
They had none it kept using pip
# How did it differ from your original approach?
Just worse backround than envissioned
# 5. Reflection on Changes
# Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:

# Why do you think ChatGPT's suggestions are helpful or relevant?
It carried my project
# Did the suggestions improve your code? How?
Not really cause backround didnt change
# Did you understand why the changes were made, or are you still uncertain about some parts?
Honestly its still confusing but i learned gitnore how to path a image and pip
# 6. Testing and Results
# After making the changes, did you test your code? What were the results?
Still no backround
# Did you run any tests (e.g., unit tests, edge cases)?
Yes
# Did the code work as expected after incorporating ChatGPT's changes?
Not all the time but the main translator function worked
# Did you encounter any bugs or issues during testing?
I dont want to install pip cause it seems sketchy.
# 7. What Did You Learn?
# In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with?
How to path an image and how to use gitnore and be more independent
