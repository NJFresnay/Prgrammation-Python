#!/bin/env python

import base_livre,base_bibli


#pdf_path = "/users/2024/ds1/123010405/Bureau/Projet_POO/cervantes_don_quichotte_2.pdf"
# pdf_path = "/users/2024/ds1/123010405/Bureau/Projet_POO/about_a_b_c_du_travailleur.pdf"
# #pdf_path = "https://math.univ-angers.fr/~jaclin/biblio/livres/balzac_seraphita.pdf"
# pdf = base_livre.PDF(pdf_path)


print()

epub_path1 = "/users/2024/ds1/123010405/Bureau/Projet_POO/bronte_anne_-_agnes_grey.epub"
epub1 = base_livre.EPUB(epub_path1)

#print(epub1.auteur())
#print(epub1.type())
print()

# epub_path = "/users/2024/ds1/123010405/Bureau/Projet_POO/bronte_anne_-_agnes_grey.epub"
# un_epub = base_livre.EPUB(epub_path)
#print(un_epub.titre())

# ma_bibli = base_bibli.base_bibli("/users/2024/ds1/123010405/Bureau/Projet_POO/Ma_bibliotheque")
# #ma_bibli.ajouter(pdf)
# print()
# ma_bibli.ajouter(epub1)
print()
# ma_bibli.ajouter(un_pdf1)


simple_bibli = base_bibli.simple_bibli("/users/2024/ds1/123010405/Bureau/Projet_POO/Ma_bibliotheque")
#simple_bibli.rapport_livres("PDF","Mon rapport1.pdf")
# simple_bibli.rapport_livres("EPUB","Mon rapport1.epub")
# print(simple_bibli._generer_contenu_html1())

simple_bibli.rapport_auteurs("PDF","Mon rapport1.pdf")

if __name__== "__main__":
    pass
