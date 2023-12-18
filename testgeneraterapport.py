#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:27:18 2023

@author: jngouna
"""

# from reportlab.pdfgen import canvas

# def create_pdf(file_path, lines):
#     # Créez un nouveau fichier PDF
#     pdf_canvas = canvas.Canvas(file_path)

#     # Ajoutez du texte à chaque ligne
#     for i, line in enumerate(lines):
#         y_position = 800 - i * 12  # Ajustez la position verticale selon vos besoins
#         pdf_canvas.drawString(100, y_position, line)

#     # Enregistrez le fichier PDF
#     pdf_canvas.save()

# # Exemple d'utilisation
# lines_of_text = ["Première ligne", "Deuxième ligne", "Troisième ligne"]
# create_pdf("nouveau_fichier.pdf", lines_of_text) 






from ebooklib import epub

def add_lines_to_epub(file_path, lines):
    # Chargez le fichier EPUB existant
    book = epub.read_epub(file_path)

    # Ajoutez une nouvelle page avec les lignes spécifiées
    new_page = epub.EpubHtml(title='Nouvelle Page', file_name='new_page.xhtml', lang='en')
    new_page.content = "<h1>Nouvelle Page</h1><p>" + "<br>".join(lines) + "</p>"

    # Ajoutez la nouvelle page au livre
    book.add_item(new_page)

    # Ajoutez la nouvelle page au tableau des contenus
    book.toc.append(epub.Link('new_page.xhtml', 'Nouvelle Page', 'intro'))

    # Écrivez le fichier EPUB mis à jour
    epub.write_epub(file_path, book)

# Exemple d'utilisation
lines_of_text = ["Première ligne", "Deuxième ligne", "Troisième ligne"]
add_lines_to_epub("/users/2024/ds1/123010405/Bureau/Projet_POO", lines_of_text)





from ebooklib import epub
from datetime import datetime

book = epub.EpubBook("/users/2024/ds1/123010405/Bureau/Projet_POO")

book.set_title("Mon Livre")
book.set_language("fr")
book.set_identifier("123456")
book.add_author("John Doe")
book.set_description("Description de mon livre.")
book.set_publisher("Ma maison d'édition")
book.set_cover("cover.jpg", open("cover.jpg", "rb").read())
book.set_pubdate(datetime(2023, 1, 1))

# ... ajoutez d'autres options selon vos besoins ...

# Écrivez le fichier EPUB
epub.write_epub("mon_livre.epub", book, {})