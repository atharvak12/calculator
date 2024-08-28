import tkinter as tk
from tkinter import ttk

def calculate_percentage(operation):
    """Performs the percentage calculation based on the operation and current values."""
    global percentage_result
    try:
        num = float(entry.get())
        if operation == "6%":
            percentage_result = num * 0.06
            percentage = 6
        elif operation == "9%":
            percentage_result = num * 0.09
            percentage = 9
        elif operation == "12%":
            percentage_result = num * 0.12
            percentage = 12
        elif operation == "18%":
            percentage_result = num * 0.18
            percentage = 18
        else:
            percentage_result = None
            result_label.config(text="Error: Invalid operation")
            return

        result_label.config(text=f"Result: {percentage_result:.2f} ({percentage}%)")
    except ValueError:
        result_label.config(text="Error: Please enter a valid number")

def calculate_custom_percentage():
    """Calculates the result based on the custom percentage input."""
    global percentage_result
    try:
        num = float(entry.get())
        custom_percentage = float(custom_percentage_entry.get()) / 100.0
        percentage_result = num * custom_percentage
        result_label.config(text=f"Result: {percentage_result:.2f} ({custom_percentage * 100:.2f}%)")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers")

def add_to_input():
    """Adds the percentage result to the current input value and displays the result."""
    try:
        num = float(entry.get())
        if percentage_result is not None:
            final_result = num + percentage_result
            result_label.config(text=f"Final Result: {final_result:.2f}")
        else:
            result_label.config(text="Error: No percentage calculation performed yet")
    except ValueError:
        result_label.config(text="Error: Please enter a valid number")

def clear_fields():
    """Clears the entry fields and result label."""
    entry.delete(0, tk.END)
    result_label.config(text="")
    custom_percentage_entry.delete(0, tk.END)
    custom_percentage_entry.insert(0, "Enter custom %")
    global percentage_result
    percentage_result = None

def on_focus_in(event):
    """Clears placeholder text when the entry field gains focus."""
    if custom_percentage_entry.get() == "Enter custom %":
        custom_percentage_entry.delete(0, tk.END)
        custom_percentage_entry.config(fg='black')

def on_focus_out(event):
    """Restores placeholder text when the entry field loses focus and is empty."""
    if custom_percentage_entry.get() == "":
        custom_percentage_entry.insert(0, "Enter custom %")
        custom_percentage_entry.config(fg='grey')

def add_data():
    """Adds some example data to the table."""
    data = [
("Leaflets (Single Sheet)", "5%", "49011020"),
("Hardcase Books, Softcover Book", "5%", "49011010"),
("Brochures (Multiple Sheets)", "5%", "49019900"),
("Annual Report", "5%", "49011010"),
("Medical Booklet", "5%", "49011020"),
("Product Booklet", "5%", "49011020"),
("Xerox/Plain Paper", "12%", "48021010"),
("Frame / Fitting (Wood / Metal)", "12%", "90031900"),
("LED Module, Power Supply, LED Strips (Rigid or Flexible)", "12%", "94054090"),
("Envelope", "18%", "48171000"),
("Letterheads", "18%", "48173090"),
("Diary", "18%", "48201090"),
("Cartons", "18%", "48191010"),
("Boxes", "18%", "48191010"),
("Corrugated Paper or Paper Board", "18%", "48191010"),
("Carry Bag", "18%", "48192090"),
("Folders", "18%", "48203000"),
("Invoice, Books, Letter Pads, Diaries", "18%", "48201020"),
("Notepads", "18%", "48201090"),
("Stickers, Packing Material", "18%", "48211090"),
("CD / DVD Holder (Pouch/Folder/Inlay)", "18%", "48211020"),
("Plain/PS Lables", "18%", "48211020"),
("Tags", "18%", "48211010"),
("Inserts", "18%", "48211090"),
("Visiting Card", "18%", "49090090"),
("Wedding / Invitation Cards", "18%", "49090090"),
("Calendars", "18%", "49100010"),
("Poster", "18%", "49111010"),
("Artwork/Designs (Printed)", "18%", "49111090"),
("Hardcase & Softcase Catalogue (Commercial)", "18%", "49111020"),
("Inlay Cards", "18%", "49111030"),
("Other Printed Matter, Including Printed Pictures & Photographs; Such as Trade Advertising Material, Commercial Catalogs, Printed Inlay Cards, Pictures, Design & Photographs, Plan & Drawings for Architectural Engineering, Industrial, Commercial, Topographical or Similar Purpose Reproduced with the Aid of Computer or any Other Devices", "18%", "49111010"),
("Digital Output", "18%", "49119990"),
("Examination Card", "18%", "49090090"),
("Bill/Tax Invoice/Cash Memo", "18%", "48209090"),
("Delivery Challan Book", "18%", "48209090"),
("Approval / Estimate / Quotation", "18%", "48209090"),
("Continuous Stationery", "18%", "48209090"),
("Binding Charges", "18%", "48209090"),
("School Calendar / Answer Sheet", "18%", "48209090"),
("I Card", "18%", "48172000"),
("Offset Printing Labour", "18%", "84431300"),
("Screen Printing Labour", "18%", "84431990"),
("Jute Bag / Cloth Bag / Paper Bag", "18%", "63051040"),
("Office Stationery", "18%", "48201010"),
("All Types of Paper Printing", "18%", "48211090"),
("Goods Received Note", "18%", "48202000"),
("Store Voucher", "18%", "48209090"),
("Coupon / Tickets", "18%", "48211090"),
("Acrylic Polymers in Primary Form", "18%", "39069090"),
("Acrylic Plastic Sheet & Cut", "18%", "39201011"),
("Plastic Aluminium Compsite Panel / Sheet", "18%", "39201019"),
("PVC Sheet", "18%", "39201099"),
("PVC Laminated Flex Rolls / Sheets", "18%", "39204900"),
("P.S. Sheets", "18%", "39205111"),
("Acrylic Sheets Off Cuts", "18%", "39205111"),
("Acrylic Polymers (Methacrylate) Sheets, Others", "18%", "39205159"),
("Plastic Sheets (Monarch)", "18%", "39205911"),
("Polycarbonate Sheet Compact", "18%", "39206190"),
("PVC Sheeting in Rolls", "18%", "39209900"),
("Translite, Inkjet PP Matt", "18%", "39209999"),
("PVC Flex Material", "18%", "39219026"),
("PVC Sheet", "18%", "39219029"),
("Ink Jet", "18%", "39219091"),
("Acrylic Sheets", "18%", "39219099"),
("Acrylic Sign Board", "18%", "39269099"),
("Plastic Photo ID Card", "18%", "39264049"),
("Danglers, Tent Card", "18%", "49111010"),
("Sunboard Plain or Printed", "18%", "49111020"),
("Foam Banners, Flex Banners, Promo Table", "18%", "49111090"),
("Promotional Items Like T-Shirts, Caps, Mugs, Pen Drives", "18%", "49111090"),
("Poly Cotton Canvas (Matt Glossy)", "18%", "59011020"),
("Acrylic Sandwich Spacer Studs", "18%", ""),
("Roll Up Stands", "18%", "76109030"),
("Roll Up Standys", "18%", "76169990"),
("ACP Signage with Channel Letter, 3D Letter, Glow Sign Boxes, Clipon Frames, Frames Boxes, Toempoles, Lollypops, Channel Letters, All Signages that Lit, LED Display Items", "18%", "94059900"),
("Scaffoldings (Services)", "18%", ""),
("Non- Illuminated Signages, Sign Plates, Name Plates, Address Plates and Similar Plates, Numbers, Letters of base Metal, Excluding there if the heading 9405., Metal Fabrication, Solid Acrylic Letters Metal Letters, Way Finding Signages, Directories, All non Lit Signages Made from Wood Metal or Plastics, Sign Board/Exit Board/Indication/Board/Display Board Non Lite/ Name Plate", "18%", "83100090"),
("All Wooden or Metal Fixture or Retail Display, Promo Table made of Plastic or Aluminium", "18%", ""),
("Installation – Maintenance, Repair & Installation (Except Construction) Services, Installation for Signage’s", "18%", ""),
("Machining, Cutting Jobs Works, Job Work on Material Supplied by Client, Manufacturing Services on Physical Inputs (Goods) Owned by Others.", "18%", ""),
("Paper and Paper Product Manufacturing Services", "18%", ""),
("Information Technology (IT) Consulting and Support Services", "18%", ""),
("Web Design & Development", "18%", ""),
("Digital Marketing", "18%", ""),
("Social Media Marketing", "18%", ""),
("Specialty Design Services including Interior Design, Fashion Design, Industrial Design & other Specialty Design Services", "18%", ""),
("Hosting Services", "18%", ""),
("Domain Name Registration/Renewal Services", "18%", ""),
("Add on services such as Site Lock, Privacy Protection Services, Digital Certificate, Bulk Email Plan", "18%", ""),
("Software Development", "18%", ""),

    ]
    for item in data:
        tree.insert("", tk.END, values=item)

def click_button(value):
    """Handles button clicks for the basic calculator."""
    current = calc_entry.get()
    if value == "=":
        try:
            result = eval(current)
            calc_entry.delete(0, tk.END)
            calc_entry.insert(0, str(result))
        except Exception as e:
            calc_entry.delete(0, tk.END)
            calc_entry.insert(0, "Error")
    elif value == "C":
        calc_entry.delete(0, tk.END)
    else:
        calc_entry.insert(tk.END, value)

def handle_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        click_button(key)
    elif key == '\r':  # Enter key
        click_button("=")
    elif key == '\x08':  # Backspace key
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    elif key == 'c' or key == 'C':
        click_button("C")

# Create the main window
window = tk.Tk()
window.title("Atharva Kabra")
window.geometry("1000x600")  # Adjust size as needed

# Create main frame for calculator and basic calculator
main_frame = tk.Frame(window, padx=10, pady=10)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create entry field for number
entry = tk.Entry(main_frame, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Create entry field for custom percentage with placeholder
custom_percentage_entry = tk.Entry(main_frame, font=("Arial", 14), fg='grey')
custom_percentage_entry.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
custom_percentage_entry.insert(0, "Enter custom %")

# Bind events to handle placeholder text
custom_percentage_entry.bind("<FocusIn>", on_focus_in)
custom_percentage_entry.bind("<FocusOut>", on_focus_out)

# Create buttons for percentage calculations
buttons = {
    "6%": lambda: calculate_percentage("6%"),
    "9%": lambda: calculate_percentage("9%"),
    "12%": lambda: calculate_percentage("12%"),
    "18%": lambda: calculate_percentage("18%"),
    "Custom %": calculate_custom_percentage,
    "Add to Input": add_to_input,
    "C": clear_fields
}

# Create button grid for percentage calculations
button_grid = tk.Frame(main_frame)
button_grid.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

for i, (symbol, command) in enumerate(buttons.items()):
    button = tk.Button(button_grid, text=symbol, command=command, font=("Arial", 12), width=15)
    button.grid(row=i // 2, column=i % 2, pady=5)

# Create the result label
result_label = tk.Label(main_frame, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

# Create a frame for the basic calculator
calc_frame = tk.Frame(main_frame, padx=10, pady=10)
calc_frame.grid(row=4, column=0, columnspan=2, pady=10)

# Create entry field for basic calculator
calc_entry = tk.Entry(calc_frame, font=("Arial", 18), width=20, borderwidth=2, relief="solid")
calc_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Create buttons for basic calculator
calc_buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(calc_buttons):
    for c, char in enumerate(row):
        button = tk.Button(calc_frame, text=char, font=("Arial", 14), width=5, height=2,
                           command=lambda v=char: click_button(v))
        button.grid(row=r + 1, column=c, padx=5, pady=5)

# Create a frame for the table
table_frame = tk.Frame(window, padx=10, pady=10)
table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create the Treeview widget
tree = ttk.Treeview(table_frame, columns=("Product Name", "GST %", "HSN Code"), show="headings")

# Define the columns and their headings
tree.heading("Product Name", text="Product Name")
tree.heading("GST %", text="GST %")
tree.heading("HSN Code", text="HSN Code")

# Define the column widths
tree.column("Product Name", width=250)
tree.column("GST %", width=100)
tree.column("HSN Code", width=150)

# Add a vertical scrollbar
vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')

# Configure the Treeview to use the scrollbar
tree.configure(yscrollcommand=vsb.set)

# Add the Treeview to the frame
tree.pack(fill=tk.BOTH, expand=True)

# Add some example data
add_data()

# Initialize global variable for storing the percentage result
percentage_result = None
# Bind keyboard events
window.bind('<Key>', handle_key)
# Start the main loop
window.mainloop()