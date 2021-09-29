class DataSet(object):

    @property

    def method_with_property(self):

        return 15

    def method_without_property(self):

        return 15

l = DataSet()

print(l.method_with_property)

print(l.method_without_property())