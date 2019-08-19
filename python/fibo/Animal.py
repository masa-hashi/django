class Animal:
    # コンストラクタの定義
    def __init__(self, name):
        self.name = name

    # オブジェクトのメソッドを定義
    def say(self):
        print("こんにちは！　私は" + self.name + "です。")
        