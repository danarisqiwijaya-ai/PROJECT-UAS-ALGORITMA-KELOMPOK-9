class Club:
    def __init__(self, id_club, nama, liga, poin):
        self.__id = id_club
        self.__nama = nama
        self.__liga = liga
        self.__poin = poin

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_liga(self):
        return self.__liga

    def get_poin(self):
        return self.__poin

    def set_data(self, nama, liga, poin):
        self.__nama = nama
        self.__liga = liga
        self.__poin = poin

    def tampil(self):
        return f"{self.__id} | {self.__nama} | {self.__liga} | Poin: {self.__poin}")
