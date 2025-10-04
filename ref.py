from enum import Enum
from typing import Tuple
import random
random.seed(114514)

class Facing(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Grid:
    def __init__(self):
        self.width: int = 5
        self.height: int = 5
        self.current_pos: Tuple[int, int] = (0, 0)
        self.current_direction: Facing = Facing.UP
        # 敌人随机生成（保证不在 (0,0)）
        while True:
            x, y = random.randint(0, self.width), random.randint(0, self.height)
            if (x, y) != (0, 0):
                self.enemy_pos: Tuple[int, int] = (x, y)
                break

    # ===================== Question 1 =====================
    def move_forward(self) -> Tuple[int, int]:
        '''
        让机器人向当前方向前进一格
        返回新的坐标 (x, y)
        要求：
          - 不能走出边界 [0, width] [0, height]
          - 更新 self.current_pos
        '''
        x, y = self.current_pos
        if self.current_direction == Facing.UP:
            y = min(self.height, y + 1)
        elif self.current_direction == Facing.DOWN:
            y = max(0, y - 1)
        elif self.current_direction == Facing.RIGHT:
            x = min(self.width, x + 1)
        elif self.current_direction == Facing.LEFT:
            x = max(0, x - 1)

        self.current_pos = (x, y)
        return self.current_pos
    # ===================== End Q1 =====================

    # ===================== Question 2 =====================
    def turn_left(self) -> Facing:
        '''
        让机器人逆时针转向，返回新方向
        '''
        value = (self.current_direction.value + 1) % 4
        self.current_direction = Facing(value)
        return self.current_direction

    def turn_right(self) -> Facing:
        '''
        让机器人顺时针转向，返回新方向
        '''
        value = (self.current_direction.value - 1) % 4
        self.current_direction = Facing(value)
        return self.current_direction
    # ===================== End Q2 =====================

    # ===================== Question 3 (稍难) =====================
    def find_enemy(self) -> bool:
        '''
        判断当前是否到达敌人位置。
        若到达敌人位置，返回 True，否则 False。
        '''
        return self.current_pos == self.enemy_pos
    # ===================== End Q3 =====================

    # ===================== Question 4 =====================
    def patrol_around(self, steps: int) -> int:
        '''
        机器人随机移动 steps 步。
        若过程中遇到敌人，立即停止并返回遇敌时的步数。
        若未遇敌，返回 -1。
        提示：
          - 每步随机选择 turn_left、turn_right 或 move_forward。
        '''
        for i in range(1, steps + 1):
            action = random.choice(["L", "R", "M"])
            if action == "L":
                self.turn_left()
            elif action == "R":
                self.turn_right()
            else:
                self.move_forward()
            if self.find_enemy():
                return i
        return -1
    # ===================== End Q4 =====================