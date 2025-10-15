class Gun:
    def __init__(self, color, recoil):
        self.color = color
        self.recoil = recoil

    def __str__(self):
        return (f"Color is {self.color} "
                f"and recoil is {self.recoil}")

newGun = Gun("Black", 4)
print(newGun)
