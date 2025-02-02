class Args:
    class Environment:
        def __init__(self, d: dict):
            self.latitude: float = float(d['latitude'])
            self.longitude: float = float(d['longitude'])
            self.elevation: float = float(d['elevation'])
            self.timezone: str = d['timezone']
            self.date_and_time: str = d['date_and_time']
            self.atmospheric_model_type: str = d['atmospheric_model_type']
            self.atmospheric_model_file: str = d['atmospheric_model_file']

    class Motor:
        def __init__(self, d: dict):
            self.thrust_source: str = d['thrust_source']
            self.burn_time: float = float(d['burn_time'])
            self.dry_mass: float = float(d['dry_mass'])
            self.grain_number: int = int(d['grain_number'])
            self.grain_separation: float = float(d['grain_separation'])
            self.grain_outer_radius: float = float(d['grain_outer_radius'])
            self.grain_initial_inner_radius: float = float(d['grain_initial_inner_radius'])
            self.grain_initial_height: float = float(d['grain_initial_height'])
            self.grain_center_of_mass_position: float = float(d['grain_center_of_mass_position'])
            self.center_of_dry_mass_position: float = float(d['center_of_dry_mass_position'])
            self.grain_mass: float = float(d['grain_mass'])
            self.nozzle_radius: float = float(d['nozzle_radius'])

    class Rocket:
        def __init__(self, d: dict):
            self.radius: float = float(d['radius'])
            self.mass: float = float(d['mass'])
            self.inertia_1: float = float(d['inertia_1'])
            self.inertia_2: float = float(d['inertia_2'])
            self.inertia_3: float = float(d['inertia_3'])
            self.power_off_drag: str = d['power_off_drag']
            self.power_on_drag: str = d['power_on_drag']
            self.center_of_mass_without_motor: float = float(d['center_of_mass_without_motor'])
            self.motor_position: float = float(d['motor_position'])
            self.nose_length: float = float(d['nose_length'])
            self.nose_kind: str = d['nose_kind']
            self.nose_position: float = float(d['nose_position'])
            self.fins_number: int = int(d['fins_number'])
            self.fin_root_chord: float = float(d['fin_root_chord'])
            self.fin_tip_chord: float = float(d['fin_tip_chord'])
            self.fin_span: float = float(d['fin_span'])
            self.fin_position: float = float(d['fin_position'])
            self.fin_sweep_length: float = float(d['fin_sweep_length'])
            self.tail_top_radius: float = float(d['tail_top_radius'])
            self.tail_bottom_radius: float = float(d['tail_bottom_radius'])
            self.tail_length: float = float(d['tail_length'])
            self.tail_position: float = float(d['tail_position'])
            self.main_chute_cd: float = float(d['main_chute_cd'])
            self.main_chute_trigger: float = float(d['main_chute_trigger'])
            self.drogue_chute_cd: float = float(d['drogue_chute_cd'])
            self.trigger_sampling_rate: float = float(d['trigger_sampling_rate'])
            self.upper_rail_button_position: float = float(d['upper_rail_button_position'])
            self.lower_rail_button_position: float = float(d['lower_rail_button_position'])

    class Flight:
        def __init__(self, d: dict):
            self.rail_length: float = float(d['rail_length'])
            self.inclination: float = float(d['inclination'])
            self.heading: float = float(d['heading'])

    def __init__(self, d: dict):
        self.environment = self.Environment(d)
        self.motor = self.Motor(d)
        self.rocket = self.Rocket(d)
        self.flight = self.Flight(d)