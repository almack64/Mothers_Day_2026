import os

# Define the path to your image folder
folder_path = 'cards'

# Get all files in the directory
try:
    files = os.listdir(folder_path)
except FileNotFoundError:
    print(f"Error: The folder '{folder_path}' was not found. Make sure your images are in a folder named 'cards'.")
    exit()

# Filter for JPEG images and sort them alphabetically
# This ensures (01) comes before (02), etc.
images = sorted([f for f in files if f.lower().endswith(('.jpg', '.jpeg'))])

if not images:
    print("No JPEG images found in the 'cards' folder.")
else:
    print("\n--- COPY AND PASTE THIS BLOCK INTO YOUR HTML --- \n")
    for img in images:
        # Create the HTML string for each slide
        html_string = f'            <div class="swiper-slide"><img src="cards/{img}" alt="Mother\'s Day Card"></div>'
        print(html_string)
    print("\n------------------------------------------------ \n")