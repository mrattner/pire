if __name__ == "__main__":
    import os

    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

    if "{{ cookiecutter.add_tests }}" != "y":
        os.rmdir(os.path.join(PROJECT_DIRECTORY, "test"))

    if "{{ cookiecutter.use_bulma_with_sass }}" != "y":
        os.rmdir(os.path.join(PROJECT_DIRECTORY, "resources", "scss"))

    if "{{ cookiecutter.use_rtk_query }}" != "y":
        os.remove(os.path.join(PROJECT_DIRECTORY, "src", "api.ts"))
