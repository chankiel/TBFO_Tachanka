class HTMLChecker:
    def __init__(self):
        self.stack = []

    def process_input(self, html_input):
        for char in html_input:
            self.process_character(char)

    def process_character(self, char):
        if char == '<':
            self.stack.append(char)
        elif char == '>':
            if self.stack and self.stack[-1] == '<':
                self.stack.pop()
            else:
                print("Error: Tidak ada tag pembuka yang sesuai.")
                exit(1)

    def is_html_valid(self):
        return not self.stack

if __name__ == "__main__":
    html_input = input("Masukkan HTML: ")
    checker = HTMLChecker()
    checker.process_input(html_input)

    if checker.is_html_valid():
        print("HTML valid.")
    else:
        print("HTML tidak valid.")
