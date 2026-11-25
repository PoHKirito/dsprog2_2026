# データサイエンスプログラミング演習Ⅱ

第1回の個人課題は `lesson1` にあります。

## 第1回 科学電卓

Python 3.13 と uv を使用します。リポジトリのルートで実行してください。

```bash
uv sync --locked
uv run flet run lesson1/main.py
```

「科学計算モード」をオンにすると、sin、cos、tan、平方、平方根、10 の累乗、常用対数、自然対数を使用できます。数値を入力してから関数のボタンを押します。三角関数は度数法（DEG）です。

- `30 → sin` は `0.5`
- `1000 → log₁₀` は `3`
- `2 → + → 9 → √x → =` は `5`

ゼロ除算や定義域外の入力は「エラー」と表示されます。AC または新しい数値の入力で計算をやり直せます。

参考：[Flet Calculator Tutorial](https://flet.dev/docs/tutorials/calculator/)
