import tkinter as tk
import mysql.connector as sql

# Connect to the database
cnx = sql.connect(user='root', password='', host='localhost', database='stock')
cursor = cnx.cursor()

# Function to add a new product
def add_product():
    product_name = entry_product_name.get()
    quantity = entry_quantity.get()

    add_product_query = "INSERT INTO product (product_name, quantity) VALUES (%s, %s)"
    data_product = (product_name, quantity)

    cursor.execute(add_product_query, data_product)
    cnx.commit()

    # Clear the input fields
    entry_product_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Function to update a product
def update_product():
    product_id = entry_product_id.get()
    product_name = entry_product_name.get()
    quantity = entry_quantity.get()

    update_product_query = "UPDATE product SET product_name=%s, quantity=%s WHERE product_id=%s"
    data_product = (product_name, quantity, product_id)

    cursor.execute(update_product_query, data_product)
    cnx.commit()

    # Clear the input fields
    entry_product_id.delete(0, tk.END)
    entry_product_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Function to delete a product
def delete_product():
    product_id = entry_product_id.get()

    delete_product_query = "DELETE FROM product WHERE product_id=%s"
    data_product = (product_id,)

    cursor.execute(delete_product_query, data_product)
    cnx.commit()

    # Clear the input field
    entry_product_id.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Product Management")

# Create input fields and labels
entry_product_id = tk.Entry(window)
entry_product_id.grid(row=0, column=1)
entry_product_name = tk.Entry(window)
entry_product_name.grid(row=1, column=1)
entry_quantity = tk.Entry(window)
entry_quantity.grid(row=2, column=1)

# Create labels for input fields
tk.Label(window, text="Product ID").grid(row=0, column=0)
tk.Label(window, text="Product Name").grid(row=1, column=0)
tk.Label(window, text="Quantity").grid(row=2, column=0)

# Create buttons
add_product_button = tk.Button(window, text="Add Product", command=add_product)
add_product_button.grid(row=3, column=0)
update_product_button = tk.Button(window, text="Update Product", command=update_product)
update_product_button.grid(row=3, column=1)
delete_product_button = tk.Button(window, text="Delete Product", command=delete_product)
delete_product_button.grid(row=3, column=2)

# Run the main loop
window.mainloop()

# Close the database connection
cursor.close()
cnx.close()