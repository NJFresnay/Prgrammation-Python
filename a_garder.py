class base_bibli:
    def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        # self.path = path
        self.livres = []
        # raise NotImplementedError("à définir dans les sous-classes")

    def ajouter(self,livre):
        """Ajoute le livre à la bibliothèque """
        if isinstance(livre, Base_livre.PDF):
            un_livre = Base_livre.PDF(livre.ressource)
            self.livres.append(un_livre)

        elif isinstance( livre, Base_livre.EPUB):
            un_livre = Base_livre.EPUB(livre.ressource)
            self.livres.append(un_livre)

        #raise NotImplementedError("à définir dans les sous-classes")

    def rapport_livres(self,format,fichier):
        """Génère un état des livres de la bibliothèque.
            Il contient la liste des livres,
            et pour chacun d'eux
            son titre, son auteur, son type (PDF ou EPUB), et le nom du fichier correspondant.

            format: format du rapport (PDF ou EPUB)
            fichier: nom du fichier généré"""

        if format == "PDF":
            self.generer_rapport_pdf(fichier)
        elif format == "EPUB":
            self.generer_rapport_epub(fichier)
        else:
            raise ValueError("Format non traité à ce niveau")

        def generer_rapport_pdf(self, fichier):
            with open(fichier,'w') as pdf_file:
                pdf_file.write("Etat des livres de la bibliothèque")

        def generer_rapport_epub(self,fichier):
            book = epub.EpubBook()
            book.set_title("Etat des livres de la bibliothèque")
            epub.write_epub(fichier, book, {})


    def rapport_auteurs(self,format,fichier):
        """
            Génère un état des auteurs des livres de la bibliothèque.
            Il contient pour chaque auteur
            le titre de ses livres en bibliothèque et le nom du fichier correspondant au livre.
            le type (PDF ou EPUB),
            et le nom du fichier correspondant.

            format: format du rapport (PDF ou EPUB)
            fichier: nom du fichier généré
        """

        if format in ['PDF', 'EPUB']:
            raise ValueError(" Ne sont pris en charge que les formats PDF et EPUB")
