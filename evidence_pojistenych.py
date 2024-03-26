class EvidencePojistenych:
    """
    Třída reprezentuje databázi pojištěných osob
    """

    def __init__(self):
        self._pojisteni = []

    def __str__(self):
        return "Databáze pojištěných osob"

    def pridej_pojisteneho(self, pojisteny):
        """
        Přidá pojištěného do databáze
        """
        self._pojisteni.append(pojisteny)

    def vrat_pojisteneho(self, jmeno, prijmeni):
        """
        Vyhledá a vrátí list pojištěných se zadaným jménem a příjmením,
        prázný list pokud nikoho se shodou nenajde
        """
        vyhledani_pojisteni = []
        for pojisteny in self._pojisteni:
            if jmeno == pojisteny.jmeno and prijmeni == pojisteny.prijmeni:
                vyhledani_pojisteni.append(pojisteny)
        return vyhledani_pojisteni

    def vrat_vsechny_pojistene(self):
        """
        Vrátí všechny pojištěné v evidenci pojištěných.
        """
        return self._pojisteni
