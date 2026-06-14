import os

def open_app(package):

    os.system(
        f"monkey -p {package} -c android.intent.category.LAUNCHER 1"
    )

    return f"Opening {package}"
