import pygame as pg

class RobotChan:
    def __init__(self, job, name, battery):
        self._job = job
        self._name = name
        self._battery = battery
    
    @property
    def job(self):
        return self.job
    @property
    def name(self):
        return self.name
    @property
    def battery(self):
        return self.battery

    @battery.setter
    def battery(self, value):
        if 0<= value <= 100:
            self.battery = value
        else:
            print("【注意】：やる気の値は0〜100にしtください")

    def show_info(self):
        print(f"私は「{self.name}」です。できることは{self.job}です。やる気は{self.battery}％です！")

    def work(self):
        self.battery -= 10
        print(f"{}")


koharu = RobotChan("プログラミング", "こはるちゃん", 100)
noromin = RobotChan("お金を貸すこと", "ノロミン", 3)
koharu.show_info()
noromin.show_info()


