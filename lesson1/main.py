import math
import operator

import flet as ft


BINARY = {
    "+": operator.add,
    "−": operator.sub,
    "×": operator.mul,
    "÷": operator.truediv,
}
def tangent_degrees(value):
    if abs(math.remainder(value, 180)) == 90:
        raise ValueError("Undefined tangent")
    return math.tan(math.radians(value))


SCIENTIFIC = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": tangent_degrees,
    "x²": lambda x: x ** 2,
    "√x": math.sqrt,
    "10ˣ": lambda x: 10 ** x,
    "log₁₀": math.log10,
    "ln": math.log,
}

BASIC_UNARY = {"±": operator.neg, "%": lambda x: x / 100}


class Calculator:
    def __init__(self):
        self.clear()

    def clear(self):
        self.display = "0"
        self.left = None
        self.operation = None
        self.fresh = True
        self.waiting = False

    def show(self, value):
        if not math.isfinite(value):
            raise ValueError("Non-finite result")
        self.display = format(value or 0, ".15g")
        self.fresh = True
        self.waiting = False

    def press(self, key):
        if key == "AC":
            self.clear()
            return

        if self.display == "エラー":
            if key not in "0123456789.":
                return
            self.clear()

        try:
            if key in "0123456789.":
                if self.fresh:
                    self.display = "0"
                if key == ".":
                    if "." not in self.display:
                        self.display += "."
                elif len(self.display) < 16:
                    self.display = key if self.display == "0" else self.display + key
                self.fresh = self.waiting = False
            elif key in BINARY or key == "=":
                if self.operation is not None and not self.waiting:
                    self.show(BINARY[self.operation](self.left, float(self.display)))
                self.operation = key if key in BINARY else None
                self.left = float(self.display) if self.operation else None
                self.waiting = self.operation is not None
                self.fresh = True
            elif key in BASIC_UNARY or key in SCIENTIFIC:
                if not self.waiting:
                    operation = (BASIC_UNARY | SCIENTIFIC)[key]
                    self.show(operation(float(self.display)))
        except (ArithmeticError, ValueError):
            self.clear()
            self.display = "エラー"


def main(page: ft.Page):
    page.title = "Flet 電卓"
    page.padding = 20
    page.window.width = 430
    page.window.height = 640
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    calculator = Calculator()
    display = ft.Text("0", size=30, color=ft.Colors.WHITE, text_align=ft.TextAlign.RIGHT)

    def press(event):
        calculator.press(event.control.data)
        display.value = calculator.display

    def keys(labels, color):
        return ft.Row([
            ft.Button(label, data=label, on_click=press, expand=True,
                      color=ft.Colors.WHITE, bgcolor=color, height=48)
            for label in labels
        ])

    keypad = [
        keys(row, "#293E56")
        for row in [
            ("AC", "±", "%", "÷"),
            ("7", "8", "9", "×"),
            ("4", "5", "6", "−"),
            ("1", "2", "3", "+"),
            ("0", ".", "="),
        ]
    ]
    scientific = ft.Column([
        ft.Text("三角関数は度数法（DEG）", color="#C5EDE9"),
        keys(("sin", "cos", "tan", "x²"), "#155D63"),
        keys(("√x", "10ˣ", "log₁₀", "ln"), "#155D63"),
    ], visible=False)

    def toggle_mode(event):
        scientific.visible = event.control.value

    page.add(ft.Container(
        width=390,
        padding=16,
        bgcolor="#122338",
        border_radius=16,
        content=ft.Column([
            ft.Text("電卓", size=20, color=ft.Colors.WHITE),
            ft.Container(display, padding=12, bgcolor="#172E46",
                         border_radius=8, alignment=ft.Alignment.CENTER_RIGHT),
            ft.Switch(label=ft.Text("科学計算モード", color=ft.Colors.WHITE),
                      on_change=toggle_mode),
            scientific,
            *keypad,
        ]),
    ))


if __name__ == "__main__":
    ft.run(main)
