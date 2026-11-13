class Log_controller:
    def __init__(self):
        self.clear_log()

    def clear_log(self):
        with open("data/logs.txt", "w", encoding="utf-8"):
            pass

    def write_log(self, text):
        with open("data/logs.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
