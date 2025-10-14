from pico2d import load_image
from state_machine import StateMachine


class Idle:
    def __init__(self, boy):
        self.boy = boy

    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        self.boy.frame = (self.boy.frame + 1) % 8

    def draw(self):
        if self.boy.face_dir == 1:
            self.boy.image.clip_draw(self.boy.frame * 100, 300, 100, 100, self.boy.x, self.boy.y)
        else:
            self.boy.image.clip_draw(self.boy.frame * 100, 200, 100, 100, self.boy.x, self.boy.y)

class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')

        self.IDLE = Idle(self)
        self.state_machine = StateMachine(self.IDLE) #상태 머신 설정 및 초기 시작 상태 초기화

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()