import contextlib


@contextlib.contextmanager
def manage_context():
    print("Entering the Context Manager")
    yield 5
    print("Exiting the Context Manager")


with manage_context() as one:
    print(one)


class ContextManager:
    def __enter__(self):
        print("Entering the Context Manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
