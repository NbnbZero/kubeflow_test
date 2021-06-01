from my_decorator import helper


# print hello world
@helper
def hello_world(filename):
    print('This is my hello world method.')


if __name__ == '__main__':
    hello_world(__file__)
