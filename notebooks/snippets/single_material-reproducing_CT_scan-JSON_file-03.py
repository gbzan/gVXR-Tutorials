nb_images = 1504
voltage_in_kV = 260
current_in_uA = 300
sdd_in_mm = 858.354
sod_in_mm = 400.88

odd_in_mm = sdd_in_mm - sod_in_mm

filter_material = "Fe"
filter_thickness = 10
thickness_unit = "mm"

filtration = [
    [filter_material, filter_thickness, thickness_unit]
]


import pandas as pd
from IPython.display import display, HTML

columns = ["Parameters", "Values", "Units"]

rows = [
    [ "Source type (beam shape)", "conebeam", "" ],
    [ "Beamline", 2, ""],
    [ "Number of projections", nb_images , ""],
    [ "Voltage", voltage_in_kV, "kV" ],
    [ "Current", current_in_uA, "uA" ],
    [ "Source to detector distance", sdd_in_mm, "mm" ],
    [ "Source to object distance", sod_in_mm, "mm" ],
    [ "Object to detector distance", odd_in_mm, "mm" ],
    [ "Filter material", filter_material, ""],
    [ "Filter thickness", filter_thickness, thickness_unit]
]

display(pd.DataFrame(columns=columns, data=rows))