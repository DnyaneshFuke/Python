import requests
import random
import prettytable
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk

url = "https://api.freeapi.app/api/v1/public/randomproducts"
response = requests.get(url)
data = response.json()

def show_images(image_urls):
    # Create a window
    root = tk.Tk()
    root.title("Product Images")

    # Create a frame to hold the images
    frame = tk.Frame(root)
    frame.pack()

    # Loop through each image URL and display it
    for image_url in image_urls:
        # Fetch and display the image
        response = requests.get(image_url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img_tk = ImageTk.PhotoImage(img)

        label = tk.Label(frame, image=img_tk)
        label.image = img_tk  # Keep a reference to avoid garbage collection
        label.pack()  # Add the image to the frame

    # Keep the window open
    root.mainloop()

def get_image_names(image_urls):
    # Extract only the image names from the URLs
    return [url.split('/')[-1] for url in image_urls]  # Get the last part of each URL

def Product_Get_Request():
    if data['success'] and 'data' in data:
        products = data['data']['data']
        if products:
            # Select 5 random products from the list
            selected_products = random.sample(products, min(5, len(products)))  # Get a random sample of 5 products (or less if not enough)

            # Create a PrettyTable to display product information
            table = prettytable.PrettyTable()
            table.field_names = ["Product Name", "Product Price", "Product Description", "Product Image Names"]
            
            # Loop through selected products and add them to the table
            for product in selected_products:
                image_names = get_image_names(product['images'])  # Get only the image names
                table.add_row([product['title'], product['price'], product['category'], ', '.join(image_names)])  # Join names for better display
                print(f"Showing images for: {product['title']}")  # Indicate which product's images are being shown
                show_images(product['images'])  # Show images for each product in separate window

            print(table)

def main():
    Product_Get_Request()

if __name__ == "__main__":
    main()
