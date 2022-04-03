class ChoiJoonLang:
    def __init__(self):
        self.var = {}

    def calc(self, code):
        codes = code.split("~")
        result = 1
        for code in codes:
            cur = 0
            for letter in code:
                if letter == 'ㅎ':
                    cur -= 1
                elif letter == '흐':
                    cur += 1
            result *= cur
        return result

    def compile_line(self, code):
        codes = code.split(" ")
        if codes[0] == "우리": # 변수 선언
            if len(codes) > 2:
                self.var[codes[1]] = self.calc(codes[2]) # 변수 할당
            else:
                self.var[codes[1]] = 0

        elif codes[0] == "보고싶어요": # 출력
            print(self.var[codes[1]])

    def compile(self, code):
        self.index = 0

        if code.pop(0) != "까꿍" or code.pop() != "귀여워":
            print("왜 이렇게 부끄러워해 이 바보야!")
            return

        while self.index < len(code):
            self.compile_line(code[self.index])
            self.index += 1

    def compile_file(self, code):
        try:
            with open(code, encoding='utf-8-sig') as cj_file:
                code = cj_file.read().splitlines()
                self.compile(code)
        except FileNotFoundError:
            print("철이 없었죠, 파일을 찾아 유학을 갔다는 게")

if __name__ == '__main__':
    compiler = ChoiJoonLang()
    compiler.compile_file('test.cj')
