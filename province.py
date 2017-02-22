from localgovernmentunit import LocalGovernmentUnit


class Province(LocalGovernmentUnit):
    province_list = []

    def __init__(self, province_id, province_name, province_type):
        self.province_id = province_id
        self.province_name = province_name
        self.province_type = province_type
