"""band"""
from musician import Musician
from guitar import Guitar

class Band(Guitar(Musician)):
    """"""

    def __init__(self, band=''):
        """..."""
        self.band = band


    def __str__(self):
        """..."""
        return f"{self.band} ({} ([{}])"

    # def play(self):






"""
Needed
band (str)
Extreme (Nuno Bettencourt ([Washburn N4 (1990) : $2,499.95, Takamine acoustic (1986) : $1,200.00]), Gary Cherone ([]), Pat Badger ([Mouradian CS-74 Bass (2009) : $1,500.00]), Kevin Figueiredo ([]))
band.play()
Nuno Bettencourt is playing: Washburn N4 (1990) : $2,499.95
Gary Cherone needs an instrument!
Pat Badger is playing: Mouradian CS-74 Bass (2009) : $1,500.00
Kevin Figueiredo needs an instrument!
"""