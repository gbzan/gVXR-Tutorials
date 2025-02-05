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

exposure_lookup_table = [0.067, 0.083, 0.111, 0.167, 0.333, 0.500] # [s]
exposure_ID = 6
exposure_time_in_sec = exposure_lookup_table[exposure_ID - 1]
mAs = exposure_time_in_sec * current_in_uA / 1000

print("Exposure time:", exposure_time_in_sec, "in sec")
print("Exposure:", mAs, "mAs")

pixel_pitch_in_um = [150, 150]

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
    [ "Filter thickness", filter_thickness, thickness_unit],
    [ "Exposure time", exposure_time_in_sec, "sec"],
    [ "Exposure", mAs, "mAs"],
    [ "Pixel pitch", str(pixel_pitch_in_um[0]) + "x" + str(pixel_pitch_in_um[1]), "um" ],
    [ "Image size", str(projection_number_of_cols) + "x" + str(projection_number_of_rows), "pixels"],
]

display(pd.DataFrame(columns=columns, data=rows))