class FeeBurn:

    def __init__(self):
        self.feeBurn = False

    @staticmethod
    def json_parse(json_data):
        result = FeeBurn()
        result.feeBurn = json_data.get_boolean("feeBurn")

        return result
