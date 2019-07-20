
class XOX():

    def __init__(self,tahta=[[ " "," "," "],[" "," "," "],[" "," "," "]]):
        self.tahta=tahta


    def tahtayıGoster(self):
        for i in self.tahta:
            print(i)

    def p1secim(self):
        satir=int(input("p1 satır giriniz:"))
        sutun = int(input("p1 sutun giriniz"))
        if self.dolumu(satir-1,sutun-1):
            self.tahta[satir-1][sutun-1] = "X"
        else:
            print("dolu")
            self.p1secim()

    def p2secim(self):
        satir=int(input("p2 satır giriniz:"))
        sutun = int(input("p2 sutun giriniz"))
        if self.dolumu(satir-1, sutun-1):
            self.tahta[satir-1][sutun-1] = "O"
        else:
            print("dolu")
            self.p2secim()
    def dolumu(self,satır,sutun):
        if self.tahta[satır][sutun] == " ":
            return True
        else:
            return False

    def bittimi(self):
        if self.tahta[0][0]=="X" and self.tahta[0][1]=="X" and self.tahta[0][2]=="X":
            return True
        if self.tahta[1][0]=="X" and self.tahta[1][1]=="X" and self.tahta[1][2]=="X":
            return True
        if self.tahta[2][0]=="X" and self.tahta[2][1]=="X" and self.tahta[2][2]=="X":
            return True
        if self.tahta[0][0]=="X" and self.tahta[1][0]=="X" and self.tahta[2][0]=="X":
            return True
        if self.tahta[0][1]=="X" and self.tahta[1][1]=="X" and self.tahta[2][1]=="X":
            return True
        if self.tahta[0][2]=="X" and self.tahta[1][2]=="X" and self.tahta[2][2]=="X":
            return True
        if self.tahta[0][0]=="X" and self.tahta[1][1]=="X" and self.tahta[2][2]=="X":
            return True
        if self.tahta[0][2]=="X" and self.tahta[1][1]=="X" and self.tahta[2][0]=="X":
            return True
        if self.tahta[0][0]=="O" and self.tahta[0][1]=="O" and self.tahta[0][2]=="O":
            return True
        if self.tahta[1][0]=="O" and self.tahta[1][1]=="O" and self.tahta[1][2]=="O":
            return True
        if self.tahta[2][0]=="O" and self.tahta[2][1]=="O" and self.tahta[2][2]=="O":
            return True
        if self.tahta[0][0]=="O" and self.tahta[1][0]=="O" and self.tahta[2][0]=="O":
            return True
        if self.tahta[0][1]=="O" and self.tahta[1][1]=="O" and self.tahta[2][1]=="O":
            return True
        if self.tahta[0][2]=="O" and self.tahta[1][2]=="O" and self.tahta[2][2]=="O":
            return True
        if self.tahta[0][0]=="O" and self.tahta[1][1]=="O" and self.tahta[2][2]=="O":
            return True
        if self.tahta[0][2]=="O" and self.tahta[1][1]=="O" and self.tahta[2][0]=="O":
            return True
        else:
            return False



xox = XOX()


while True:
    xox.tahtayıGoster()
    xox.p1secim()
    xox.tahtayıGoster()
    if xox.bittimi():
        break
    xox.p2secim()
    if xox.bittimi():
        break