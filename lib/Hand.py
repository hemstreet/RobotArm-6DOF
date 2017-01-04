class Hand:
    def __init__(self, options):
        self.report = options['report']
        print("Initializing Hand")
        pass

    def open(self):
        self.report.log("HAND::Open")
        pass

    def close(self):
        self.report.log("HAND::Close")
        pass

    def rotate(self):
        self.report.log("HAND::Rotate")
        pass

    def position(self, value):
        self.report.log("HAND::Position")
        pass

