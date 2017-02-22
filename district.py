from localgovernmentunit import LocalGovernmentUnit


class District(LocalGovernmentUnit):
    district_list = []

    def __init__(self, province_id, province_name, province_type, district_id, district_name, district_type):
        self.province_id = province_id
        self.province_name = province_name
        self.province_type = province_type
        self.district_id = district_id
        self.district_name = district_name
        self.district_type = district_type
