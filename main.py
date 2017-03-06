from searchengine import SearchEngine
from filemanager import FileManager
from ptprint import PTPrint

class Menu:
    @staticmethod
    def show_main_menu():
        while True:
            print(
                '\n'
                'What would you like to do:\n'
                '   (1) List statistics\n'
                '   (2) Display 3 cities with longest names\n'
                '   (3) Display county\'s name with the largest number of communities\n'
                '   (4) Display locations, that belong to more than one category\n'
                '   (5) Advanced search\n'
                '   (0) Exit program\n'
            )
            option = input('Choose option: ')
            if option == '1':
                PTPrint.list_statistics_print(SearchEngine.list_statistics())
            elif option == '2':
                PTPrint.cities_with_longest_names_print(SearchEngine.cities_with_longest_names(3))
            elif option == '3':
                PTPrint.largest_number_of_communities_print(SearchEngine.largest_number_of_communities(4))
            elif option == '4':
                PTPrint.more_then_one_cat_loc_print(SearchEngine.more_than_one_category_locations())
            elif option == '5':
                Menu.advanced_search()
            elif option == '0':
                return False
            else:
                'There is no such option in menu'

    @staticmethod
    def advanced_search():
        while True:
            print(
                'What would you like to do:\n'
                '   (1) Search by name\n'
                '   (2) Search by type\n'
                '   (3) Search by district\n'
                '   (0) Exit search\n'
            )
            option = input('Choose option: ')
            if option == '0':
                return False
            search = input('Search for:')
            if option == '1':
                PTPrint.advanced_search_print(SearchEngine.advanced_search_by_name(search))
            elif option == '2':
                PTPrint.advanced_search_print(SearchEngine.advanced_search_by_type(search))
            elif option == '3':
                PTPrint.advanced_search_print(SearchEngine.advanced_search_by_district(search))


    @staticmethod
    def main():
        FileManager.load_file_csv()
        Menu.show_main_menu()


if __name__ == '__main__':
    Menu.main()
