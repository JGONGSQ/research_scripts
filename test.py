#!/usr/bin/python


UTILITY_VARIABLES_ALL = [
    ["HOMESUPP", "HOMESLA", "HOMEREGN", "ORIGIN"],
    ["HOMESUPP", "HOMESLA", "HOMEREGN", "ORIGIN"],
    ["HOMESUPP", "HOMESLA", "HOMEREGN", "ORIGIN", "HOUSEHOLD", "YOUNGEST", "EMPLOYMENT", "LIFECYCLE"],
    ["HOMESUPP", "HOMEREGN", "UNDER15", "OVER15", "AGEGROUP", "CH15TO24", "EMPLOYMENT", "LIFECYCLE"],
    ["HOMESUPP", "HOMESLA", "ORIGIN", "YOUNGEST", "MARITAL", "EMPLOYMENT"]
]


def get_utility_variables(alternatives):
    utility_variable = list()

    for alternative in alternatives:

        for item in alternative:
            if item not in utility_variable:
                utility_variable.append(item)

    return utility_variable



get_utility_variables(UTILITY_VARIABLES_ALL)
