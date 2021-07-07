class StringCheck():
    @staticmethod
    def is_space_or_null(string):
        is_invalid = False

        if len(string) == 0:
            is_invalid = True
        else:
            for char in string:
                if char == "" or char == " ":
                    is_invalid = True
                else:
                    is_invalid = False
                    break
        return is_invalid