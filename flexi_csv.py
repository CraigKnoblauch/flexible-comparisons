import csv
import os.path
from datetime import datetime


class Data:

    def __init__(self, filename, date_column=0):
        self.date_column = date_column
        self.dates = []
        self.filename = self.give_file(filename)
        self.selections = self.set_selections()
        self.values = self.set_values()

    def give_file(self, filename):
        """Method checks for existence of file before setting the 'filename'
        attribute to the argument
        """
        if not os.path.isfile(filename):
            print("The file " + filename + " could not be found")
        else:
            return filename

    def set_selections(self):
        """Method sets a list of selections from the header row of the
        provided file
        """
        with open(self.filename) as f:
            reader = csv.reader(f)

            # set the header row as the selections
            selections = next(reader)

            return selections

    def show_selections(self):
        """An object can call this method to display the list of selections to
        a program
        """
        for i, selection in enumerate(self.selections):
            print(i, selection)

    def set_values(self):
        """Method returns a dictionary following this kind of format:

        {'selection1': [csv_read_values],
         'selection2': [csv_read_values]}
        """
        values = {}
        with open(self.filename) as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    date = datetime.strptime(row[self.date_column], "%Y-%m-%d")
                except ValueError:
                    print(date, "missing data")
                    break
                else:
                    self.dates.append(date)

                for selection in self.selections:
                    values[selection] = []

                    try:
                        datum = row[self.selections.index(selection)]  # I'm not sure if index should be +1
                    except ValueError:
                        print(datum, "missing data")
                    else:
                        # Add a key value pair out of a selection and and the corresponding selection column
                        values[selection].append(datum)

        return values

