import importlib


class ClassReturner:
    """
    Class for help with classes that are unknown in that package.
    """
    @staticmethod
    def get_class(package, kls):
        """
        Returns the class of the given package with the classname
        :param package: name of the package the class is in
        :param kls: Classname
        :return: The Class
        """
        try:
            mod = importlib.import_module(package)
            return getattr(mod, kls)
        except (AttributeError, ModuleNotFoundError) as e:
            print(kls, "error: {0}".format(e.msg))
            return None

