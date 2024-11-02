from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# params
name_factor = { "a": None, "b": None, "r2": None, "max": None }
pri_factor = { "a": None, "b": None, "r2": None, "max": None }
num_stars_factor = { "a": None, "b": None, "r2": None, "max": None }
radius_factor = { "a": 0.5, "b": 100, "r2": 1, "max" : 450 }
num_emp_min_factor = { "a": 0, "b": 0, "r2": 1, "max" : None }
num_emp_max_factor = { "a": 0.03, "b": 0, "r2": 1, "max" : None }
num_def_emp_factor = { "a": 0.015, "b": 0, "r2": 1, "max" : None }
fallen_emp_def_factor = { "a": 0.005, "b": -1, "r2": 1, "max" : None }
fallen_emp_max_factor = { "a": 0.005, "b": 0, "r2": 1, "max" : None }
marauder_emp_def_factor = { "a": 0.0025, "b": 0.3, "r2": 0.89, "max" : None }
marauder_emp_max_factor = { "a": 0.0025, "b": 0.7, "r2": 0.89, "max" : None }
adv_emp_def_factor = { "a": 0.005, "b": -1, "r2": 1, "max" : None }
colonizable_planet_odds_factor = { "a": None, "b": None, "r2": None, "max": None }
primitive_odds_factor = { "a": None, "b": None, "r2": None, "max": None }
crisis_strength_factor = { "a": 0.00125, "b": 0.25, "r2": None, "max": None }
ex_crisis_min_factor = { "a": None, "b": None, "r2": None, "max": None }
ex_crisis_max_factor = { "a": None, "b": None, "r2": None, "max": None }
cluster_value_factor = { "a": None, "b": None, "r2": None, "max": None }
cluster_max_factor = { "a": 0.0075, "b": 0, "r2": 1.33333, "max" : 6 }
cluster_radius_factor = { "a": 0.095, "b": 70, "r2": 0.96, "max" : 150 }
cluster_dist_factor = { "a": 0.3075, "b": 57.5, "r2": 0.99, "max" : 300 }
max_hyperlane_dist_factor = { "a": None, "b": None, "r2": None, "max" : 50 }
home_max_system_factor = { "a": None, "b": None, "r2": None, "max": None }
home_min_system_factor = { "a": None, "b": None, "r2": None, "max": None }
home_min_bridges_factor = { "a": None, "b": None, "r2": None, "max": None }
home_max_bridges_factor = { "a": None, "b": None, "r2": None, "max": None }
open_max_system_factor = { "a": None, "b": None, "r2": None, "max": None }
open_min_system_factor = { "a": None, "b": None, "r2": None, "max": None }
open_min_bridges_factor = { "a": None, "b": None, "r2": None, "max": None }
open_max_bridges_factor = { "a": None, "b": None, "r2": None, "max": None }
num_nebulas_factor = { "a": 0.01, "b": 0, "r2": 1, "max" : None }
nebula_size_factor = { "a": None, "b": None, "r2": None, "max": None }
nebula_min_dist_factor = { "a": None, "b": None, "r2": None, "max": None }
num_wormhole_mix_factor = { "a": None, "b": None, "r2": None, "max": None }
num_wormhole_max_factor = { "a": None, "b": None, "r2": None, "max": None }
num_wormhole_pair_def_factor = { "a": None, "b": None, "r2": None, "max": None }
num_gate_min_factor = { "a": None, "b": None, "r2": None, "max": None }
num_gate_max_factor = { "a": None, "b": None, "r2": None, "max": None }
num_gate_def_factor = { "a": None, "b": None, "r2": None, "max": None }
num_hyperlanes_min_factor = { "a": None, "b": None, "r2": None, "max": None }
num_hyperlanes_max_factor = { "a": None, "b": None, "r2": None, "max": None }
num_hyperlanes_def_factor = { "a": None, "b": None, "r2": None, "max": None }

# add your map size ranges for generation.
map_gen_list = [
    {"min":25, "max":400, "step":25},
    {"min":400, "max":1000, "step":50},
    {"min":1000, "max":5500,"step":500}
]

class setting:
    def __init__(self, arg):
        self.name = arg["name"]
        self.pri = arg["pri"]
        self.num_stars = arg["num_stars"]
        self.radius = arg["radius"]
        self.num_emp_min = arg["num_emp_min"]
        self.num_emp_max = arg["num_emp_max"]
        self.num_def_emp = arg["num_def_emp"]
        self.fallen_emp_def = arg["fallen_emp_def"]
        self.fallen_emp_max = arg["fallen_emp_max"]
        self.marauder_emp_def = arg["marauder_emp_def"]
        self.marauder_emp_max = arg["marauder_emp_max"]
        self.adv_emp_def = arg["adv_emp_def"]
        self.colonizable_planet_odds = arg["colonizable_planet_odds"]
        self.primitive_odds = arg["primitive_odds"]
        self.crisis_strength = arg["crisis_strength"]
        self.ex_crisis_min = arg["ex_crisis_min"]
        self.ex_crisis_max = arg["ex_crisis_max"]
        self.cluster_value = arg["cluster_value"]
        self.cluster_max = arg["cluster_max"]
        self.cluster_radius = arg["cluster_radius"]
        self.cluster_dist = arg["cluster_dist"]
        self.max_hyperlane_dist = arg["max_hyperlane_dist"]
        self.home_max_system = arg["home_max_system"]
        self.home_min_system = arg["home_min_system"]
        self.home_min_bridges = arg["home_min_bridges"]
        self.home_max_bridges = arg["home_max_bridges"]
        self.open_max_system = arg["open_max_system"]
        self.open_min_system = arg["open_min_system"]
        self.open_min_bridges = arg["open_min_bridges"]
        self.open_max_bridges = arg["open_max_bridges"]
        self.num_nebulas = arg["num_nebulas"]
        self.nebula_size = arg["nebula_size"]
        self.nebula_min_dist = arg["nebula_min_dist"]
        self.num_wormhole_min = arg["num_wormhole_min"]
        self.num_wormhole_max = arg["num_wormhole_max"]
        self.num_wormhole_pair_def = arg["num_wormhole_pair_def"]
        self.num_gate_min = arg["num_gate_min"]
        self.num_gate_max = arg["num_gate_max"]
        self.num_gate_def = arg["num_gate_def"]
        self.num_hyperlanes_min = arg["num_hyperlanes_min"]
        self.num_hyperlanes_max = arg["num_hyperlanes_max"]
        self.num_hyperlanes_def = arg["num_hyperlanes_def"]

    def get_setting(self):
        tex = f"""
setup_scenario = {{
    name = "{self.name}"
    priority = {self.pri}					#priority decides in which order the scenarios are listed
    num_stars = {self.num_stars}
    radius = {self.radius}					#should be less than 500, preferably less than ~460
    num_empires = {{ min = {self.num_emp_min} max = {self.num_emp_max} }}	#limits player customization
    num_empire_default = {self.num_def_emp}
    fallen_empire_default = {self.fallen_emp_def}
    fallen_empire_max = {self.fallen_emp_max}
    marauder_empire_default = {self.marauder_emp_def}
    marauder_empire_max = {self.marauder_emp_max}
    advanced_empire_default = {self.adv_emp_def}
    colonizable_planet_odds = {self.colonizable_planet_odds}
    primitive_odds = {self.primitive_odds}
    crisis_strength = {self.crisis_strength}
    extra_crisis_strength = {{ 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10 11 12 13 14 15 17.5 20 22.5 25 30 35 40 45 50 100 300 500 1000 }}

    cluster_count = {{
        method = one_every_x_empire
        #method = constant
        value = {self.cluster_value}
        max = {self.cluster_max}
    }}
    cluster_radius = {self.cluster_radius}
    cluster_distance_from_core = {self.cluster_dist}

    max_hyperlane_distance = {self.max_hyperlane_dist}

    home_system_partitions = {{
        max_systems = {self.home_max_system}
        min_systems= {self.home_min_system}

        min_bridges = {self.home_min_bridges}
        max_bridges = {self.home_max_bridges}

        method = breadth_first
    }}

    open_space_partitions = {{
        max_systems = {self.open_max_system}
        min_systems= {self.open_min_system}

        min_bridges = {self.open_min_bridges}
        max_bridges = {self.open_max_bridges}

        method = depth_first
    }}

    num_nebulas	= {self.num_nebulas}
    nebula_size = {self.nebula_size}
    nebula_min_dist = {self.nebula_min_dist}

    num_wormhole_pairs = {{ min = {self.num_wormhole_min} max = {self.num_wormhole_max} }}
    num_wormhole_pairs_default = {self.num_wormhole_pair_def}
    num_gateways = {{ min = {self.num_gate_min} max = {self.num_gate_max} }}
    num_gateways_default = {self.num_gate_def}
    num_hyperlanes = {{ min={self.num_hyperlanes_min} max= {self.num_hyperlanes_max} }}
    num_hyperlanes_default = {self.num_hyperlanes_def}

	supports_shape = elliptical
	supports_shape = spiral_2
	supports_shape = spiral_3
	supports_shape = spiral_4
	supports_shape = spiral_6
	supports_shape = ring
	supports_shape = bar
	supports_shape = starburst
	supports_shape = cartwheel
	supports_shape = spoked
}}
"""

        return tex

def align_num_by_step(num, step, power):
    pow10 = 10**power
    aligned_stepped = int(num * pow10 + step / 2)
    aligned = (aligned_stepped // step) * step
    return aligned / pow10

map_text = ""
#num_star_list = [50,75,100,125,150,175,200,225, 250, 275, 300, 325, 350, 375, 400, 450,500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1500,2000,2500,3000,3500,4000,4500,5000]
#num_star_list = [
#    50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900,925,950,975,
#    1000, 1250,1500,1750,2000,2250,2500,2750,3000,3500,4000,4500,5000
#]

map_size_list = []

for map_gen in map_gen_list:
    for i in range(map_gen["min"], map_gen["max"], map_gen["step"]):
        map_size_list.append(i)


count = 5
for galaxy in map_size_list:
    add_max_emp = round(galaxy / 2)
    add_max_fall = round(galaxy / 10)

    kwargs = {}
    kwargs.update({"name": str(galaxy)})
    kwargs.update({"pri": str(count)})
    kwargs.update({"num_stars": str(galaxy)})
    if galaxy > 450:
        kwargs.update({"radius": "450"})
    else:
        kwargs.update({"radius": str(round(radius_factor["a"] * galaxy + radius_factor["b"]))})
    kwargs.update({"num_emp_min": "0"})
    kwargs.update({"num_emp_max": str(round(num_emp_max_factor["a"] * galaxy + num_emp_max_factor["b"] + add_max_emp))})
    kwargs.update({"num_def_emp": str(round(num_def_emp_factor["a"] * galaxy + num_def_emp_factor["b"]))})
    kwargs.update({"fallen_emp_def": str(round(fallen_emp_def_factor["a"] * galaxy + fallen_emp_def_factor["b"]))})
    kwargs.update({"fallen_emp_max": str(round(fallen_emp_max_factor["a"] * galaxy + fallen_emp_max_factor["b"] + add_max_fall))})
    kwargs.update({"marauder_emp_def": str(round(marauder_emp_def_factor["a"] * galaxy + marauder_emp_def_factor["b"]))})
    kwargs.update({"marauder_emp_max": str(round(marauder_emp_max_factor["a"] * galaxy + marauder_emp_def_factor["b"] + add_max_fall))})
    kwargs.update({"adv_emp_def": str(round(adv_emp_def_factor["a"] * galaxy + adv_emp_def_factor["b"]))})
    kwargs.update({"colonizable_planet_odds": "1.0"})
    kwargs.update({"primitive_odds": "1.0"})
    crisis_str = crisis_strength_factor["a"] * galaxy + crisis_strength_factor["b"]
    kwargs.update({"crisis_strength": str(align_num_by_step(crisis_str, 25, 2))})
    # kwargs.update({"crisis_strength": str(Decimal(str(crisis_str)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))})
    kwargs.update({"ex_crisis_min": "10"})
    kwargs.update({"ex_crisis_max": "25"})
    kwargs.update({"cluster_value": "1"})
    clus_max = cluster_max_factor["a"] * galaxy + cluster_max_factor["b"]
    if clus_max > cluster_max_factor["max"]:
        kwargs.update({"cluster_max": cluster_max_factor["max"]})
    else:
        kwargs.update({"cluster_max": str(round(clus_max))})
    clus_r = cluster_radius_factor["a"] * galaxy + cluster_radius_factor["b"]
    if clus_r > cluster_radius_factor["max"]:
        kwargs.update({"cluster_radius": cluster_radius_factor["max"]})
    else:
        kwargs.update({"cluster_radius": str(round(clus_r))})
    clus_d = cluster_dist_factor["a"] * galaxy + cluster_dist_factor["b"]
    if clus_d > cluster_dist_factor["max"]:
        kwargs.update({"cluster_dist": cluster_dist_factor["max"]})
    else:
        kwargs.update({"cluster_dist": str(round(clus_d))})
    kwargs.update({"max_hyperlane_dist": "50"})
    kwargs.update({"home_max_system": "15"})
    kwargs.update({"home_min_system": "8"})
    kwargs.update({"home_min_bridges": "2"})
    kwargs.update({"home_max_bridges": "4"})
    kwargs.update({"open_max_system": "10"})
    kwargs.update({"open_min_system": "4"})
    kwargs.update({"open_min_bridges": "2"})
    open_max_b = 3
    if galaxy <= 200:
        open_max_b = 4
    elif galaxy >= 400 and galaxy < 500:
        open_max_b = 6
    elif galaxy >= 500 and galaxy < 900:
        open_max_b = 2
    elif galaxy >= 1000:
        open_max_b = 4
    kwargs.update({"open_max_bridges": str(open_max_b)})
    kwargs.update({"num_nebulas": str(round(num_nebulas_factor["a"] * galaxy + num_nebulas_factor["b"]))})
    kwargs.update({"nebula_size": "60"})
    if galaxy <= 200:
        kwargs.update({"nebula_min_dist": "100"})
    else:
        kwargs.update({"nebula_min_dist": "200"})
    kwargs.update({"num_wormhole_min": "0"})
    kwargs.update({"num_wormhole_max": "5"})
    kwargs.update({"num_wormhole_pair_def": "1"})
    kwargs.update({"num_gate_min": "0"})
    kwargs.update({"num_gate_max": "5"})
    kwargs.update({"num_gate_def": "1"})
    kwargs.update({"num_hyperlanes_min": "0.5"})
    kwargs.update({"num_hyperlanes_max": "3"})
    kwargs.update({"num_hyperlanes_def": "1"})

    # check
    for key in kwargs:
        if float(kwargs[key]) < 0:
            kwargs[key] = "0"

    count += 1
    set = setting(kwargs)
    setting_text = set.get_setting()
    print(setting_text)

    map_text += "################# " + str(galaxy) + " #################"
    map_text += setting_text
    map_text += "################# " + str(galaxy) + " END " + "#################\n\n"

with open("./out_circinus.txt", mode="w") as f:
    f.write(map_text)


