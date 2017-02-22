from localgovernmentunit import LocalGovernmentUnit


class Commune(LocalGovernmentUnit):
    commune_list = []

    def __init__(self, province_id, province_name, province_type, district_id, district_name, district_type,
                 commune_id, commune_type_id, commune_name, commune_type_name):
        self.province_id = province_id
        self.province_name = province_name
        self.province_type = province_type
        self.district_id = district_id
        self.district_name = district_name
        self.district_type = district_type
        self.commune_id = commune_id
        self.commune_name = commune_name
        self.commune_type_id = commune_type_id
        self.commune_type_name = commune_type_name
