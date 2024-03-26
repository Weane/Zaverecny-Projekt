from pojistenec import Pojistenec
from evidence_pojistenych import EvidencePojistenych


class UzivatelskeRozhrani:
    """
    Třida uživatelského rozhraní pro výpis a čtení z konzole
    """

    def __init__(self):
        self._evidence = EvidencePojistenych()

    def vytvor_pojisteneho(self):
        """
        Načte ůdaje a vytvoří pojištěného, pokud jsou zadány všechny hodnoty a přidá ho do databáze,
        případně vypíše chybu do konzole.
        """
        try:
            jmeno = self._nacti_vstup("Zadej jméno pojištěného: ", "jméno").capitalize()
            prijmeni = self._nacti_vstup("Zadej příjmení pojištěného: ", "příjmení").capitalize()
            vek = int(self._nacti_vstup("Zadej věk pojištěného: ", "věk", kontrola_cisla=True))
            telefon = self._nacti_vstup("Zadej telefonní číslo pojištěného: ", "telefonní číslo")
            pojisteny = Pojistenec(jmeno, prijmeni, vek, telefon)
            self._evidence.pridej_pojisteneho(pojisteny)
            print("\nZáznam přidán. Pokračuj stisknutím ENTER")
            input()
        except ValueError as chyba_vstupu:
            print(f"\nZáznam nebyl přidán. {chyba_vstupu} Pokračuj stisknutím ENTER")
            input()

    def vypis_vsechny_pojistene(self):
        """
        Vytiskne celou databázi pojištěných
        """
        self.vytisni_pojistene(self._evidence.vrat_vsechny_pojistene())

    def hledej_pojistene(self):
        """
        Načte jméno a příjmení pojištěného a vypíše všechny záznamy, které mají shodné zadané jméno i příjmení,
        případně vypíše do konzole, že záznam nenalezl.
        """
        jmeno = input("Zadej jméno pojištěného: ").capitalize()
        prijmeni = input("Zadej příjmení pojištěného: ").capitalize()
        print()
        hledani_pojisteni = self._evidence.vrat_pojisteneho(jmeno, prijmeni)
        self.vytisni_pojistene(hledani_pojisteni)

    def vytisni_pojistene(self, pojisteni):
        """
        Vytiskne do konzole pojištěné předané jako seznam.
        """
        if pojisteni:
            for pojisteny in pojisteni:
                print(pojisteny)
        else:
            print("Žádný pojištěný nebyl nalezen.")

        print("\nPokračuj stisknutím ENTER")
        input()

    def _vypis_volby(self):
        """
        Vypíše text pro volbu operace s databází
        """
        print("-----------------------\n"
              "Evidence pojištěných\n"
              "-----------------------\n\n"
              "Vyberte akci:\n"
              "1 - Přidat nového pojištěného\n"
              "2 - Vyhledat pojištěného\n"
              "3 - Vypsat všechny pojištěné\n"
              "4 - Konec\n")

    def nacti_volbu(self):
        """
        Načte volbu, pokud je správná (1-4) vrátí jí, jinak vypíše chybu.
        """
        self._vypis_volby()
        vstup = input().strip()
        try:
            volba = int(vstup)
            if 1 <= volba <= 4:
                return volba
            else:
                raise ValueError
        except ValueError:
            print("Neplatná volba. Pokračuj stisknutím ENTER")
            input()

    def _nacti_vstup(self, zprava, jmeno_parametru, kontrola_cisla=False):
        """
        Načte a zkontroluje vstup, jestli není prázdný, pokud je vrací chybu
        :param zprava: Zpráva pro načtení vstupu
        :param jmeno_parametru: jméno parametru, který načítáme
        :param kontrola_cisla: Nastavený na True, kontroluje vstup, je-li číslo a vrací chybu pokud není
        """
        vstup = input(zprava).strip()
        if not vstup:
            raise ValueError(f"Hodnota pro {jmeno_parametru} musí být zadána.")
        if kontrola_cisla and not vstup.isdigit():
            raise ValueError(f"Hodnota pro {jmeno_parametru} musí být číslo.")
        return vstup

    def run(self):
        """
        Načítá a obsluhuje volbu.
        """
        volba = 0

        while volba != 4:
            volba = self.nacti_volbu()
            match volba:
                case 1:
                    self.vytvor_pojisteneho()
                case 2:
                    self.hledej_pojistene()
                case 3:
                    self.vypis_vsechny_pojistene()
