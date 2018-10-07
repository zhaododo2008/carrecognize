import os


def handle_uploaded_file(f):
    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
    IMGFILES_FOLDER = os.path.join(PROJECT_ROOT, 'file/a.jpg')

    with open(IMGFILES_FOLDER, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

        if os.path.exists(IMGFILES_FOLDER):
            os.remove(IMGFILES_FOLDER)
