class Pojistenec:
    """
    Třída reprezentuje pojištěnou osobu
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Vytváří instanci pojištěnce s parametry:
        :param jmeno: jméno pojištěného - str
        :param prijmeni: příjmení pojištěného - str
        :param vek: věk pojištěného - int
        :param telefon: telefon pojištěného - str
        """
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._telefon = telefon

    def __str__(self):
        """
        Vrací naformátované údaje o pojištěném
        """
        return f"{self._jmeno:<15}\t{self._prijmeni:<15}\t{self._vek:<5}\t{self._telefon}"

    @property
    def jmeno(self):
        return self._jmeno

    @property
    def prijmeni(self):
        return self._prijmeni
