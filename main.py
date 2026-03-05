from dataclasses import dataclass

#5
@dataclass
class Shaxs:
    nom: str
    soni: int
    narx: int

    def umumiy_qiymat(self):
        return self.soni * self.narx
