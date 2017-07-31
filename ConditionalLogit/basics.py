from collections import OrderedDict


# utility function settings
basic_specification = OrderedDict()
basic_names = OrderedDict()

basic_specification["intercept"] = [1, 2, 3, 4]
basic_names["intercept"] = [
    'ASC_NSW',
    'ASC_VIC',
    'ASC_QLD',
    'ASC_SA',
    # 'ASC_TAS',
]

basic_specification["HOMESLA"] = [1, 2, 4]
basic_names["HOMESLA"] = [
    'HOMESLA_NSW',
    'HOMESLA_VIC',
    # 'HOMESLA_QLD',
    'HOMESLA_SA',
    # 'HOMESLA_TAS'
]
# "LIFECYCLE_SINGLE"
# "LIFECYCLE_COUPLE_NO_KIDS"
# "LIFECYCLE_COUPLE_WITH_KIDS"

# basic_specification["HOUSEHOLD"] = [2]
# basic_names["HOUSEHOLD"] = [
#     # "HOUSEHOLD_NSW",
#     "HOUSEHOLD_VIC",
#     # "HOUSEHOLD_QLD",
#     # "HOUSEHOLD_SA",
#     # "HOUSEHOLD_TAS"
# ]

# basic_specification["LIFECYCLE_COUPLE_WITH_KIDS"] = [5]
# basic_names["LIFECYCLE_COUPLE_WITH_KIDS"] = [
#     "LIFECYCLE_COUPLE_WITH_KIDS_NSW",
#     # "LIFECYCLE_SINGLE_VIC",
#     # "LIFECYCLE_SINGLE_QLD",
#     # "LIFECYCLE_SINGLE_SA",
#     # "LIFECYCLE_SINGLE_TAS"
# ]


basic_specification["ORIGIN_NSW"] = [2]
basic_names["ORIGIN_NSW"] = [
    # "ORIGIN_NSW_NSW",
    "ORIGIN_NSW_VIC",
    # "ORIGIN_NSW_QLD",
    # "ORIGIN_NSW_SA",
#     "ORIGIN_NSW_TAS"
]

basic_specification["ORIGIN_VIC"] = [1, 2, 3]
basic_names["ORIGIN_VIC"] = [
    "ORIGIN_VIC_NSW",
    "ORIGIN_VIC_VIC",
    "ORIGIN_VIC_QLD",
    # "ORIGIN_VIC_SA",
    # "ORIGIN_VIC_TAS"
]

basic_specification["ORIGIN_QLD"] = [1, 3]
basic_names["ORIGIN_QLD"] = [
    "ORIGIN_QLD_NSW",
    # "ORIGIN_QLD_VIC",
    "ORIGIN_QLD_QLD",
    # "ORIGIN_QLD_SA",
    # "ORIGIN_QLD_TAS"
]

basic_specification["ORIGIN_SA"] = [1, 2, 3]
basic_names["ORIGIN_SA"] = [
    "ORIGIN_SA_NSW",
    "ORIGIN_SA_VIC",
    "ORIGIN_SA_QLD",
    # "ORIGIN_SA_SA",
    # "ORIGIN_SA_TAS"
]

# "ORIGIN_NSW_NSW",
# "ORIGIN_NSW_VIC",
# "ORIGIN_NSW_QLD",
# "ORIGIN_NSW_SA",
# "ORIGIN_NSW_TAS"

basic_specification["GENDER_MALE"] = [1, 2]
basic_names["GENDER_MALE"] = [
    'GENDER_MALE_NSW',
    'GENDER_MALE_VIC',
    # 'GENDER_MALE_QLD',
    # 'GENDER_MALE_SA',
    # 'GENDER_MALE_TAS',
]

basic_specification["GENDER_FEMALE"] = [4]
basic_names["GENDER_FEMALE"] = [
#     'GENDER_FEMALE_NSW',
#     'GENDER_FEMALE_VIC',
#     'GENDER_FEMALE_QLD',
    'GENDER_FEMALE_SA',
    # 'GENDER_FEMALE_TAS',
]


basic_specification["AGEGROUP_15_29"] = [1, 2]
basic_names["AGEGROUP_15_29"] = [
    "AGEGROUP_15_29_NSW",
    "AGEGROUP_15_29_VIC",
    # "AGEGROUP_15_29_QLD",
    # "AGEGROUP_15_29_SA",
    # "AGEGROUP_15_29_TAS",
]

basic_specification["AGEGROUP_30_39"] = [2, 3]
basic_names["AGEGROUP_30_39"] = [
    # "AGEGROUP_30_39_NSW",
    "AGEGROUP_30_39_VIC",
    "AGEGROUP_30_39_QLD",
    # "AGEGROUP_30_39_SA",
    # "AGEGROUP_30_39_TAS",
]
#
basic_specification["AGEGROUP_40_49"] = [4]
basic_names["AGEGROUP_40_49"] = [
    # "AGEGROUP_40_49_NSW",
    # "AGEGROUP_40_49_VIC",
    # "AGEGROUP_40_49_QLD",
    "AGEGROUP_40_49_SA",
    # "AGEGROUP_40_49_TAS",
]

basic_specification["AGEGROUP_50_59"] = [2]
basic_names["AGEGROUP_50_59"] = [
    # "AGEGROUP_50_59_NSW",
    "AGEGROUP_50_59_VIC",
    # "AGEGROUP_50_59_QLD",
    # "AGEGROUP_50_59_SA",
    # "AGEGROUP_50_59_TAS",
]


# basic_specification["EMPLOYMENT_STUDYING"] = [2]
# basic_names["EMPLOYMENT_STUDYING"] = [
    # "EMPLOYMENT_STUDYING_NSW",
    # "EMPLOYMENT_STUDYING_VIC",
    # "EMPLOYMENT_STUDYING_QLD",
    # "EMPLOYMENT_STUDYING_SA",
    # "EMPLOYMENT_STUDYING_TAS",
# ]

basic_specification["EMPLOYMENT_WORKING"] = [1, 2]
basic_names["EMPLOYMENT_WORKING"] = [
    "EMPLOYMENT_WORKING_NSW",
    "EMPLOYMENT_WORKING_VIC",
    # "EMPLOYMENT_WORKING_QLD",
    # "EMPLOYMENT_WORKING_SA",
    # "EMPLOYMENT_WORKING_TAS",
]

basic_specification["EMPLOYMENT_RETIRED"] = [1, 2, 5]
basic_names["EMPLOYMENT_RETIRED"] = [
    "EMPLOYMENT_RETIRED_NSW",
    "EMPLOYMENT_RETIRED_VIC",
    # "EMPLOYMENT_RETIRED_QLD",
    # "EMPLOYMENT_RETIRED_SA",
    "EMPLOYMENT_RETIRED_TAS",
]

basic_specification["Distance"] = [1, 2, 3, 4, 5]
basic_names["Distance"] = [
    "Distance_NSW",
    "Distance_VIC",
    "Distance_QLD",
    "Distance_SA",
    "Distance_TAS",
    # "Distance_NT",
]