from prettytable import PrettyTable


class PTPrint:
    """
    Resources:
    http://ptable.readthedocs.io/en/latest/installation.html
    """
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

    @staticmethod
    def cities_with_longest_names_print(table):
        prettytable = PrettyTable()
        prettytable.field_names = ["Cities with longest names"]
        for item in table:
            prettytable.add_row([item])
        prettytable.align = "r"

        return print(prettytable)

    @staticmethod
    def largest_number_of_communities_print(table):
        prettytable = PrettyTable()
        prettytable.field_names = ["District name", "Number of communes"]
        prettytable = PTPrint.pt_loop(table, prettytable)
        prettytable.align = "r"

        return print(prettytable)

    @staticmethod
    def more_then_one_cat_loc_print(table):
        prettytable = PrettyTable()
        prettytable.field_names = ["More than one category locations"]
        for item in table:
            prettytable.add_row([item])
        prettytable.align = "r"

        return print(prettytable)

