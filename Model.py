class Handphone:
    def __init__(self, id_hp, nama, harga, ram, storage, rating):
        self.id = id_hp
        self.nama = nama
        self.harga = harga        
        self.ram = ram            
        self.storage = storage
        self.rating = rating      

    def __str__(self):
        return f"{self.nama} (RAM: {self.ram}GB) - Rp{self.harga:,} [★{self.rating}]"
