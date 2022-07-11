class Filter:
    @staticmethod
    def filter(function, list):
        new_list = []
        for s in list:
            if function(s) is True:
                new_list.append(s)
        list = new_list
        return list