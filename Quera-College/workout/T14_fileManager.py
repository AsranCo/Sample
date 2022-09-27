import os


class FileManager:
    def find(self, name, address):
        resut = list()
        for root, dirs, files in os.walk(address):
            for file in files:
                if file == name:
                    resut.append(os.path.join(root, file))
        return resut

    def create_file(self, name, address):
        path = os.path.join(address, name)
        if os.path.exists(path):
            pass
        else:
            with open(path, 'w') as fp:
                pass

    def create_dir(self, name, address):
        path = os.path.join(address, name)
        try:
            os.mkdir(path)
        except:
            pass

    def delete(self, name, address):
        path = os.path.join(address, name)

        if os.path.exists(path):
            os.remove(path)
        else:
            pass

    def restore(self, name):
        pass
