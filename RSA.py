import tkinter as tk
from tkinter import ttk
import random

# Function to encrypt a message
def encrypt(message, e, n):
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

# Function to decrypt a message
def decrypt(cipher, d, n):
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

# Function to encrypt the message for GUI callback
def encrypt_gui_message():
    message = message_entry.get()
    e = int(public_key_entry.get())
    n = int(modulus_entry.get())

    encrypted_message = encrypt(message, e, n)

    encrypted_text.delete(1.0, tk.END)
    encrypted_text.insert(tk.END, encrypted_message)

# Function to decrypt the message for GUI callback
def decrypt_gui_message():
    cipher = [int(char) for char in encrypted_text.get(1.0, tk.END).split() if char.isdigit()]
    d = int(private_key_entry.get())
    n = int(modulus_entry.get())

    decrypted_message = decrypt(cipher, d, n)

    decrypted_text.delete(1.0, tk.END)
    decrypted_text.insert(tk.END, decrypted_message)

# Create the main application window
root = tk.Tk()
root.title("RSA Encryption/Decryption")


# Set background color
root.config(bg='lightblue')

# Define colors
bg_color = 'lightblue'  
entry_bg_color = 'pink'  
button_bg_color = 'pink'  
button_fg_color = 'black'  

# Create and place widgets
frame = ttk.Frame(root, padding="10", style='My.TFrame')
frame.grid(row=0, column=0)

style = ttk.Style()
style.configure('My.TFrame', background=bg_color)

ttk.Label(frame, text="Message:", background=bg_color).grid(row=0, column=0, padx=5, pady=5)
message_entry = ttk.Entry(frame, style='EntryStyle.TEntry')
message_entry.grid(row=0, column=1, padx=5, pady=5)

public_key_label = ttk.Label(frame, text="Public Key (e):", background=bg_color)
public_key_label.grid(row=1, column=0, padx=5, pady=5)
public_key_entry = ttk.Entry(frame, style='EntryStyle.TEntry')
public_key_entry.grid(row=1, column=1, padx=5, pady=5)

private_key_label = ttk.Label(frame, text="Private Key (d):", background=bg_color)
private_key_label.grid(row=2, column=0, padx=5, pady=5)
private_key_entry = ttk.Entry(frame, style='EntryStyle.TEntry')
private_key_entry.grid(row=2, column=1, padx=5, pady=5)

modulus_label = ttk.Label(frame, text="Modulus (n):", background=bg_color)
modulus_label.grid(row=3, column=0, padx=5, pady=5)
modulus_entry = ttk.Entry(frame, style='EntryStyle.TEntry')
modulus_entry.grid(row=3, column=1, padx=5, pady=5)

encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt_gui_message, style='ButtonStyle.TButton')
encrypt_button.grid(row=4, column=0, padx=5, pady=5)

decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt_gui_message, style='ButtonStyle.TButton')
decrypt_button.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame, text="Encrypted Message:", background=bg_color).grid(row=5, column=0, padx=5, pady=5)
encrypted_text = tk.Text(frame, height=5, width=30)
encrypted_text.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(frame, text="Decrypted Message:", background=bg_color).grid(row=6, column=0, padx=5, pady=5)
decrypted_text = tk.Text(frame, height=5, width=30)
decrypted_text.grid(row=6, column=1, padx=5, pady=5)

# Configure widget styles
style.configure('EntryStyle.TEntry', background=entry_bg_color)
style.configure('ButtonStyle.TButton', background=button_bg_color, foreground=button_fg_color)

# Run the Tkinter event loop
root.mainloop()

