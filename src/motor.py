import rocketpy
import math
import args


def calculate_moment_of_inertia(grain_number, grain_outer_radius, grain_initial_height, grain_separation, grain_mass, dry_mass, thickness):
    total_height = grain_initial_height * grain_number + (grain_number - 1) * grain_separation
    radius = grain_outer_radius + thickness
    grains_total_mass = grain_mass * grain_number
    wet_mass = grains_total_mass + dry_mass

    I_zz = dry_mass * 0.5 * (pow(radius, 2) + pow(grain_outer_radius, 2))
    I_xx = ((wet_mass*pow(radius, 2)) / 4 + (wet_mass * pow(total_height, 2)) / 12) - (grains_total_mass * pow(grain_outer_radius, 2)) / 4 + (grains_total_mass*pow(total_height, 2)) / 12
    
    return (I_xx, I_xx, I_zz)

def calculate_grains_center_of_mass(grain_number, grain_initial_height, grain_separation):
    
    local_grain_center_of_mass = grain_initial_height / 2

    return (local_grain_center_of_mass * grain_number) + (grain_separation * (grain_number // 2))

def calculate_center_of_dry_mass(grain_number, grain_initial_height, grain_separation):
    total_height = grain_initial_height * grain_number + (grain_number - 1) * grain_separation
    
    return total_height / 2

def calculate_density(grain_outer_radius, grain_initial_inner_radius, grain_initial_height, grain_mass):
    grain_volume = math.pi * (pow(grain_outer_radius, 2) - pow(grain_initial_inner_radius, 2)) * grain_initial_height

    return grain_mass / grain_volume

def init_motor(motor_args: args.Args.Motor) -> rocketpy.SolidMotor:
    motor = rocketpy.SolidMotor(
        thrust_source = motor_args.thrust_source,
        burn_time = motor_args.burn_time,
        dry_mass = motor_args.dry_mass,
        
        grain_number = motor_args.grain_number,
        grain_separation = motor_args.grain_separation,
        grain_outer_radius = motor_args.grain_outer_radius, 
        grain_initial_inner_radius = motor_args.grain_initial_inner_radius,
        grain_initial_height = motor_args.grain_initial_height,

        grains_center_of_mass_position = motor_args.grains_center_of_mass_position,
        center_of_dry_mass_position = motor_args.center_of_dry_mass_position,
        dry_inertia = calculate_moment_of_inertia(motor_args.grain_number, motor_args.grain_outer_radius, motor_args.grain_initial_height, motor_args.grain_separation, motor_args.grain_mass, motor_args.dry_mass, 0.002),
        grain_density = calculate_density(motor_args.grain_outer_radius, motor_args.grain_initial_inner_radius, motor_args.grain_initial_height, motor_args.grain_mass),
        
        nozzle_radius = motor_args.nozzle_radius, 
        nozzle_position = 0, 

        interpolation_method = "linear", 
        coordinate_system_orientation = "nozzle_to_combustion_chamber"
    )

    return motor