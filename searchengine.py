from province import Province
from district import District
from commune import Commune
from operator import itemgetter


class SearchEngine:
    """
    Class for searching methods.
    """
    @staticmethod
    def list_statistics():
        """
        Returns list with specified order:

        |       MAŁOPOLSKIE               |
        |-----+---------------------------|
        |   1 | wojewódźtwo               |
        |-----+---------------------------|
        |  22 | powiaty                   |
        |-----+---------------------------|
        |  14 | gmina miejska             |
        |-----+---------------------------|
        | 122 | gmina wiejska             |
        |-----+---------------------------|
        |  46 | gmina miejsko-wiejska     |
        |-----+---------------------------|
        |  46 | obszar wiejski            |
        |-----+---------------------------|
        |  46 | miasto                    |
        |-----+---------------------------|
        |   3 | miasto na prawach powiatu |
        |-----+---------------------------|
        |   4 | delegatura                |

        :return: list
        """
        statistics_list = []

        powiaty_str = 'Powiaty'
        gmina_miejska_str = 'gmina miejska'
        gmina_wiejska_str = 'gmina wiejska'
        gmina_miejsko_wiejska_str = 'gmina miejsko-wiejska'
        obszar_wiejski_str = 'obszar wiejski'
        miasto_str = 'miasto'
        miasto_na_prawach_powiatu_str = 'miasto na prawach powiatu'
        delegatura_str = 'delegatura'

        if len(Province.province_list):
            statistics_list.append(
                                        [len(Province.province_list),
                                         Province.province_list[0].province_type]
            )

        if len(District.district_list):
            statistics_list.append(
                                        [len(District.district_list),
                                         powiaty_str]
            )

        statistics_list.append(
                                    [SearchEngine.count_type_occurrences(gmina_miejska_str),
                                     gmina_miejska_str]
        )

        statistics_list.append(
                                    [SearchEngine.count_type_occurrences(gmina_wiejska_str),
                                     gmina_wiejska_str]
        )

        statistics_list.append(
                                   [SearchEngine.count_type_occurrences(gmina_miejsko_wiejska_str),
                                    gmina_miejsko_wiejska_str]
        )

        statistics_list.append(
                                    [SearchEngine.count_type_occurrences(obszar_wiejski_str),
                                     obszar_wiejski_str]
        )

        statistics_list.append(
                                    [SearchEngine.count_type_occurrences(miasto_str),
                                     miasto_str]
        )

        statistics_list.append(
                                   [SearchEngine.count_type_occurrences(miasto_na_prawach_powiatu_str),
                                    miasto_na_prawach_powiatu_str]
        )

        statistics_list.append(
                                    [SearchEngine.count_type_occurrences(delegatura_str),
                                     delegatura_str]
        )

        return statistics_list

    @staticmethod
    def count_type_occurrences(commune_type):
        """
        counts occurrences of specified type in district and commune lists.

        :param commune_type: str
        :return: int
        """
        count = 0
        for commune_object in Commune.commune_list:
            if commune_object.commune_type_name == commune_type:
                count += 1
        for district_object in District.district_list:
            if district_object.district_type == commune_type:
                count += 1
        return count

    @staticmethod
    def cities_with_longest_names(how_many=1):
        """
        Returns a list of Cities with longest names.
        :param how_many: int
        :return: list
        """
        cities_list = []

        miasto_str = 'miasto'
        miasto_na_prawach_powiatu_str = 'miasto na prawach powiatu'

        while len(cities_list) < how_many:
            longest_name = ''
            for commune_object in Commune.commune_list:
                if commune_object.commune_type_name == miasto_str:
                    if (
                            len(commune_object.commune_name) > len(longest_name) and
                            (commune_object.commune_name not in cities_list)
                    ):
                        longest_name = commune_object.commune_name

            for district_object in District.district_list:
                if district_object.district_type == miasto_na_prawach_powiatu_str:
                    if (
                            len(district_object.district_name) > len(longest_name) and
                            (district_object.district_name not in cities_list)
                    ):
                        longest_name = district_object.district_name

            cities_list.append(longest_name)

        return cities_list

    @staticmethod
    def largest_number_of_communities(how_many=1):
        """

        :param how_many:
        :return:
        """
        districts_dict = {}

        for district_object in District.district_list:
            district_id = district_object.district_id
            count_occurrences = 0
            for commune_object in Commune.commune_list:
                if commune_object.district_id == district_id:
                    count_occurrences += 1

            districts_dict.update(
                                        {str(district_object.district_name): count_occurrences}
            )

        districts_dict = sorted(districts_dict.items(), key=itemgetter(1), reverse=True)
        return_list = districts_dict[:how_many]

        return return_list

    @staticmethod
    def more_than_one_category_locations():
        locations_list = []
        for commune_object in Commune.commune_list:
            look_for = str(commune_object.commune_name)
            flag = False
            for commune_name in Commune.commune_list:
                if(
                        commune_object is not commune_name and
                        commune_object.district_id == commune_name.district_id and
                        str(commune_name.commune_name) == look_for and
                        look_for not in locations_list
                ):
                    flag = True
                    break

            for district_name in District.district_list:
                if(
                                str(district_name.district_name) == look_for and
                                commune_object.district_id == district_name.district_id and
                                look_for not in locations_list
                ):
                    flag = True
                    break

            if flag:
                locations_list.append(commune_object.commune_name)

        locations_list = sorted(locations_list)
        return locations_list

    @staticmethod
    def advanced_search_by_name(user_input):
        search_lst = []
        for commune in Commune.commune_list:
            if commune.commune_name.lower().find(user_input.lower()) is not -1:
                search_lst.append(
                                        [commune.commune_name,
                                         commune.commune_type_name]
                )
        for district in District.district_list:
            if district.district_name.lower().find(user_input.lower()) is not -1:
                search_lst.append(
                                        [district.district_name,
                                         district.district_type]
                )
        search_lst = sorted(search_lst)
        return search_lst

    @staticmethod
    def advanced_search_by_type(user_input):
        search_lst = []
        for commune in Commune.commune_list:
            if commune.commune_type_name.lower().find(user_input.lower()) is not -1:
                search_lst.append(
                                        [commune.commune_name,
                                         commune.commune_type_name]
                )
        for district in District.district_list:
            if district.district_type.lower().find(user_input.lower()) is not -1:
                search_lst.append(
                                        [district.district_name,
                                         district.district_type]
                )
        search_lst = sorted(search_lst)
        return search_lst

    @staticmethod
    def advanced_search_by_district(user_input):
        search_lst = []
        for commune in Commune.commune_list:
            if commune.district_name.lower().find(user_input.lower()) is not -1:
                search_lst.append(
                                        [commune.commune_name,
                                         commune.commune_type_name]
                )
        for district in District.district_list:
            if district.district_name.lower().find(user_input.lower()) is not -1:
                search_lst.append(
                                        [district.district_name,
                                         district.district_type]
                )
        search_lst = sorted(search_lst)
        return search_lst
