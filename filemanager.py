import csv
from province import Province
from district import District
from commune import Commune


class FileManager:

    @staticmethod
    def load_file_csv():
        with open('malopolska.csv', 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)

            province_name = ''
            province_type = ''
            district_name = ''
            district_type = ''

            for line in reader:
                if line[1] == '':
                    Province.province_list.append(Province(line[0], line[4], line[5]))
                    province_name = line[4]
                    province_type = line[5]
                elif line[2] == '':
                    District.district_list.append(District(line[0], province_name, province_type,
                                                           line[1], line[4], line[5]))
                    district_name = line[4]
                    district_type = line[5]
                else:
                    Commune.commune_list.append(Commune(line[0], province_name, province_type, line[1], district_name,
                                                        district_type, line[2], line[3], line[4], line[5]))

    def save_file(self):
        pass

