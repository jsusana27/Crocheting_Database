import tkinter as tk
import psycopg2
import messagebox
from datetime import datetime

global title_font
title_font = ("Helvetica", 20)

global button_font
button_font = ("Helvetica", 12)

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def start_up():
    clear_window(root)
    intro_text = tk.Label(root, text="What do you want to do?", font=title_font, bg = 'powderblue')
    intro_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    look_at_data_button = tk.Button(root, text="Look at data", font=button_font, command=look_at_data_options, width=20, height=2)
    look_at_data_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    add_data_button = tk.Button(root, text="Add data", font=button_font, command=add_data_options, width=20, height=2)
    add_data_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    modify_data_button = tk.Button(root, text="Modify data", font=button_font, command=modify_data_options, width=20, height=2)
    modify_data_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    delete_data_button = tk.Button(root, text="Delete data", font=button_font, command=delete_data_options, width=20, height=2)
    delete_data_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

def look_at_data_options():
    global what_i_can_make_materials
    what_i_can_make_materials = []

    clear_window(root)
    look_at_data_text = tk.Label(root, text="What data do you want to look at?", font=title_font, bg = 'powderblue')
    look_at_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    yarn_button = tk.Button(root, text="Yarn", command=yarn_options, font=button_font, width=35, height=2)
    yarn_button.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    safety_eyes_button = tk.Button(root, text="Safety Eyes", command=safety_eyes_options, font=button_font, width=35, height=2)
    safety_eyes_button.place(relx=0.5, rely=0.19, anchor=tk.CENTER)

    stuffing_button = tk.Button(root, text="Stuffing", command=stuffing_options, font=button_font, width=35, height=2)
    stuffing_button.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

    products_button = tk.Button(root, text="Products", command=products_options, font=button_font, width=35, height=2)
    products_button.place(relx=0.5, rely=0.33, anchor=tk.CENTER)

    customers_button = tk.Button(root, text="Materials Needed to Make a Product", command=materials_needed_name,
                                 font=button_font, width=35, height=2)
    customers_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    customers_button = tk.Button(root, text="With the Materials I Have, What Can I Make?",
                                 command=what_i_can_make_material_type, font=button_font, width=35, height=2)
    customers_button.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

    customers_button = tk.Button(root, text="All Customers", command=all_customer_information,
                                 font=button_font, width=35, height=2)
    customers_button.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

    customers_button = tk.Button(root, text="All General Order Information", command=all_general_order_info,
                                 font=button_font, width=35, height=2)
    customers_button.place(relx=0.5, rely=0.61, anchor=tk.CENTER)

    customers_button = tk.Button(root, text="Customer All Purchased Products", command=customer_purchased_name,
                                 font=button_font, width=35, height=2)
    customers_button.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

    customers_button = tk.Button(root, text="Sale Stats for a Product", command=product_stats_name,
                                 font=button_font, width=35, height=2)
    customers_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def yarn_options():
    clear_window(root)
    yarn_text = tk.Label(root, text="What data from Yarn do you want to see?", font=title_font, bg = 'powderblue')
    yarn_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    yarn_brands_button = tk.Button(root, text="Brands", command=yarn_brands, font=button_font, width=20, height=2)
    yarn_brands_button.place(relx=0.5, rely=0.14, anchor=tk.CENTER)

    yarn_colors_button = tk.Button(root, text="Colors", command=yarn_colors, font=button_font, width=20, height=2)
    yarn_colors_button.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

    fiber_types_button = tk.Button(root, text="Fiber Types", command=fiber_types, font=button_font, width=20, height=2)
    fiber_types_button.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

    fiber_weights_button = tk.Button(root, text="Fiber Weights", command=fiber_weights, font=button_font, width=20, height=2)
    fiber_weights_button.place(relx=0.5, rely=0.41, anchor=tk.CENTER)

    yarn_by_prices_button = tk.Button(root, text="Yarn by Prices",command=yarn_by_prices, font=button_font, width=20, height=2)
    yarn_by_prices_button.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

    yarn_by_yardage_button = tk.Button(root, text="Yarn by Yardage/Skein",command=yarn_by_yardage, font=button_font, width=20, height=2)
    yarn_by_yardage_button.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

    yarn_by_grams_button = tk.Button(root, text="Yarn by Grams/Skein",command=yarn_by_grams, font=button_font, width=20, height=2)
    yarn_by_grams_button.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

    yarn_by_num_in_stock_button = tk.Button(root, text="Yarn by Number in Stock",command=yarn_by_num_in_stock, font=button_font, width=20, height=2)
    yarn_by_num_in_stock_button.place(relx=0.5, rely=0.77, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def yarn_brands():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT brand FROM Yarn ORDER BY brand")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Brand"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0], bg='powderblue')
        brand_label.grid(row=idx, column=0, padx=5, pady=5, sticky='nsew')

    # Update the canvas scrollregion and position
    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion

    # Ensure the view starts at the top
    canvas.yview_moveto(0)  # Move the canvas view to the top

    # Add a back button
    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def yarn_colors():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT color FROM Yarn ORDER BY color")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Color"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    # Update the canvas scrollregion and position
    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion

    # Ensure the view starts at the top
    canvas.yview_moveto(0)  # Move the canvas view to the top

    # Add a back button
    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def fiber_types():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT fibertype FROM Yarn ORDER BY fibertype")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Fiber Type"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        data_label = tk.Label(frame, text=row[0], bg='powderblue')
        data_label.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

    # Update the canvas scrollregion and position
    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion

    # Ensure the view starts at the top
    canvas.yview_moveto(0)  # Move the canvas view to the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def fiber_weights():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT fiberweight FROM Yarn ORDER BY fiberweight")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Fiber Weight"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0], bg='powderblue')
        brand_label.grid(row=idx, column=0, padx=5, pady=5)

    # Update the canvas scrollregion and position
    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion

    # Ensure the view starts at the top
    canvas.yview_moveto(0)  # Move the canvas view to the top

    # Add a back button
    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def yarn_by_prices():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, yardageperskein, gramsperskein, numberofskeinsowned, "
                "price FROM Yarn ORDER BY price DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Yardage/Skein", "Grams/Skein",
               "Number of Skeins in Stock", "Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    # Update the canvas scrollregion and position
    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion

    # Ensure the view starts at the top
    canvas.yview_moveto(0)  # Move the canvas view to the top

    # Add a back button
    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def yarn_by_yardage():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, gramsperskein, numberofskeinsowned, "
                "price, yardageperskein FROM Yarn ORDER BY yardageperskein DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Grams/Skein", "Number of Skeins in Stock", "Price", "Yardage/Skein"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    # Update the canvas scrollregion and position
    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion

    # Ensure the view starts at the top
    canvas.yview_moveto(0)  # Move the canvas view to the top

    # Add a back button
    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def yarn_by_grams():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, yardageperskein, numberofskeinsowned, "
                "price, gramsperskein FROM Yarn ORDER BY gramsperskein DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Yardage/Skein", "Number of Skeins in Stock", "Price",
               "Grams/Skein"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def yarn_by_num_in_stock():
    def clear_window(window):
        for widget in window.winfo_children():
            widget.destroy()

    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, yardageperskein, gramsperskein, "
                "price, numberofskeinsowned FROM Yarn ORDER BY numberofskeinsowned DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, 0), window=frame, anchor="n")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Yardage/Skein", "Grams/Skein", "Price",
               "Number of Skeins in Stock"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def safety_eyes_options():
    clear_window(root)
    safety_eyes_text = tk.Label(root, text="What data from Safety Eyes do you want to see?", font=title_font, bg='powderblue')
    safety_eyes_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    size_in_mm_button = tk.Button(root, text="Size in Millimeters", command=size_in_mm, font=button_font, width=20, height=2)
    size_in_mm_button.place(relx=0.5, rely=0.14, anchor=tk.CENTER)

    eye_colors_button = tk.Button(root, text="Colors", command=eye_colors, font=button_font, width=20, height=2)
    eye_colors_button.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

    shapes_button = tk.Button(root, text="Shapes", command=shapes, font=button_font, width=20, height=2)
    shapes_button.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

    eyes_by_price_button = tk.Button(root, text="Eyes by Price", command=eyes_by_price, font=button_font, width=20, height=2)
    eyes_by_price_button.place(relx=0.5, rely=0.41, anchor=tk.CENTER)

    eyes_by_num_in_stock_button = tk.Button(root, text="Eyes by Number in Stock", command=eyes_by_num_in_stock, font=button_font, width=20, height=2)
    eyes_by_num_in_stock_button.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def size_in_mm():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT sizeinmm FROM safetyeyes ORDER BY sizeinmm")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Size in mm"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        size_label = tk.Label(frame, text=row[0], bg='powderblue')
        size_label.grid(row=idx, column=0, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def eye_colors():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT color FROM safetyeyes ORDER BY color")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Color"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        color_label = tk.Label(frame, text=row[0], bg='powderblue')
        color_label.grid(row=idx, column=0, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def shapes():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT shape FROM safetyeyes ORDER BY shape")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Shape"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        shape_label = tk.Label(frame, text=row[0], bg='powderblue')
        shape_label.grid(row=idx, column=0, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def eyes_by_price():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT sizeinmm, color, shape, numberofeyesowned, price FROM safetyeyes "
                "ORDER BY price DESC, sizeinmm")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Size in mm", "Color", "Shape", "Number Eyes in Stock", "Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def eyes_by_num_in_stock():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT sizeinmm, color, shape, price, numberofeyesowned FROM safetyeyes "
                "ORDER BY numberofeyesowned DESC, sizeinmm DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Size in mm", "Color", "Shape", "Price", "Number of Eyes in Stock"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def stuffing_options():
    clear_window(root)
    stuffing_text = tk.Label(root, text="What data from Stuffing do you want to see?", font=title_font, bg='powderblue')
    stuffing_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    stuffing_brands_button = tk.Button(root, text="Brands", command=stuffing_brands, font=button_font, width=20, height=2)
    stuffing_brands_button.place(relx=0.5, rely=0.14, anchor=tk.CENTER)

    types_button = tk.Button(root, text="Types", command=stuffing_types, font=button_font, width=20, height=2)
    types_button.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

    price_per_5_pounds_button = tk.Button(root, text="Stuffing by Price per 5 lbs", command=stuffing_by_price,
                                           font=button_font, width=20, height=2)
    price_per_5_pounds_button.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def stuffing_brands():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT brand FROM stuffing")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Brand"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def stuffing_types():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT type FROM stuffing")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Type"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def stuffing_by_price():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, type, priceperfivelbs FROM stuffing ORDER BY priceperfivelbs DESC, brand")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Brand", "Type", "Price per 5 lbs"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def products_options():
    clear_window(root)
    products_text = tk.Label(root, text="What data from Products do you want to see?", font=title_font, bg='powderblue')
    products_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    product_names_button = tk.Button(root, text="Names of Products", command=product_names,
                                     font=button_font, width=25, height=2)
    product_names_button.place(relx=0.5, rely=0.14, anchor=tk.CENTER)

    product_time_to_make_button = tk.Button(root, text="Products by Time to Make", command=product_time_to_make,
                                            font=button_font, width=25, height=2)
    product_time_to_make_button.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

    product_cost_to_make_button = tk.Button(root, text="Products by Total Cost to Make", command=product_cost_to_make,
                                            font=button_font, width=25, height=2)
    product_cost_to_make_button.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

    product_by_price_button = tk.Button(root, text="Products by Sale Price", command=product_by_price,
                                        font=button_font, width=25, height=2)
    product_by_price_button.place(relx=0.5, rely=0.41, anchor=tk.CENTER)

    product_by_num_in_stock_button = tk.Button(root, text="Products by Number in Stock", command=product_by_num_in_stock,
                                               font=button_font, width=25, height=2)
    product_by_num_in_stock_button.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def product_names():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name FROM finishedproducts ORDER BY name;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def product_time_to_make():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, totalcosttomake, saleprice, numberinstock, timetomake FROM finishedproducts "
                "ORDER BY timetomake;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name", "Total Cost to Make", "Sale Price", "Number in Stock", "Time to Make"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def product_cost_to_make():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, timetomake, saleprice, numberinstock, totalcosttomake FROM finishedproducts "
                "ORDER BY totalcosttomake;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name", "Time to Make", "Sale Price", "Number in Stock", "Total Cost to Make"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def product_by_price():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, timetomake, totalcosttomake, numberinstock, saleprice FROM finishedproducts "
                "ORDER BY saleprice;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name", "Time to Make", "Total Cost to Make", "Number in Stock", "Sale Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def product_by_num_in_stock():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, timetomake, totalcosttomake, saleprice, numberinstock FROM finishedproducts "
                "ORDER BY numberinstock;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name", "Time to Make", "Total Cost to Make", "Sale Price", "Number in Stock"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def materials_needed_name():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the name of the product whose materials you want to see?",
                                     font=title_font, bg='powderblue')
    new_product_name_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_product_name_materials_needed
    entry_product_name_materials_needed = tk.Entry(root, width=30, font=button_font)
    entry_product_name_materials_needed.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=materials_needed_display,
                            font=button_font, width=15, height=2)
    next_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def materials_needed_display():
    global product_name_materials_needed_input
    product_name_materials_needed_input = entry_product_name_materials_needed.get()
    clear_window(root)

    # Database connection
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Execute query with a parameter tuple
    cur.execute("""
        SELECT 
            fpm.MaterialType,
            CASE
                WHEN fpm.MaterialType = 'Yarn' THEN y.Brand
                WHEN fpm.MaterialType = 'Safety Eyes' THEN se.Shape
                WHEN fpm.MaterialType = 'Stuffing' THEN s.Brand
            END AS MaterialDetail,
            fpm.QuantityUsed,
            CASE
                WHEN fpm.MaterialType = 'Yarn' THEN y.Color
                WHEN fpm.MaterialType = 'Safety Eyes' THEN se.Color
            END AS Color,
            CASE
                WHEN fpm.MaterialType = 'Yarn' THEN y.FiberWeight
                ELSE NULL
            END AS FiberWeight,
            CASE
                WHEN fpm.MaterialType = 'Yarn' THEN y.FiberType
                ELSE NULL
            END AS FiberType,
            CASE
                WHEN fpm.MaterialType = 'Safety Eyes' THEN se.SizeInMM
                ELSE NULL
            END AS SizeInMM
        FROM 
            FinishedProducts fp
        JOIN 
            FinishedProductMaterials fpm ON fp.FinishedProductsID = fpm.FinishedProductsID
        LEFT JOIN 
            Yarn y ON fpm.MaterialType = 'Yarn' AND fpm.MaterialID = y.YarnID
        LEFT JOIN 
            SafetyEyes se ON fpm.MaterialType = 'Safety Eyes' AND fpm.MaterialID = se.SafetyEyesID
        LEFT JOIN 
            Stuffing s ON fpm.MaterialType = 'Stuffing' AND fpm.MaterialID = s.StuffingID
        WHERE 
            fp.Name = %s;
    """, (product_name_materials_needed_input,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Material Type", "Brand/Shape", "Quantity Used", "Color", "Fiber Weight", "Fiber Type", "Size (mm)"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value if value is not None else "", bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def what_i_can_make_material_type():
    clear_window(root)

    # Title label
    title_label = tk.Label(root, text="Select the Material Type", font=title_font, bg='powderblue')
    title_label.pack(pady=20)

    # Frame for buttons
    button_frame = tk.Frame(root, bg='powderblue')
    button_frame.pack(pady=20)

    # Buttons for material types
    yarn_button = tk.Button(button_frame, text="Yarn", command=what_i_can_make_yarn_details,
                            font=button_font, width=20, height=2)
    yarn_button.pack(pady=10)

    safety_eyes_button = tk.Button(button_frame, text="Safety Eyes", command=what_i_can_make_safety_eyes_details,
                                   font=button_font, width=20, height=2)
    safety_eyes_button.pack(pady=10)

    stuffing_button = tk.Button(button_frame, text="Stuffing", command=what_i_can_make_stuffing_details,
                                font=button_font, width=20, height=2)
    stuffing_button.pack(pady=10)

    # Back to start button
    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def what_i_can_make_yarn_details():
    clear_window(root)
    material_label = tk.Label(root, text="Enter Yarn Details", font=title_font, bg='powderblue')
    material_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    brand_label = tk.Label(root, text="Brand:", font=button_font, bg='powderblue')
    brand_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    global entry_what_i_can_make_yarn_brand
    entry_what_i_can_make_yarn_brand = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_yarn_brand.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    fiber_type_label = tk.Label(root, text="Fiber Type:", font=button_font, bg='powderblue')
    fiber_type_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    global entry_what_i_can_make_yarn_fiber_type
    entry_what_i_can_make_yarn_fiber_type = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_yarn_fiber_type.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    fiber_weight_label = tk.Label(root, text="Fiber Weight:", font=button_font, bg='powderblue')
    fiber_weight_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    global entry_what_i_can_make_yarn_fiber_weight
    entry_what_i_can_make_yarn_fiber_weight = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_yarn_fiber_weight.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    color_label = tk.Label(root, text="Color:", font=button_font, bg='powderblue')
    color_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    global entry_what_i_can_make_yarn_color
    entry_what_i_can_make_yarn_color = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_yarn_color.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    add_button = tk.Button(root, text="Add Yarn", command=what_i_can_make_add_yarn_list,
                           font=button_font, width=20, height=2)
    add_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    next_material_button = tk.Button(root, text="Add Another Material", command=what_i_can_make_material_type,
                                     font=button_font, width=20, height=2)
    next_material_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    find_products_button = tk.Button(root, text="Find Products", command=what_i_can_make_display,
                                     font=button_font, width=20, height=2)
    find_products_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def what_i_can_make_safety_eyes_details():
    clear_window(root)
    material_label = tk.Label(root, text="Enter Safety Eyes Details", font=title_font, bg='powderblue')
    material_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    size_label = tk.Label(root, text="Size (mm):", font=button_font, bg='powderblue')
    size_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    global entry_what_i_can_make_eyes_size
    entry_what_i_can_make_eyes_size = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_eyes_size.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    color_label = tk.Label(root, text="Color:", font=button_font, bg='powderblue')
    color_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    global entry_what_i_can_make_eyes_color
    entry_what_i_can_make_eyes_color = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_eyes_color.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    shape_label = tk.Label(root, text="Shape:", font=button_font, bg='powderblue')
    shape_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    global entry_what_i_can_make_eyes_shape
    entry_what_i_can_make_eyes_shape = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_eyes_shape.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    add_button = tk.Button(root, text="Add Safety Eyes", command=what_i_can_make_add_eyes_list,
                           font=button_font, width=20, height=2)
    add_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    next_material_button = tk.Button(root, text="Add Another Material", command=what_i_can_make_material_type,
                                     font=button_font, width=20, height=2)
    next_material_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    find_products_button = tk.Button(root, text="Find Products", command=what_i_can_make_display,
                                     font=button_font, width=20, height=2)
    find_products_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def what_i_can_make_stuffing_details():
    clear_window(root)
    material_label = tk.Label(root, text="Enter Stuffing Details", font=title_font, bg='powderblue')
    material_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    brand_label = tk.Label(root, text="Brand:", font=button_font, bg='powderblue')
    brand_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    global entry_what_i_can_make_stuffing_brand
    entry_what_i_can_make_stuffing_brand = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_stuffing_brand.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    type_label = tk.Label(root, text="Type:", font=button_font, bg='powderblue')
    type_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    global entry_what_i_can_make_stuffing_type
    entry_what_i_can_make_stuffing_type = tk.Entry(root, width=30, font=button_font)
    entry_what_i_can_make_stuffing_type.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    add_button = tk.Button(root, text="Add Stuffing", command=what_i_can_make_add_stuffing_list,
                           font=button_font, width=20, height=2)
    add_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    next_material_button = tk.Button(root, text="Add Another Material", command=what_i_can_make_material_type,
                                     font=button_font, width=20, height=2)
    next_material_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    find_products_button = tk.Button(root, text="Find Products", command=what_i_can_make_display,
                                     font=button_font, width=20, height=2)
    find_products_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def what_i_can_make_add_yarn_list():
    global what_i_can_make_yarn_brand_input
    what_i_can_make_yarn_brand_input = entry_what_i_can_make_yarn_brand.get()
    global what_i_can_make_yarn_fiber_type_input
    what_i_can_make_yarn_fiber_type_input = entry_what_i_can_make_yarn_fiber_type.get()
    global what_i_can_make_yarn_fiber_weight_input
    what_i_can_make_yarn_fiber_weight_input = entry_what_i_can_make_yarn_fiber_weight.get()
    global what_i_can_make_yarn_color_input
    what_i_can_make_yarn_color_input = entry_what_i_can_make_yarn_color.get()

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
                SELECT YarnID FROM Yarn 
                WHERE Brand = %s AND FiberType = %s AND FiberWeight = %s AND Color = %s
            """,
                    (what_i_can_make_yarn_brand_input,
                  what_i_can_make_yarn_fiber_type_input,
                  what_i_can_make_yarn_fiber_weight_input,
                  what_i_can_make_yarn_color_input))
        result = cur.fetchone()
        if result:
            what_i_can_make_materials.append(('Yarn', result[0]))
            messagebox.showinfo("Success", "Yarn material added!")
        else:
            messagebox.showerror("Error", "Yarn material not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def what_i_can_make_add_eyes_list():
    global what_i_can_make_eyes_size
    what_i_can_make_eyes_size = entry_what_i_can_make_eyes_size.get()
    global what_i_can_make_eyes_color
    what_i_can_make_eyes_color = entry_what_i_can_make_eyes_color.get()
    global what_i_can_make_eyes_shape
    what_i_can_make_eyes_shape = entry_what_i_can_make_eyes_shape.get()

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
                SELECT SafetyEyesID FROM SafetyEyes 
                WHERE SizeInMM = %s AND Color = %s AND Shape = %s
            """, (what_i_can_make_eyes_size,
                  what_i_can_make_eyes_color,
                  what_i_can_make_eyes_shape))
        result = cur.fetchone()
        if result:
            what_i_can_make_materials.append(('Safety Eyes', result[0]))
            messagebox.showinfo("Success", "Safety eyes material added!")
        else:
            messagebox.showerror("Error", "Safety eyes material not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def what_i_can_make_add_stuffing_list():
    global what_i_can_make_stuffing_brand_input
    what_i_can_make_stuffing_brand_input = entry_what_i_can_make_stuffing_brand.get()
    global what_i_can_make_stuffing_type_input
    what_i_can_make_stuffing_type_input = entry_what_i_can_make_stuffing_type.get()

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
                SELECT StuffingID FROM Stuffing 
                WHERE Brand = %s AND Type = %s
            """, (what_i_can_make_stuffing_brand_input,
                  what_i_can_make_stuffing_type_input))
        result = cur.fetchone()
        if result:
            what_i_can_make_materials.append(('Stuffing', result[0],))
            messagebox.showinfo("Success", "Stuffing material added!")
        else:
            messagebox.showerror("Error", "Stuffing material not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def what_i_can_make_display():
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        query = """
            SELECT fp.Name 
            FROM FinishedProducts fp
            JOIN FinishedProductMaterials fpm ON fp.FinishedProductsID = fpm.FinishedProductsID
            WHERE (fpm.MaterialType, fpm.MaterialID) IN %s
            GROUP BY fp.Name
            HAVING COUNT(DISTINCT fpm.MaterialID) = %s
        """
        cur.execute(query, (tuple(what_i_can_make_materials), len(what_i_can_make_materials)))
        results = cur.fetchall()
        cur.close()
        conn.close()

        # Create a canvas for scrolling
        canvas = tk.Canvas(root, bg='powderblue')
        canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame to contain the labels
        frame = tk.Frame(canvas, bg='powderblue')
        canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

        # Define header
        header_label = tk.Label(frame, text="Finished Products", font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=0, padx=5, pady=5)

        # Display results
        if results:
            for idx, result in enumerate(results, start=1):
                result_label = tk.Label(frame, text=result[0], bg='powderblue')
                result_label.grid(row=idx, column=0, padx=5, pady=5)
        else:
            no_results_label = tk.Label(frame, text="No finished products can be made with the given materials.", bg='powderblue')
            no_results_label.grid(row=1, column=0, padx=5, pady=5)

        frame.update_idletasks()  # Ensure frame is updated before computing its size
        canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
        canvas.yview_moveto(0)  # Ensure the view starts at the top

    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
        return  # Exit early if there was an error

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def all_customer_information():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, phonenumber, emailaddress FROM customers ORDER BY name")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name", "Phone Number", "Email Address"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def all_general_order_info():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT c.name, o.orderdate, o.formofpayment, o.totalprice "
                "FROM orders o JOIN customers c ON o.customerid = c.customerid;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Name", "Order Date", "Form of Payment", "Total Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value, bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)

def customer_purchased_name():
    clear_window(root)

    customer_name_label = tk.Label(root, text="What is the name of the customer?",
                                   font=title_font, bg='powderblue')
    customer_name_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_customer_purchased_name
    entry_customer_purchased_name = tk.Entry(root, width=30, font=button_font)
    entry_customer_purchased_name.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=customer_purchased_display,
                            font=button_font, width=15, height=2)
    next_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def customer_purchased_display():
    global customer_purchased_name_input
    customer_purchased_name_input = entry_customer_purchased_name.get()
    clear_window(root)

    # Database connection
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Execute query with a parameter tuple
    cur.execute("""
            SELECT 
                c.Name AS CustomerName,
                fp.Name AS ProductName,
                op.Quantity AS QuantityBought
            FROM 
                Customers c
            JOIN 
                Orders o ON c.CustomerID = o.CustomerID
            JOIN 
                OrderProducts op ON o.OrderID = op.OrderID
            JOIN 
                FinishedProducts fp ON op.FinishedProductsID = fp.FinishedProductsID
            WHERE 
                c.Name = %s
            ORDER BY 
                fp.Name;
        """, (customer_purchased_name_input,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width() // 2, root.winfo_height() // 2), window=frame, anchor="center")

    # Define headers
    headers = ["Customer Name", "Product Name", "Quantity Purchased"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg='powderblue')
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value if value is not None else "", bg='powderblue')
            data_label.grid(row=idx, column=i, padx=5, pady=5)

    frame.update_idletasks()  # Ensure frame is updated before computing its size
    canvas.configure(scrollregion=canvas.bbox("all"))  # Recompute scrollregion
    canvas.yview_moveto(0)  # Ensure the view starts at the top

    back_to_start_button = tk.Button(root, text="Back to start", command=start_up)
    back_to_start_button.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-10)


def product_stats_name():
    clear_window(root)

    product_name_label = tk.Label(root, text="What is the name of the product?",
                                  font=title_font, bg='powderblue')
    product_name_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_product_stats_name
    entry_product_stats_name = tk.Entry(root, width=30, font=button_font)
    entry_product_stats_name.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=product_stats,
                            font=button_font, width=15, height=2)
    next_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def product_stats():
    global product_stats_name_input
    product_stats_name_input = entry_product_stats_name.get()
    clear_window(root)

    # Database connection
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    try:
        # Get the number of products sold and the total revenue
        cur.execute("""
            SELECT SUM(op.Quantity), SUM(op.Quantity * fp.SalePrice)
            FROM OrderProducts op
            JOIN FinishedProducts fp ON op.FinishedProductsID = fp.FinishedProductsID
            WHERE fp.Name = %s;
        """, (product_stats_name_input,))
        result = cur.fetchone()

        if result is None or result[0] is None:
            messagebox.showinfo("Info", "No sales data found for the specified product.")
        else:
            quantity_sold, total_revenue = result

            # Create a canvas for scrolling
            canvas = tk.Canvas(root, bg='powderblue')
            canvas.pack(side="left", fill="both", expand=True)

            # Add a scrollbar
            scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
            scrollbar.pack(side="right", fill="y")

            # Configure the canvas
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            # Create a frame to contain the labels
            frame = tk.Frame(canvas, bg='powderblue')
            canvas.create_window((0, 0), window=frame, anchor="nw")

            # Display the results
            quantity_label = tk.Label(frame, text=f"Total quantity sold: {quantity_sold}", font=("Arial", 12), bg='powderblue')
            quantity_label.pack(pady=5)
            revenue_label = tk.Label(frame, text=f"Total revenue: ${total_revenue:.2f}", font=("Arial", 12), bg='powderblue')
            revenue_label.pack(pady=5)

            # Calculate the vertical position to center the frame
            canvas.update_idletasks()
            canvas_height = canvas.winfo_height()
            frame_height = frame.winfo_reqheight()
            vertical_position = max((canvas_height - frame_height) // 2, 0)

            canvas.create_window((root.winfo_width() // 2, vertical_position), window=frame, anchor="center")

            canvas.yview_moveto(0)  # Ensure the view starts at the top

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up,
                                     font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def add_data_options():
    clear_window(root)

    add_data_text = tk.Label(root, text="What data do you want to add?", font=title_font, bg='powderblue')
    add_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    new_yarn_button = tk.Button(root, text="New yarn", command=new_yarn_details, font=button_font, width=35, height=2)
    new_yarn_button.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    new_safety_eyes_button = tk.Button(root, text="New safety eyes", command=new_eyes_details, font=button_font, width=35,
                                       height=2)
    new_safety_eyes_button.place(relx=0.5, rely=0.19, anchor=tk.CENTER)

    new_stuffing_button = tk.Button(root, text="New stuffing", command=new_stuffing_details, font=button_font, width=35,
                                    height=2)
    new_stuffing_button.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

    new_finished_product_button = tk.Button(root, text="New finished product", command=new_finished_product_details,
                                            font=button_font, width=35, height=2)
    new_finished_product_button.place(relx=0.5, rely=0.33, anchor=tk.CENTER)

    new_finished_product_material_button = tk.Button(root, text="New material for finished product",
                                                     command=new_product_material_name, font=button_font, width=35,
                                                     height=2)
    new_finished_product_material_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    new_customer_button = tk.Button(root, text="New customer", command=new_customer_details, font=button_font, width=35,
                                    height=2)
    new_customer_button.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

    new_order_button = tk.Button(root, text="New order", command=new_order_details, font=button_font, width=35, height=2)
    new_order_button.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def new_yarn_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each yarn attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Yarn Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Brand:", "Price:", "Fiber Type:", "Fiber Weight:", "Color:", "Yardage per Skein:",
                    "Grams per Skein:", "Skeins in Stock:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_yarn_brand, entry_new_yarn_price, entry_new_yarn_fiber_type, entry_new_yarn_fiber_weight
    global entry_new_yarn_color, entry_new_yarn_yardage, entry_new_yarn_grams, entry_new_yarn_in_stock
    entry_new_yarn_brand, entry_new_yarn_price, entry_new_yarn_fiber_type, entry_new_yarn_fiber_weight = entries[:4]
    entry_new_yarn_color, entry_new_yarn_yardage, entry_new_yarn_grams, entry_new_yarn_in_stock = entries[4:]

    add_button = tk.Button(form_frame, text="Add Yarn", command=add_new_yarn, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_yarn():
    global new_yarn_brand_input, new_yarn_price_input, new_yarn_fiber_type_input, new_yarn_fiber_weight_input
    global new_yarn_color_input, new_yarn_yardage_input, new_yarn_grams_input, new_yarn_in_stock_input
    new_yarn_brand_input = entry_new_yarn_brand.get()
    new_yarn_price_input = entry_new_yarn_price.get()
    new_yarn_fiber_type_input = entry_new_yarn_fiber_type.get()
    new_yarn_fiber_weight_input = entry_new_yarn_fiber_weight.get()
    new_yarn_color_input = entry_new_yarn_color.get()
    new_yarn_yardage_input = entry_new_yarn_yardage.get()
    new_yarn_grams_input = entry_new_yarn_grams.get()
    new_yarn_in_stock_input = entry_new_yarn_in_stock.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO yarn 
            (Brand, Price, FiberType, FiberWeight, Color, YardagePerSkein, GramsPerSkein, NumberOfSkeinsOwned)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                new_yarn_brand_input,
                new_yarn_price_input,
                new_yarn_fiber_type_input,
                new_yarn_fiber_weight_input,
                new_yarn_color_input,
                new_yarn_yardage_input,
                new_yarn_grams_input,
                new_yarn_in_stock_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Yarn has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_eyes_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each safety eyes attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Safety Eyes Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Size (mm):", "Color:", "Shape:", "Price:", "In Stock:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_eyes_size, entry_new_eyes_color, entry_new_eyes_shape, entry_new_eyes_price, entry_new_eyes_in_stock
    entry_new_eyes_size, entry_new_eyes_color, entry_new_eyes_shape, entry_new_eyes_price, entry_new_eyes_in_stock = entries

    add_button = tk.Button(form_frame, text="Add Safety Eyes", command=add_new_eyes, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_eyes():
    global new_eyes_size_input, new_eyes_color_input, new_eyes_shape_input, new_eyes_price_input, new_eyes_in_stock_input
    new_eyes_size_input = entry_new_eyes_size.get()
    new_eyes_color_input = entry_new_eyes_color.get()
    new_eyes_shape_input = entry_new_eyes_shape.get()
    new_eyes_price_input = entry_new_eyes_price.get()
    new_eyes_in_stock_input = entry_new_eyes_in_stock.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO safetyeyes (Price, SizeinMM, Color, Shape, NumberOfEyesOwned)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (
                new_eyes_price_input,
                new_eyes_size_input,
                new_eyes_color_input,
                new_eyes_shape_input,
                new_eyes_in_stock_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Safety eyes have been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_stuffing_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each stuffing attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Stuffing Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Brand:", "Type:", "Price per 5 lbs:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_stuffing_brand, entry_new_stuffing_type, entry_new_stuffing_price
    entry_new_stuffing_brand, entry_new_stuffing_type, entry_new_stuffing_price = entries

    add_button = tk.Button(form_frame, text="Add Stuffing", command=add_new_stuffing, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_stuffing():
    global new_stuffing_brand_input, new_stuffing_type_input, new_stuffing_price_input
    new_stuffing_brand_input = entry_new_stuffing_brand.get()
    new_stuffing_type_input = entry_new_stuffing_type.get()
    new_stuffing_price_input = entry_new_stuffing_price.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO stuffing (Brand, Type, PricePerFivelbs)
            VALUES (%s, %s, %s);
            """,
            (
                new_stuffing_brand_input,
                new_stuffing_type_input,
                new_stuffing_price_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Stuffing has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_finished_product_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each product attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Finished Product Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Product Name:", "Time to Make:", "Total Cost to Make:", "Sale Price:", "Number in Stock:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_finished_product_name, entry_new_finished_product_time, entry_new_finished_product_cost
    global entry_new_finished_product_saleprice, entry_new_finished_product_in_stock
    entry_new_finished_product_name, entry_new_finished_product_time, entry_new_finished_product_cost = entries[:3]
    entry_new_finished_product_saleprice, entry_new_finished_product_in_stock = entries[3:]

    add_button = tk.Button(form_frame, text="Add Product", command=add_new_finished_product, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_finished_product():
    global new_finished_product_name_input, new_finished_product_time_input, new_finished_product_cost_input
    global new_finished_product_saleprice_input, new_finished_product_in_stock_input
    new_finished_product_name_input = entry_new_finished_product_name.get()
    new_finished_product_time_input = entry_new_finished_product_time.get()
    new_finished_product_cost_input = entry_new_finished_product_cost.get()
    new_finished_product_saleprice_input = entry_new_finished_product_saleprice.get()
    new_finished_product_in_stock_input = entry_new_finished_product_in_stock.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO finishedproducts (name, timetomake, totalcosttomake, saleprice, numberinstock)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (
                new_finished_product_name_input,
                new_finished_product_time_input,
                new_finished_product_cost_input,
                new_finished_product_saleprice_input,
                new_finished_product_in_stock_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "New product has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_product_material_name():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the name of the product that is getting a "
                                                "new material added to it?", font=title_font, bg='powderblue')
    new_product_name_text.pack(pady=20)

    global entry_new_product_material_name
    entry_new_product_material_name = tk.Entry(root, width=30, font=button_font)
    entry_new_product_material_name.pack(pady=20)

    next_button = tk.Button(root, text="Next", command=new_product_material_type, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def new_product_material_type():
    global new_product_material_name_input
    new_product_material_name_input = entry_new_product_material_name.get()
    clear_window(root)

    # Title label
    title_label = tk.Label(root, text="Is the new material Yarn, Safety Eyes, or Stuffing?", font=title_font, bg='powderblue')
    title_label.pack(pady=20)

    # Frame for buttons
    button_frame = tk.Frame(root, bg='powderblue')
    button_frame.pack(pady=20)

    # Buttons for material types
    yarn_button = tk.Button(button_frame, text="Yarn", command=new_product_material_yarn_details,
                            font=button_font, width=20, height=2)
    yarn_button.pack(pady=10)

    safety_eyes_button = tk.Button(button_frame, text="Safety Eyes", command=new_product_material_safety_eyes_details,
                                   font=button_font, width=20, height=2)
    safety_eyes_button.pack(pady=10)

    stuffing_button = tk.Button(button_frame, text="Stuffing", command=new_product_material_stuffing_details,
                                font=button_font, width=20, height=2)
    stuffing_button.pack(pady=10)

    # Back to start button
    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def new_product_material_yarn_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each product attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Yarn Material Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Brand",
        "Fiber Type",
        "Fiber Weight",
        "Color",
        "Quantity"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_product_material_yarn_brand, entry_new_product_material_yarn_fiber_type
    global entry_new_product_material_yarn_fiber_weight, entry_new_product_material_yarn_color
    global entry_new_product_material_yarn_quantity

    entry_new_product_material_yarn_brand, entry_new_product_material_yarn_fiber_type = entries[:2]
    entry_new_product_material_yarn_fiber_weight, entry_new_product_material_yarn_color = entries[2:4]
    entry_new_product_material_yarn_quantity = entries[4]

    add_button = tk.Button(form_frame, text="Add Yarn", command=add_new_product_material_yarn, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_product_material_yarn():
    global new_product_material_yarn_brand_input, new_product_material_yarn_fiber_type_input
    global new_product_material_yarn_fiber_weight_input, new_product_material_yarn_color_input
    global new_product_material_yarn_quantity_input

    new_product_material_yarn_brand_input = entry_new_product_material_yarn_brand.get()
    new_product_material_yarn_fiber_type_input = entry_new_product_material_yarn_fiber_type.get()
    new_product_material_yarn_fiber_weight_input = entry_new_product_material_yarn_fiber_weight.get()
    new_product_material_yarn_color_input = entry_new_product_material_yarn_color.get()
    new_product_material_yarn_quantity_input = entry_new_product_material_yarn_quantity.get()

    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get FinishedProductsID
        cur.execute(
            "SELECT FinishedProductsID FROM FinishedProducts WHERE Name = %s",
            (new_product_material_name_input,)
        )
        finished_product_id = cur.fetchone()
        if finished_product_id is None:
            messagebox.showerror("Error", "Finished product not found!")
            return
        finished_product_id = finished_product_id[0]

        # Get MaterialID for Yarn
        cur.execute(
            """
            SELECT YarnID FROM Yarn 
            WHERE Brand = %s AND Color = %s AND FiberType = %s AND FiberWeight = %s
            """,
            (
                new_product_material_yarn_brand_input,
                new_product_material_yarn_color_input,
                new_product_material_yarn_fiber_type_input,
                new_product_material_yarn_fiber_weight_input,
            )
        )
        material_id = cur.fetchone()
        if material_id is None:
            messagebox.showerror("Error", "Material not found!")
            return
        material_id = material_id[0]

        # Insert into FinishedProductMaterials
        cur.execute(
            """
            INSERT INTO FinishedProductMaterials (FinishedProductsID, MaterialType, MaterialID, QuantityUsed)
            VALUES (%s, %s, %s, %s)
            """,
            (finished_product_id, 'Yarn', material_id, new_product_material_yarn_quantity_input)
        )
        conn.commit()
        messagebox.showinfo("Success", "Material has been successfully added to the finished product!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_product_material_safety_eyes_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each product attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Safety Eyes Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Size in mm",
        "Color",
        "Shape",
        "Quantity"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_product_material_safety_eyes_size, entry_new_product_material_safety_eyes_color
    global entry_new_product_material_safety_eyes_shape, entry_new_product_material_safety_eyes_quantity

    entry_new_product_material_safety_eyes_size, entry_new_product_material_safety_eyes_color = entries[:2]
    entry_new_product_material_safety_eyes_shape, entry_new_product_material_safety_eyes_quantity = entries[2:]

    add_button = tk.Button(form_frame, text="Add Safety Eyes", command=add_new_product_material_safety_eyes, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_product_material_safety_eyes():
    global new_product_material_safety_eyes_size_input, new_product_material_safety_eyes_color_input
    global new_product_material_safety_eyes_shape_input, new_product_material_safety_eyes_quantity_input

    new_product_material_safety_eyes_size_input = entry_new_product_material_safety_eyes_size.get()
    new_product_material_safety_eyes_color_input = entry_new_product_material_safety_eyes_color.get()
    new_product_material_safety_eyes_shape_input = entry_new_product_material_safety_eyes_shape.get()
    new_product_material_safety_eyes_quantity_input = entry_new_product_material_safety_eyes_quantity.get()

    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get FinishedProductsID
        cur.execute(
            "SELECT FinishedProductsID FROM FinishedProducts WHERE Name = %s",
            (new_product_material_name_input,)
        )
        finished_product_id = cur.fetchone()
        if finished_product_id is None:
            messagebox.showerror("Error", "Finished product not found!")
            return
        finished_product_id = finished_product_id[0]

        # Get MaterialID for Safety Eyes
        cur.execute(
            """
            SELECT SafetyEyesID FROM SafetyEyes 
            WHERE SizeInMM = %s AND Color = %s AND Shape = %s
            """,
            (
                new_product_material_safety_eyes_size_input,
                new_product_material_safety_eyes_color_input,
                new_product_material_safety_eyes_shape_input,
            )
        )
        material_id = cur.fetchone()
        if material_id is None:
            messagebox.showerror("Error", "Material not found!")
            return
        material_id = material_id[0]

        # Insert into FinishedProductMaterials
        cur.execute(
            """
            INSERT INTO FinishedProductMaterials (FinishedProductsID, MaterialType, MaterialID, QuantityUsed)
            VALUES (%s, %s, %s, %s)
            """,
            (finished_product_id, 'Safety Eyes', material_id, new_product_material_safety_eyes_quantity_input)
        )
        conn.commit()
        messagebox.showinfo("Success", "Material has been successfully added to the finished product!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_product_material_stuffing_details():
    clear_window(root)

    # Title label
    title_label = tk.Label(root, text="Enter New Stuffing Material Details", font=title_font, bg='powderblue')
    title_label.pack(pady=20)

    # Label and Entry for material details
    stuffing_label = tk.Label(root, text="Brand", font=button_font, bg='powderblue')
    stuffing_label.pack(pady=5)

    global entry_new_product_material_stuffing_brand
    entry_new_product_material_stuffing_brand = tk.Entry(root, width=30, font=button_font)
    entry_new_product_material_stuffing_brand.pack(pady=5)

    type_label = tk.Label(root, text="Type", font=button_font, bg='powderblue')
    type_label.pack(pady=5)

    global entry_new_product_material_stuffing_type
    entry_new_product_material_stuffing_type = tk.Entry(root, width=30, font=button_font)
    entry_new_product_material_stuffing_type.pack(pady=5)

    add_button = tk.Button(root, text="Add Stuffing", command=add_new_product_material_stuffing, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_product_material_stuffing():
    global new_product_material_stuffing_brand_input, new_product_material_stuffing_type_input

    new_product_material_stuffing_brand_input = entry_new_product_material_stuffing_brand.get()
    new_product_material_stuffing_type_input = entry_new_product_material_stuffing_type.get()

    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get FinishedProductsID
        cur.execute(
            "SELECT FinishedProductsID FROM FinishedProducts WHERE Name = %s",
            (new_product_material_name_input,)
        )
        finished_product_id = cur.fetchone()
        if finished_product_id is None:
            messagebox.showerror("Error", "Finished product not found!")
            return
        finished_product_id = finished_product_id[0]

        # Get MaterialID for Stuffing
        cur.execute(
            """
            SELECT StuffingID FROM Stuffing
            WHERE Brand = %s AND Type = %s
            """,
            (
                new_product_material_stuffing_brand_input,
                new_product_material_stuffing_type_input
            )
        )
        material_id = cur.fetchone()
        if material_id is None:
            messagebox.showerror("Error", "Material not found!")
            return
        material_id = material_id[0]

        # Insert into FinishedProductMaterials for stuffing
        cur.execute(
            """
            INSERT INTO FinishedProductMaterials (FinishedProductsID, MaterialType, MaterialID, QuantityUsed)
            VALUES (%s, %s, %s, %s)
            """,
            (finished_product_id, 'Stuffing', material_id, '0')
        )
        conn.commit()
        messagebox.showinfo("Success", "Stuffing material has been successfully added to the finished product!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def new_customer_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each customer attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter New Customer Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["First and Last Name:", "Phone Number (optional):", "Email Address (optional):"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_new_customer_name, entry_new_customer_phone, entry_new_customer_email
    entry_new_customer_name, entry_new_customer_phone, entry_new_customer_email = entries

    add_button = tk.Button(form_frame, text="Add Customer", command=add_new_customer, font=button_font, width=20, height=2)
    add_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_new_customer():
    global new_customer_name_input, new_customer_phone_input, new_customer_email_input
    new_customer_name_input = entry_new_customer_name.get()
    new_customer_phone_input = entry_new_customer_phone.get()
    new_customer_email_input = entry_new_customer_email.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO customers (Name, PhoneNumber, EmailAddress)
            VALUES (%s, %s, %s);
            """,
            (
                new_customer_name_input,
                new_customer_phone_input,
                new_customer_email_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Customer has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()


def new_order_details():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="Enter Order Details",
                                     font=title_font, bg='powderblue')
    new_product_name_text.pack(pady=10)


    # Customer name entry
    new_product_name_text = tk.Label(root, text="First and Last Name",
                                     font=button_font, bg='powderblue')
    new_product_name_text.pack()
    global entry_new_order_name
    entry_new_order_name = tk.Entry(root, width=30, font=button_font)
    entry_new_order_name.pack(pady=10)

    # Order date entry
    new_product_date_text = tk.Label(root, text="Order Date (YYYY-MM-DD format)",
                                     font=button_font, bg='powderblue')
    new_product_date_text.pack()
    global entry_new_order_date
    entry_new_order_date = tk.Entry(root, width=30, font=button_font)
    entry_new_order_date.pack(pady=10)

    # Form of payment entry
    new_product_payment_text = tk.Label(root, text="Form of Payment",
                                     font=button_font, bg='powderblue')
    new_product_payment_text.pack()
    global entry_new_order_form_payment
    entry_new_order_form_payment = tk.Entry(root, width=30, font=button_font)
    entry_new_order_form_payment.pack(pady=10)

    # Submit button
    submit_button = tk.Button(root, text="Next", command=new_order_products_purchased,
                              font=button_font, width=20, height=2)
    submit_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    global purchased_products
    purchased_products = []

def new_order_products_purchased():
    global new_order_date_input
    new_order_date_input = entry_new_order_date.get()
    global new_order_name_input
    new_order_name_input = entry_new_order_name.get()
    global new_order_form_payment_input
    new_order_form_payment_input = entry_new_order_form_payment.get()
    clear_window(root)
    new_order_products_text = tk.Label(root, text="Enter the Product Name and Quantity Purchased",
                                       font=title_font, bg='powderblue')
    new_order_products_text.pack(pady=10)

    global entry_new_product_name
    global entry_new_product_quantity
    entry_new_product_name = tk.Entry(root, width=30, font=button_font)
    entry_new_product_name.pack(pady=5)
    entry_new_product_name.insert(0, "Product Name")

    entry_new_product_quantity = tk.Entry(root, width=30, font=button_font)
    entry_new_product_quantity.pack(pady=5)
    entry_new_product_quantity.insert(0, "Quantity")

    add_product_button = tk.Button(root, text="Add Product", command=add_product_to_order_list,
                                   font=button_font, width=20, height=2)
    add_product_button.pack(pady=20)

    finish_button = tk.Button(root, text="Finish Order", command=add_order_to_db, font=button_font, width=20, height=2)
    finish_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def add_product_to_order_list():
    product_name = entry_new_product_name.get()
    quantity = int(entry_new_product_quantity.get())
    purchased_products.append((product_name, quantity))
    entry_new_product_name.delete(0, tk.END)
    entry_new_product_quantity.delete(0, tk.END)
    messagebox.showinfo("Success", "Product added to the list!")

def add_order_before_db(customer_name, order_date, form_of_payment, purchased_products):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        cur.execute(
            "SELECT CustomerID FROM Customers WHERE Name = %s",
            (customer_name,)
        )
        customer = cur.fetchone()
        if customer is None:
            cur.execute(
                """
                INSERT INTO Customers (Name)
                VALUES (%s)
                RETURNING CustomerID
                """,
                (customer_name,)
            )
            customer_id = cur.fetchone()[0]
        else:
            customer_id = customer[0]

        cur.execute(
            """
            INSERT INTO Orders (CustomerID, OrderDate, FormOfPayment, TotalPrice)
            VALUES (%s, %s, %s, %s)
            RETURNING OrderID
            """,
            (customer_id, order_date, form_of_payment, 0)
        )
        order_id = cur.fetchone()[0]

        total_price = 0

        # Process each product in the order
        for product_name, quantity in purchased_products:
            cur.execute(
                "SELECT FinishedProductsID, SalePrice FROM FinishedProducts WHERE Name = %s",
                (product_name,)
            )
            finished_product = cur.fetchone()
            if finished_product is None:
                raise ValueError(f"Product '{product_name}' not found in FinishedProducts")

            finished_product_id = finished_product[0]
            sale_price = finished_product[1]
            product_total = sale_price * quantity
            total_price += product_total

            cur.execute(
                """
                INSERT INTO OrderProducts (OrderID, FinishedProductsID, Quantity)
                VALUES (%s, %s, %s)
                """,
                (order_id, finished_product_id, quantity)
            )

            cur.execute(
                """
                INSERT INTO CustomerPurchases (CustomerID, FinishedProductsID)
                VALUES (%s, %s)
                """,
                (customer_id, finished_product_id)
            )

        # Update the total price of the order
        cur.execute(
            "UPDATE Orders SET TotalPrice = %s WHERE OrderID = %s",
            (total_price, order_id)
        )

        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def add_order_to_db():
    try:
        # Parse the date string into a datetime object
        order_date = datetime.strptime(new_order_date_input, "%Y-%m-%d")

        # Insert the order into the database
        add_order_before_db(new_order_name_input, order_date, new_order_form_payment_input, purchased_products)
        messagebox.showinfo("Success", "Order has been successfully added!")
        start_up()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def modify_data_options():
    clear_window(root)

    modify_data_text = tk.Label(root, text="What data do you want to modify?", font=title_font, bg='powderblue')
    modify_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    quantity_update_button = tk.Button(root, text="Quantity Update", command=quantity_update_options, font=button_font, width=35, height=2)
    quantity_update_button.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    product_price_button = tk.Button(root, text="Product Sale Price", command=modify_product_price_details, font=button_font, width=35, height=2)
    product_price_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    product_time_button = tk.Button(root, text="Estimated Time to Make a Product", command=modify_product_time_details, font=button_font, width=35, height=2)
    product_time_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    customer_info_button = tk.Button(root, text="Customer Phone # / Email Address", command=modify_customer_details, font=button_font, width=35, height=2)
    customer_info_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def quantity_update_options():
    clear_window(root)

    quantity_update_text = tk.Label(root, text="What type of data do you want to update the quantity of?", font=title_font, bg='powderblue')
    quantity_update_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    finished_product_button = tk.Button(root, text="Finished Products", command=modify_product_name, font=button_font, width=30, height=2)
    finished_product_button.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    yarn_button = tk.Button(root, text="Yarn", command=modify_yarn_details, font=button_font, width=30, height=2)
    yarn_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    safety_eyes_button = tk.Button(root, text="Safety Eyes", command=modify_eyes_details, font=button_font, width=30, height=2)
    safety_eyes_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    material_product_button = tk.Button(root, text="Material for a Product",
                                        command=modify_product_material_quantity_name, font=button_font, width=30, height=2)
    material_product_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def modify_product_name():
    clear_window(root)

    modify_product_text = tk.Label(root, text="What is the name of the product whose quantity you are modifying?", font=title_font, bg='powderblue')
    modify_product_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_modify_product_name
    entry_modify_product_name = tk.Entry(root, width=30, font=button_font)
    entry_modify_product_name.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=product_increasing_decreasing, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def product_increasing_decreasing():
    global modify_product_name_input
    modify_product_name_input = entry_modify_product_name.get()
    clear_window(root)

    increasing_decreasing_text = tk.Label(root, text="Are you increasing or decreasing the quantity?", font=title_font, bg='powderblue')
    increasing_decreasing_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    increasing_button = tk.Button(root, text="Increasing", command=product_increasing_howmuch, font=button_font, width=20, height=2)
    increasing_button.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    decreasing_button = tk.Button(root, text="Decreasing", command=product_decreasing_howmuch, font=button_font, width=20, height=2)
    decreasing_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def product_increasing_howmuch():
    clear_window(root)

    increasing_howmuch_text = tk.Label(root, text="How many of the new product are you adding?", font=title_font, bg='powderblue')
    increasing_howmuch_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_increase_product
    entry_increase_product = tk.Entry(root, width=30, font=button_font)
    entry_increase_product.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=increase_product, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def increase_product():
    global increase_product_input
    increase_product_input = entry_increase_product.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE finishedproducts 
            SET numberinstock = numberinstock + %s
            WHERE name = %s
            """,
            (
                increase_product_input,
                modify_product_name_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Quantity has been successfully modified!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def product_decreasing_howmuch():
    clear_window(root)

    decreasing_howmuch_text = tk.Label(root, text="How many of the new product are you subtracting?", font=title_font, bg='powderblue')
    decreasing_howmuch_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_decrease_product
    entry_decrease_product = tk.Entry(root, width=30, font=button_font)
    entry_decrease_product.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=decrease_product, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def decrease_product():
    global decrease_product_input
    decrease_product_input = entry_decrease_product.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE finishedproducts 
            SET numberinstock = numberinstock - %s
            WHERE name = %s
            """,
            (
                decrease_product_input,
                modify_product_name_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Quantity has been successfully modified!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def modify_yarn_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each yarn attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Yarn Quantity", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Brand",
        "Fiber Type",
        "Fiber Weight",
        "Color"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_yarn_brand, entry_modify_yarn_fiber_type
    global entry_modify_yarn_fiber_weight, entry_modify_yarn_color
    entry_modify_yarn_brand, entry_modify_yarn_fiber_type = entries[:2]
    entry_modify_yarn_fiber_weight, entry_modify_yarn_color = entries[2:]

    next_button = tk.Button(form_frame, text="Next", command=yarn_increasing_decreasing, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def yarn_increasing_decreasing():
    global modify_yarn_brand_input, modify_yarn_fiber_weight_input, modify_yarn_fiber_type_input, modify_yarn_color_input
    modify_yarn_brand_input = entry_modify_yarn_brand.get()
    modify_yarn_fiber_weight_input = entry_modify_yarn_fiber_weight.get()
    modify_yarn_fiber_type_input = entry_modify_yarn_fiber_type.get()
    modify_yarn_color_input = entry_modify_yarn_color.get()
    clear_window(root)

    increasing_decreasing_text = tk.Label(root, text="Are you increasing or decreasing the quantity?", font=title_font, bg='powderblue')
    increasing_decreasing_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    increasing_button = tk.Button(root, text="Increasing", command=yarn_increasing_howmuch, font=button_font, width=20, height=2)
    increasing_button.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    decreasing_button = tk.Button(root, text="Decreasing", command=yarn_decreasing_howmuch, font=button_font, width=20, height=2)
    decreasing_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def yarn_increasing_howmuch():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="How many skeins of the yarn are you adding?", font=title_font, bg='powderblue')
    look_at_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_increase_yarn
    entry_increase_yarn = tk.Entry(root, width=30, font=button_font)
    entry_increase_yarn.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=increase_yarn, font=button_font, width=20,
                            height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def increase_yarn():
    global increase_yarn_input
    increase_yarn_input = entry_increase_yarn.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE yarn 
            SET numberofskeinsowned = numberofskeinsowned + %s
            WHERE brand = %s and fibertype = %s and fiberweight = %s and color = %s;
            """,
            (
                increase_yarn_input,
                modify_yarn_brand_input,
                modify_yarn_fiber_type_input,
                modify_yarn_fiber_weight_input,
                modify_yarn_color_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Quantity has been successfully modified!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def yarn_decreasing_howmuch():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="How many skeins of the yarn are you subtracting?", font=title_font, bg='powderblue')
    look_at_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_decrease_yarn
    entry_decrease_yarn = tk.Entry(root, width=30, font=button_font)
    entry_decrease_yarn.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=decrease_yarn, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def decrease_yarn():
    global decrease_yarn_input
    decrease_yarn_input = entry_decrease_yarn.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE yarn 
            SET numberofskeinsowned = numberofskeinsowned - %s
            WHERE brand = %s and fibertype = %s and fiberweight = %s and color = %s;
            """,
            (
                decrease_yarn_input,
                modify_yarn_brand_input,
                modify_yarn_fiber_type_input,
                modify_yarn_fiber_weight_input,
                modify_yarn_color_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Quantity has been successfully modified!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def modify_eyes_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each eye attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Safety Eyes Quantity", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Size (mm)",
        "Color",
        "Shape"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_eyes_size, entry_modify_eyes_color, entry_modify_eyes_shape
    entry_modify_eyes_size, entry_modify_eyes_color, entry_modify_eyes_shape = entries

    next_button = tk.Button(form_frame, text="Next", command=eyes_increasing_decreasing, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def eyes_increasing_decreasing():
    global modify_eyes_size_input, modify_eyes_color_input, modify_eyes_shape_input
    modify_eyes_size_input = entry_modify_eyes_size.get()
    modify_eyes_color_input = entry_modify_eyes_color.get()
    modify_eyes_shape_input = entry_modify_eyes_shape.get()
    clear_window(root)

    increasing_decreasing_text = tk.Label(root, text="Are you increasing or decreasing the quantity?", font=title_font, bg='powderblue')
    increasing_decreasing_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    increasing_button = tk.Button(root, text="Increasing", command=eyes_increasing_howmuch, font=button_font, width=20, height=2)
    increasing_button.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    decreasing_button = tk.Button(root, text="Decreasing", command=eyes_decreasing_howmuch, font=button_font, width=20, height=2)
    decreasing_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def eyes_increasing_howmuch():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="How many safety eyes are you adding?", font=title_font, bg='powderblue')
    look_at_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_increase_eyes
    entry_increase_eyes = tk.Entry(root, width=30, font=button_font)
    entry_increase_eyes.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=increase_eyes, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def increase_eyes():
    global increase_eyes_input
    increase_eyes_input = entry_increase_eyes.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE safetyeyes 
            SET numberofeyesowned = numberofeyesowned + %s
            WHERE sizeinmm = %s AND color = %s AND shape = %s;
            """,
            (
                increase_eyes_input,
                modify_eyes_size_input,
                modify_eyes_color_input,
                modify_eyes_shape_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Quantity has been successfully modified!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def eyes_decreasing_howmuch():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="How many safety eyes are you subtracting?", font=title_font, bg='powderblue')
    look_at_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_decrease_eyes
    entry_decrease_eyes = tk.Entry(root, width=30, font=button_font)
    entry_decrease_eyes.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=decrease_eyes, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def decrease_eyes():
    global decrease_eyes_input
    decrease_eyes_input = entry_decrease_eyes.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE safetyeyes 
            SET numberofeyesowned = numberofeyesowned - %s
            WHERE sizeinmm = %s AND color = %s AND shape = %s;
            """,
            (
                decrease_eyes_input,
                modify_eyes_size_input,
                modify_eyes_color_input,
                modify_eyes_shape_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Quantity has been successfully modified!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def modify_product_material_quantity_name():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="What is the name of the product that has the material whose quantity you are modifying?", font=title_font, bg='powderblue')
    look_at_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    global entry_modify_product_material_quantity_name
    entry_modify_product_material_quantity_name = tk.Entry(root, width=30, font=button_font)
    entry_modify_product_material_quantity_name.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=modify_product_material_quantity_type, font=button_font, width=20, height=2)
    next_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def modify_product_material_quantity_type():
    global modify_product_material_quantity_name_input
    modify_product_material_quantity_name_input = entry_modify_product_material_quantity_name.get()
    clear_window(root)

    # Title label
    title_label = tk.Label(root, text="Select the Product Material Type", font=title_font, bg='powderblue')
    title_label.pack(pady=20)

    # Frame for buttons
    button_frame = tk.Frame(root, bg='powderblue')
    button_frame.pack(pady=20)

    # Buttons for material types
    yarn_button = tk.Button(button_frame, text="Yarn", command=modify_product_material_quantity_yarn_details,
                            font=button_font, width=20, height=2)
    yarn_button.pack(pady=10)

    safety_eyes_button = tk.Button(button_frame, text="Safety Eyes", command=modify_product_material_quantity_eyes_details,
                                   font=button_font, width=20, height=2)
    safety_eyes_button.pack(pady=10)

    # Back to start button
    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def modify_product_material_quantity_yarn_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each yarn attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Product Material Quantity - Yarn", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Brand",
        "Fiber Type",
        "Fiber Weight",
        "Color",
        "New Quantity"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_product_material_quantity_yarn_brand, entry_modify_product_material_quantity_yarn_fiber_type
    global entry_modify_product_material_quantity_yarn_fiber_weight, entry_modify_product_material_quantity_yarn_color
    global entry_modify_product_material_quantity_yarn_quantity
    entry_modify_product_material_quantity_yarn_brand, entry_modify_product_material_quantity_yarn_fiber_type = entries[:2]
    entry_modify_product_material_quantity_yarn_fiber_weight, entry_modify_product_material_quantity_yarn_color = entries[2:4]
    entry_modify_product_material_quantity_yarn_quantity = entries[4]

    next_button = tk.Button(form_frame, text="Modify", command=modify_product_material_quantity_yarn, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def modify_product_material_quantity_yarn():
    global modify_product_material_quantity_yarn_brand_input, modify_product_material_quantity_yarn_fiber_type_input
    global modify_product_material_quantity_yarn_fiber_weight_input, modify_product_material_quantity_yarn_color_input
    global modify_product_material_quantity_yarn_quantity_input
    modify_product_material_quantity_yarn_brand_input = entry_modify_product_material_quantity_yarn_brand.get()
    modify_product_material_quantity_yarn_fiber_type_input = entry_modify_product_material_quantity_yarn_fiber_type.get()
    modify_product_material_quantity_yarn_fiber_weight_input = entry_modify_product_material_quantity_yarn_fiber_weight.get()
    modify_product_material_quantity_yarn_color_input = entry_modify_product_material_quantity_yarn_color.get()
    modify_product_material_quantity_yarn_quantity_input = entry_modify_product_material_quantity_yarn_quantity.get()
    clear_window(root)

    try:
        modify_product_material_quantity_yarn_quantity_input = float(modify_product_material_quantity_yarn_quantity_input)
    except ValueError:
        messagebox.showinfo("Error", "Invalid quantity entered. Please enter a numeric value.")
        return

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            SELECT YarnID FROM Yarn 
            WHERE Brand = %s AND FiberType = %s AND FiberWeight = %s AND Color = %s
            """, (modify_product_material_quantity_yarn_brand_input, modify_product_material_quantity_yarn_fiber_type_input,
                  modify_product_material_quantity_yarn_fiber_weight_input, modify_product_material_quantity_yarn_color_input))

        yarn = cur.fetchone()
        if yarn:
            yarn_id = yarn[0]

            # Update the quantity
            cur.execute("""
                UPDATE FinishedProductMaterials
                SET QuantityUsed = %s 
                WHERE MaterialID = %s;
            """, (modify_product_material_quantity_yarn_quantity_input, yarn_id))

            conn.commit()
            messagebox.showinfo("Success", "Yarn quantity has been successfully updated.")
        else:
            messagebox.showinfo("Error", "No matching yarn found with the given details.")

        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {e}")
        if conn:
            conn.close()
    start_up()

def modify_product_material_quantity_eyes_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Product Material Quantity - Safety Eyes", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Size in MM",
        "Color",
        "Shape",
        "New Quantity"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_product_material_quantity_eyes_size, entry_modify_product_material_quantity_eyes_color
    global entry_modify_product_material_quantity_eyes_shape, entry_modify_product_material_quantity_eyes_quantity
    entry_modify_product_material_quantity_eyes_size, entry_modify_product_material_quantity_eyes_color = entries[:2]
    entry_modify_product_material_quantity_eyes_shape, entry_modify_product_material_quantity_eyes_quantity = entries[2:4]

    next_button = tk.Button(form_frame, text="Modify", command=modify_product_material_quantity_eyes, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def modify_product_material_quantity_eyes():
    global modify_product_material_quantity_eyes_size_input, modify_product_material_quantity_eyes_color_input
    global modify_product_material_quantity_eyes_shape_input, modify_product_material_quantity_eyes_quantity_input
    modify_product_material_quantity_eyes_size_input = entry_modify_product_material_quantity_eyes_size.get()
    modify_product_material_quantity_eyes_color_input = entry_modify_product_material_quantity_eyes_color.get()
    modify_product_material_quantity_eyes_shape_input = entry_modify_product_material_quantity_eyes_shape.get()
    modify_product_material_quantity_eyes_quantity_input = entry_modify_product_material_quantity_eyes_quantity.get()
    clear_window(root)

    try:
        modify_product_material_quantity_eyes_quantity_input = float(modify_product_material_quantity_eyes_quantity_input)
    except ValueError:
        messagebox.showinfo("Error", "Invalid quantity entered. Please enter a numeric value.")
        return

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            SELECT SafetyEyesID FROM SafetyEyes 
            WHERE SizeInMM = %s AND Color = %s AND Shape = %s
            """, (modify_product_material_quantity_eyes_size_input, modify_product_material_quantity_eyes_color_input,
                  modify_product_material_quantity_eyes_shape_input))

        eyes = cur.fetchone()
        if eyes:
            eyes_id = eyes[0]

            # Update the quantity
            cur.execute("""
                UPDATE FinishedProductMaterials
                SET QuantityUsed = %s 
                WHERE MaterialID = %s;
            """, (modify_product_material_quantity_eyes_quantity_input, eyes_id))

            conn.commit()
            messagebox.showinfo("Success", "Safety Eyes quantity has been successfully updated.")
        else:
            messagebox.showinfo("Error", "No matching safety eyes found with the given details.")

        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {e}")
        if conn:
            conn.close()
    start_up()

def modify_product_price_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Product Price", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Product Name",
        "New Price"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_product_price_name, entry_modify_product_price
    entry_modify_product_price_name, entry_modify_product_price = entries

    next_button = tk.Button(form_frame, text="Modify", command=get_product_price_details_and_modify, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def get_product_price_details_and_modify():
    global modify_product_price_name_input, modify_product_price_input
    modify_product_price_name_input = entry_modify_product_price_name.get()
    modify_product_price_input = entry_modify_product_price.get()
    modify_product_price()

def modify_product_price():
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE finishedproducts
            SET saleprice = %s
            WHERE name = %s;
            """,
            (
                modify_product_price_input,
                modify_product_price_name_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Sale price has been successfully modified!")
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def modify_product_time_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Product Time", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Product Name",
        "Estimated Time to Make"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_product_time_name, entry_modify_product_time_time
    entry_modify_product_time_name, entry_modify_product_time_time = entries

    next_button = tk.Button(form_frame, text="Modify", command=get_product_time_details_and_modify, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def get_product_time_details_and_modify():
    global modify_product_time_name_input, modify_product_time_time_input
    modify_product_time_name_input = entry_modify_product_time_name.get()
    modify_product_time_time_input = entry_modify_product_time_time.get()
    modify_product_time()

def modify_product_time():
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE FinishedProducts
            SET TimeToMake = interval %s
            WHERE Name = %s;
            """,
            (
                modify_product_time_time_input,
                modify_product_time_name_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Estimated time to make a product has been successfully updated!")
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def modify_customer_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Modify Customer Details", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = [
        "Customer Name",
        "New Phone Number",
        "New Email Address"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_modify_customer_name, entry_modify_customer_phone, entry_modify_customer_email
    entry_modify_customer_name, entry_modify_customer_phone, entry_modify_customer_email = entries

    next_button = tk.Button(form_frame, text="Modify", command=get_customer_details_and_modify, font=button_font, width=20, height=2)
    next_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def get_customer_details_and_modify():
    global modify_customer_name_input, modify_customer_phone_input, modify_customer_email_input
    modify_customer_name_input = entry_modify_customer_name.get()
    modify_customer_phone_input = entry_modify_customer_phone.get()
    modify_customer_email_input = entry_modify_customer_email.get()
    modify_customer()

def modify_customer():
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE Customers
            SET PhoneNumber = %s, EmailAddress = %s
            WHERE Name = %s;
            """,
            (
                modify_customer_phone_input,
                modify_customer_email_input,
                modify_customer_name_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Customer information has been successfully updated!")
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_data_options():
    clear_window(root)

    delete_data_text = tk.Label(root, text="What data do you want to delete?", font=title_font, bg='powderblue')
    delete_data_text.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    yarn_button = tk.Button(root, text="Yarn", command=delete_yarn_details, font=button_font, width=35, height=2)
    yarn_button.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    safety_eyes_button = tk.Button(root, text="Safety Eyes", command=delete_eyes_details, font=button_font, width=35, height=2)
    safety_eyes_button.place(relx=0.5, rely=0.19, anchor=tk.CENTER)

    stuffing_button = tk.Button(root, text="Stuffing", command=delete_stuffing_details, font=button_font, width=35, height=2)
    stuffing_button.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

    products_button = tk.Button(root, text="Products", command=delete_product_details, font=button_font, width=35, height=2)
    products_button.place(relx=0.5, rely=0.33, anchor=tk.CENTER)

    product_material_button = tk.Button(root, text="Material for a Product", command=delete_product_material_name, font=button_font, width=35, height=2)
    product_material_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    customer_button = tk.Button(root, text="Customer", command=delete_customer_name, font=button_font, width=35, height=2)
    customer_button.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

    order_button = tk.Button(root, text="Order", command=delete_order_details, font=button_font, width=35, height=2)
    order_button.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_yarn_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each yarn attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Yarn Details to Delete", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Brand:", "Fiber Type:", "Fiber Weight:", "Color:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_yarn_brand, entry_delete_yarn_fiber_type, entry_delete_yarn_fiber_weight, entry_delete_yarn_color
    entry_delete_yarn_brand, entry_delete_yarn_fiber_type, entry_delete_yarn_fiber_weight, entry_delete_yarn_color = entries

    delete_button = tk.Button(form_frame, text="Delete Yarn", command=delete_yarn, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_yarn():
    global delete_yarn_brand_input, delete_yarn_fiber_type_input, delete_yarn_fiber_weight_input, delete_yarn_color_input
    delete_yarn_brand_input = entry_delete_yarn_brand.get()
    delete_yarn_fiber_type_input = entry_delete_yarn_fiber_type.get()
    delete_yarn_fiber_weight_input = entry_delete_yarn_fiber_weight.get()
    delete_yarn_color_input = entry_delete_yarn_color.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM yarn
            WHERE brand = %s AND fibertype = %s AND fiberweight = %s AND color = %s;
            """,
            (
                delete_yarn_brand_input,
                delete_yarn_fiber_type_input,
                delete_yarn_fiber_weight_input,
                delete_yarn_color_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Yarn has been successfully deleted!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_eyes_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each safety eyes attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Safety Eyes Details to Delete", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Size (mm):", "Color:", "Shape:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_eyes_size, entry_delete_eyes_color, entry_delete_eyes_shape
    entry_delete_eyes_size, entry_delete_eyes_color, entry_delete_eyes_shape = entries

    delete_button = tk.Button(form_frame, text="Delete Safety Eyes", command=delete_eyes, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_eyes():
    global delete_eyes_size_input, delete_eyes_color_input, delete_eyes_shape_input
    delete_eyes_size_input = entry_delete_eyes_size.get()
    delete_eyes_color_input = entry_delete_eyes_color.get()
    delete_eyes_shape_input = entry_delete_eyes_shape.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM safetyeyes
            WHERE sizeinmm = %s AND color = %s AND shape = %s;
            """,
            (
                delete_eyes_size_input,
                delete_eyes_color_input,
                delete_eyes_shape_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Safety eyes have been successfully deleted!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()


def delete_stuffing_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each stuffing attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Stuffing Details to Delete", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Brand:", "Type:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_stuffing_brand, entry_delete_stuffing_type
    entry_delete_stuffing_brand, entry_delete_stuffing_type = entries

    delete_button = tk.Button(form_frame, text="Delete Stuffing", command=delete_stuffing, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_stuffing():
    global delete_stuffing_brand_input, delete_stuffing_type_input
    delete_stuffing_brand_input = entry_delete_stuffing_brand.get()
    delete_stuffing_type_input = entry_delete_stuffing_type.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM stuffing
            WHERE brand = %s AND type = %s;
            """,
            (
                delete_stuffing_brand_input,
                delete_stuffing_type_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Stuffing has been successfully deleted!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_product_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for the product name inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Product Name to Delete", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    label_product_name = tk.Label(form_frame, text="Product Name:", font=button_font, bg='powderblue')
    label_product_name.pack(pady=5)

    global entry_delete_product_name
    entry_delete_product_name = tk.Entry(form_frame, width=30, font=button_font)
    entry_delete_product_name.pack(pady=5)

    delete_button = tk.Button(form_frame, text="Delete Product", command=delete_product, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_product():
    global delete_product_name_input
    delete_product_name_input = entry_delete_product_name.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM finishedproducts
            WHERE name = %s
            """,
            (
                delete_product_name_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Product has been successfully deleted!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_product_material_name():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="What is the name of the product that has the material you want to delete?", font=title_font, bg='powderblue')
    look_at_data_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    global entry_delete_product_material_name
    entry_delete_product_material_name = tk.Entry(root, width=30)
    entry_delete_product_material_name.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    next_button = tk.Button(root, text="Next", command=delete_product_material_type, font=button_font, width=5, height=1)
    next_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_product_material_type():
    global delete_product_material_name_input
    delete_product_material_name_input = entry_delete_product_material_name.get()
    clear_window(root)

    # Title label
    title_label = tk.Label(root, text="Select the Material Type to Delete", font=title_font, bg='powderblue')
    title_label.pack(pady=20)

    # Frame for buttons
    button_frame = tk.Frame(root, bg='powderblue')
    button_frame.pack(pady=20)

    # Buttons for material types
    yarn_button = tk.Button(button_frame, text="Yarn", command=delete_product_material_yarn_details,
                            font=button_font, width=20, height=2)
    yarn_button.pack(pady=10)

    safety_eyes_button = tk.Button(button_frame, text="Safety Eyes",
                                   command=delete_product_material_eyes_details, font=button_font, width=20,
                                   height=2)
    safety_eyes_button.pack(pady=10)

    stuffing_button = tk.Button(button_frame, text="Stuffing", command=delete_product_material_stuffing_details,
                                font=button_font, width=20, height=2)
    stuffing_button.pack(pady=10)

    # Back to start button
    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_product_material_yarn_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each yarn attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Yarn Details to Delete from Product", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Brand:", "Fiber Type:", "Fiber Weight:", "Color:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_product_material_yarn_brand, entry_delete_product_material_yarn_fiber_type
    global entry_delete_product_material_yarn_fiber_weight, entry_delete_product_material_yarn_color
    entry_delete_product_material_yarn_brand, entry_delete_product_material_yarn_fiber_type = entries[:2]
    entry_delete_product_material_yarn_fiber_weight, entry_delete_product_material_yarn_color = entries[2:]

    delete_button = tk.Button(form_frame, text="Delete Yarn", command=delete_product_material_yarn, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_product_material_yarn():
    global delete_product_material_yarn_brand_input, delete_product_material_yarn_fiber_type_input
    global delete_product_material_yarn_fiber_weight_input, delete_product_material_yarn_color_input
    delete_product_material_yarn_brand_input = entry_delete_product_material_yarn_brand.get()
    delete_product_material_yarn_fiber_type_input = entry_delete_product_material_yarn_fiber_type.get()
    delete_product_material_yarn_fiber_weight_input = entry_delete_product_material_yarn_fiber_weight.get()
    delete_product_material_yarn_color_input = entry_delete_product_material_yarn_color.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get FinishedProductsID
        cur.execute(
            "SELECT FinishedProductsID FROM FinishedProducts WHERE Name = %s",
            (delete_product_material_name_input,)
        )
        finished_product_id = cur.fetchone()
        if finished_product_id is None:
            messagebox.showerror("Error", "Finished product not found!")
            return
        finished_product_id = finished_product_id[0]

        # Get MaterialID for Yarn
        cur.execute(
            """
            SELECT YarnID FROM Yarn 
            WHERE Brand = %s AND Color = %s AND FiberType = %s AND FiberWeight = %s
            """,
            (
                delete_product_material_yarn_brand_input,
                delete_product_material_yarn_color_input,
                delete_product_material_yarn_fiber_type_input,
                delete_product_material_yarn_fiber_weight_input,
            )
        )
        material_id = cur.fetchone()
        if material_id is None:
            messagebox.showerror("Error", "Material not found!")
            return
        material_id = material_id[0]

        # Delete FinishedProductMaterials
        cur.execute(
            """
            DELETE FROM FinishedProductMaterials 
            WHERE finishedproductsid = %s AND materialtype = 'Yarn' AND materialid = %s
            """,
            (finished_product_id, material_id,)
        )
        conn.commit()
        messagebox.showinfo("Success", "Material has been successfully deleted from the finished product!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_product_material_eyes_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each safety eye attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Safety Eyes Details to Delete from Product", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Size in MM:", "Color:", "Shape:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_product_material_eyes_size, entry_delete_product_material_eyes_color
    global entry_delete_product_material_eyes_shape
    entry_delete_product_material_eyes_size, entry_delete_product_material_eyes_color, entry_delete_product_material_eyes_shape = entries

    delete_button = tk.Button(form_frame, text="Delete Safety Eyes", command=delete_product_material_eyes, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_product_material_eyes():
    global delete_product_material_eyes_size_input, delete_product_material_eyes_color_input
    global delete_product_material_eyes_shape_input
    delete_product_material_eyes_size_input = entry_delete_product_material_eyes_size.get()
    delete_product_material_eyes_color_input = entry_delete_product_material_eyes_color.get()
    delete_product_material_eyes_shape_input = entry_delete_product_material_eyes_shape.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get FinishedProductsID
        cur.execute(
            "SELECT FinishedProductsID FROM FinishedProducts WHERE Name = %s",
            (delete_product_material_name_input,)
        )
        finished_product_id = cur.fetchone()
        if finished_product_id is None:
            messagebox.showerror("Error", "Finished product not found!")
            return
        finished_product_id = finished_product_id[0]

        # Get MaterialID for Safety Eyes
        cur.execute(
            """
            SELECT SafetyEyesID FROM SafetyEyes
            WHERE SizeInMM = %s AND Color = %s AND Shape = %s
            """,
            (
                delete_product_material_eyes_size_input,
                delete_product_material_eyes_color_input,
                delete_product_material_eyes_shape_input,
            )
        )
        material_id = cur.fetchone()
        if material_id is None:
            messagebox.showerror("Error", "Material not found!")
            return
        material_id = material_id[0]

        # Delete FinishedProductMaterials
        cur.execute(
            """
            DELETE FROM FinishedProductMaterials 
            WHERE finishedproductsid = %s AND materialtype = 'Safety Eyes' AND materialid = %s
            """,
            (finished_product_id, material_id,)
        )
        conn.commit()
        messagebox.showinfo("Success", "Material has been successfully deleted from the finished product!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_product_material_stuffing_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for each stuffing attribute inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Stuffing Details to Delete from Product", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Brand:", "Type:"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_product_material_stuffing_brand, entry_delete_product_material_stuffing_type
    entry_delete_product_material_stuffing_brand, entry_delete_product_material_stuffing_type = entries

    delete_button = tk.Button(form_frame, text="Delete Stuffing", command=delete_product_material_stuffing, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_product_material_stuffing():
    global delete_product_material_stuffing_brand_input, delete_product_material_stuffing_type_input
    delete_product_material_stuffing_brand_input = entry_delete_product_material_stuffing_brand.get()
    delete_product_material_stuffing_type_input = entry_delete_product_material_stuffing_type.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get FinishedProductsID
        cur.execute(
            "SELECT FinishedProductsID FROM FinishedProducts WHERE Name = %s",
            (delete_product_material_name_input,)
        )
        finished_product_id = cur.fetchone()
        if finished_product_id is None:
            messagebox.showerror("Error", "Finished product not found!")
            return
        finished_product_id = finished_product_id[0]

        # Get MaterialID for Stuffing
        cur.execute(
            """
            SELECT StuffingID FROM Stuffing
            WHERE Brand = %s AND Type = %s
            """,
            (
                delete_product_material_stuffing_brand_input,
                delete_product_material_stuffing_type_input,
            )
        )
        material_id = cur.fetchone()
        if material_id is None:
            messagebox.showerror("Error", "Material not found!")
            return
        material_id = material_id[0]

        # Delete FinishedProductMaterials
        cur.execute(
            """
            DELETE FROM FinishedProductMaterials 
            WHERE finishedproductsid = %s AND materialtype = 'Stuffing' AND materialid = %s
            """,
            (finished_product_id, material_id,)
        )
        conn.commit()
        messagebox.showinfo("Success", "Material has been successfully deleted from the finished product!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_customer_name():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place label and entry field for customer name inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Customer Name to Delete", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    label = tk.Label(form_frame, text="Customer Name:", font=button_font, bg='powderblue')
    label.pack(pady=5)

    global entry_delete_customer_name
    entry_delete_customer_name = tk.Entry(form_frame, width=30, font=button_font)
    entry_delete_customer_name.pack(pady=5)

    delete_button = tk.Button(form_frame, text="Delete Customer", command=delete_customer, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_customer():
    global delete_customer_name_input
    delete_customer_name_input = entry_delete_customer_name.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM customers
            WHERE name = %s
            """,
            (delete_customer_name_input,)
        )
        conn.commit()
        messagebox.showinfo("Success", "Customer has been successfully deleted!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

def delete_order_details():
    clear_window(root)

    # Create a Canvas widget
    canvas = tk.Canvas(root, bg='powderblue')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    form_frame = tk.Frame(canvas, bg='powderblue')
    canvas.create_window((root.winfo_width()/2, 0), window=form_frame, anchor='n')

    # Create and place labels and entry fields for customer name and order date inside the form_frame
    title_label = tk.Label(form_frame, text="Enter Customer Name and Order Date to Delete Order", font=title_font, bg='powderblue')
    title_label.pack(pady=10)

    labels_texts = ["Customer Name:", "Order Date (YYYY-MM-DD):"]
    entries = []

    for text in labels_texts:
        label = tk.Label(form_frame, text=text, font=button_font, bg='powderblue')
        label.pack(pady=5)

        entry = tk.Entry(form_frame, width=30, font=button_font)
        entry.pack(pady=5)
        entries.append(entry)

    # Store the entries in global variables
    global entry_delete_order_name, entry_delete_order_date
    entry_delete_order_name, entry_delete_order_date = entries

    delete_button = tk.Button(form_frame, text="Delete Order", command=delete_order, font=button_font, width=20, height=2)
    delete_button.pack(pady=20)

    back_to_start_button = tk.Button(root, text="Back to Start", command=start_up, font=button_font, width=15, height=2)
    back_to_start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def delete_order():
    global delete_order_name_input, delete_order_date_input
    delete_order_name_input = entry_delete_order_name.get()
    delete_order_date_input = entry_delete_order_date.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Get the CustomerID
        cur.execute(
            """
            SELECT CustomerID FROM Customers WHERE Name = %s;
            """,
            (delete_order_name_input,)
        )
        customer_id = cur.fetchone()
        if not customer_id:
            raise ValueError("Customer not found")
        customer_id = customer_id[0]

        # Get the OrderID
        cur.execute(
            """
            SELECT OrderID FROM Orders WHERE CustomerID = %s AND OrderDate::date = %s::date;
            """,
            (customer_id, delete_order_date_input,)
        )
        order_id = cur.fetchone()
        if not order_id:
            raise ValueError("Order not found")
        order_id = order_id[0]

        # Delete from OrderProducts
        cur.execute(
            """
            DELETE FROM OrderProducts WHERE OrderID = %s;
            """,
            (order_id,)
        )

        # Delete from Orders
        cur.execute(
            """
            DELETE FROM Orders WHERE OrderID = %s;
            """,
            (order_id,)
        )

        # Optionally, update CustomerPurchases
        cur.execute(
            """
            DELETE FROM CustomerPurchases WHERE CustomerID = %s AND FinishedProductsID IN (
                SELECT FinishedProductsID FROM OrderProducts WHERE OrderID = %s
            );
            """,
            (customer_id, order_id)
        )

        conn.commit()
        messagebox.showinfo("Success", "Order has been successfully deleted!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
        start_up()

# Create main window
root = tk.Tk()
root.title("Jazmine's Yarn Database")

# Change the background color of the main window
root.configure(bg='powderblue')

# Call start_up to set up GUI components
start_up()

# Start the GUI event loop
root.mainloop()
