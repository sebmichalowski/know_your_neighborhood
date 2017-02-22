from prettytable import PrettyTable
from searchengine import SearchEngine


class PTPrint:
    @staticmethod
    def pt_loop(table, prettytable):
        for row in table:
            prettytable.add_row([item for item in row])
        return prettytable

    @staticmethod
    def list_statistics_print(table):
        prettytable = PrettyTable()
        prettytable.field_names = ['', 'Małopolska']
        for row in table:
            prettytable.add_row([item for item in row])
        prettytable.align = "l"

        return print(prettytable)



    @staticmethod
    def advanced_search_print(table):
        prettytable = PrettyTable()
        prettytable.field_names = ["City name", "Area"]
        prettytable = PTPrint.pt_loop(table, prettytable)
        prettytable.align = "r"

        return print(prettytable)
