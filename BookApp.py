#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:12:24 2018

@author: chris
"""

import tkinter as tk

from tkinter import ttk
from BookAndInventory import Inventory
from BookAndInventory import Book
from BookAndInventory import InventoryItem



class BookApp(tk.Frame):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Book Inventory')
        
        TopFrame = tk.Frame(app,bg = 'purple', width = 900, height = 100, relief = 'flat')
        TopFrame.pack(side= tk.TOP)
        
        
        MidLeftFrame = tk.Frame(app, width = 200,bd = 14, relief = 'raise')
        MidLeftFrame.pack(side = tk.LEFT)
        
        MidRightFrame = tk.Frame(app, width = 750,bd = 14, relief = 'raise')
        MidRightFrame.pack(side = tk.RIGHT)
        
        self.BookTree = ttk.Treeview(MidRightFrame,column = ('column1','column2'),show = 'headings')
        self.BookTree.heading('#1',text = 'Title')
        self.BookTree.heading('#2',text = 'Author')
        self.BookTree.pack(side = tk.RIGHT)
        
        self.name = tk.StringVar()
        self.name.set('')
        
        self.author = tk.StringVar()
        self.author.set('')
        
        AppTitle = tk.Label(TopFrame ,font = ('arial',15, 'bold'),text = 'BOOK INVENTORY APP', relief = 'raise')
        AppTitle.grid(row = 3)
        #name entry group
        name_label = tk.Label(MidLeftFrame,font = ('arial',10,'bold'), text = 'Enter Book Title',
                              fg = 'blue', bd = 10 )
        name_label.grid(row = 1, column = 1)
        
        name_entry = tk.Entry(MidLeftFrame,textvariable = self.name, bd = 10, width =40)
        name_entry.grid(row = 2, column = 1)
        
        #author entry group
        author_label = tk.Label(MidLeftFrame,font = ('arial',10,'bold'),text = 'Enter Author',
                                fg = 'blue',bd = 10)
        author_label.grid(row = 3, column = 1)
        
        author_entry = tk.Entry(MidLeftFrame,textvariable = self.author, bd = 10, width = 40)
        author_entry.grid(row = 4, column = 1)
        
        #all my buttons
        add_button = tk.Button(MidLeftFrame, font = ('arial',10,'bold'),text = 'Add Book',
                               bd = 10, width = 10,relief = 'raise', command = self.Add_book)
        add_button.grid(row = 5, column = 1)
        
        delete_button = tk.Button(MidLeftFrame, font = ('arial',10,'bold'),text = 'Delete Book', 
                                  bd = 10,width = 10, command = self.Delete_book)
        delete_button.grid(row = 5, column = 2)
        
        save_button = tk.Button(MidLeftFrame, font = ('arial',10,'bold'),text = 'Save',
                                bd = 10, width = 10, command = self.Save_book)
        save_button.grid(row = 6, column = 1)
        
        quit_button = tk.Button(MidLeftFrame, font = ('arial',10, 'bold'),text = 'Quit', 
                                bd = 10, width = 10 ,command = self.quit_app)
        quit_button.grid(row = 6, column = 2)
        
        
        
        
    def quit_app(self):
        app.destroy()
    
    def Add_book(self):
        BookTitle = self.name.get()
        AuthorName = self.author.get()
        self.BookTree.insert('','end',values=(BookTitle,AuthorName,''))
        Inventory.add_item(Inventory,BookTitle)
        
     #allows yo to highlight selected item in tree and delete.   
    def Delete_book(self):
        selected_item = self.BookTree.selection()[0] ## get selected item
        self.BookTree.delete(selected_item)
        Inventory.remove_item(Inventory,selected_item)
        
    def Save_book(self):
        
        Inventory.save_item(self,'books.xml')

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("900x300")
    frame = BookApp(app)
    
    
    app.mainloop()
    
        
        