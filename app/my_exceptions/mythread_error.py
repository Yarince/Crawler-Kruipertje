class MyThreadError(Exception):

    def __init__(self, message='Error in Thread!'):
        self.message = message

    def __str__(self):
        return self.message
