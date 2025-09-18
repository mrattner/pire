if __name__ == "__main__":
    import os

    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

    if "{{ cookiecutter.add_tests }}" != "y":
        os.rmdir(os.path.join(PROJECT_DIRECTORY, "test"))
