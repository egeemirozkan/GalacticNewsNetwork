class Beacon:
    def take_passwords(string_):
        file_ = open(string_, "r")
        passes = file_.read().split("\n")
        file_.close()
        return passes


    def twittfy(string_):
        continue_ = True
        strings = []
        while continue_ == True:
            first_string = string_[:130]
            strings.append(first_string)
            string_ = string_[130:]
            if string_ == '':
                continue_ = False
        return strings, len(strings)
