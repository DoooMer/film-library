import sys
from Filmlibrary.Filmlibrary import Filmlibrary

if __name__ == '__main__':
    app = Filmlibrary(sys.argv)
    sys.exit(app.run())
