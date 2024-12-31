class SREFManager:
    def __init__(self):
        self.current_sref = None
        self.base_path = None

    def set_base_path(self, path):
        self.base_path = path

    def set_current_sref(self, sref):
        self.current_sref = sref