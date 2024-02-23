from Utils import ArgumentParser

class ApplicationContext:

    def __init__(self) -> None:
        self.args = ArgumentParser().parse_args()

if __name__=='__main__':
    app = ApplicationContext()
