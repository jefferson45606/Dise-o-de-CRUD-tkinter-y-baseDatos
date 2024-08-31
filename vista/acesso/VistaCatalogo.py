import tkinter as tk

def menu():
  root =tk.Tk()
  root.title("Menú de opciones")
  root.geometry("600x400")
  root.configure(bg="#b9f1d6")
  
  main_frame = tk.Frame(root, padx=10, pady=10, bg="#b9f1d6")
  main_frame.pack(expand=True, fill= 'both')
  
  label_font= ("")
  
  tk.Button(button_frame, text="Salir", command=root.destroy, **button_style).pack(padx=5, pady=5)

  root.mainloop()

menu()