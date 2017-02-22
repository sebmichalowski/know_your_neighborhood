from searchengine import SearchEngine
from filemanager import FileManager
from prettytable import PrettyTable
from district import District
from commune import Commune
from province import Province
from ptprint import PTPrint

class Menu:
    @staticmethod
    def show_main_menu():
        while True:
            Menu.show_table(
                'What would you like to do:\n'
                '   (1) List statistics\n'
                '   (2) Display 3 cities with longest names\n'
                '   (3) Display county\'s name with the largest number of communities\n'
                '   (4) Display locations, that belong to more than one category\n'
                '   (5) Advanced search\n'
                '   (0) Exit program)\n'
            )
            option = input('Choose option: ')
            if option == '1':
                Main.show_table(SearchEngine.list_statistics())
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                pass
            elif option == '0':
                pass
            else:
                'There is no such option in menu'

    @staticmethod
    def main_menu_logic():
        pass

    @staticmethod
    def main():
        #Menu.show_main_menu()
        FileManager.load_file_csv()

        #print(Menu.show_table(SearchEngine.cities_with_longest_names(3)))
        #print(SearchEngine.cities_with_longest_names(3))
        PTPrint.list_statistics_print(SearchEngine.list_statistics())

        #Menu.show_table(SearchEngine.largest_number_of_communities())

        #Menu.show_table(SearchEngine.largest_number_of_communities_bad(4))
        #print(SearchEngine.largest_number_of_communities_bad(4))

        #print(SearchEngine.more_than_one_category_locations())

        #print(Menu.show_table(SearchEngine.advanced_search_by_name('nowy')))
        PTPrint.advanced_search_print(SearchEngine.advanced_search_by_name('nowy'))

        #print(len(Commune.commune_list) + len(Province.province_list) + len(District.district_list))
        #print(len(District.district_list))

    @staticmethod
    def show_table(to_print_list):
        """
        Returns a list as a string with users depending on the class we choose

        :param to_print_list:

        :return: string
        """
        # transposition of list to print, for easy access to columns
        transposed_to_print_list = [list(x) for x in zip(*to_print_list)]

        # evaluate lengths of strings in columns for getting longest strings, to determine columns widths
        columns_widths = []
        for line in transposed_to_print_list:
            max_width = 0
            for item in line:
                if len(str(item)) > max_width:
                    max_width = len(str(item)) + 2
            columns_widths.append(max_width)

        table_str = ""  # string with content of table
        # generate strings for top and bottom of table, and row separator
        pauses = "-" * (sum(columns_widths) + len(to_print_list[0]) - 1)  # create of string with '-' for printing (---)
        top = "/{}\\\n".format(pauses)  # top row of table /----\
        bot = "\\{}/\n".format(pauses)  # bottom row       \----/

        # generate separator row |---|----------|-----| ....
        separator = "|"

        for item in columns_widths:
            separator += '{:^{}}|'.format("-" * (columns_widths[columns_widths.index(item)]),
                                          columns_widths[columns_widths.index(item)] - 1)

        for line in to_print_list:
            i = 0
            table_str += '|'
            for item in line:  # print every item from list from table in format: | column | column | col | ...
                table_str += '{:^{}}|'.format(item, columns_widths[i])
                i += 1

            if line != to_print_list[-1]:  # adds separator after row, except last row (bottom row is adding later)
                table_str += "\n{}\n".format(separator)

        return "{}{}\n{}".format(top, table_str, bot)


if __name__ == '__main__':
    Menu.main()
