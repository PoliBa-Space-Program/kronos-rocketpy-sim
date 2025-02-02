import rocketpy
import args


def init_rocket(rocket_args: args.Args.Rocket, motor) -> rocketpy.Rocket:
    rocket = rocketpy.Rocket(
        radius = rocket_args.radius,
        mass = rocket_args.mass,
        inertia = [rocket_args.inertia_1, rocket_args.inertia_2, rocket_args.inertia_3],
        power_off_drag = rocket_args.power_off_drag,
        power_on_drag = rocket_args.power_on_drag,
        center_of_mass_without_motor = rocket_args.center_of_mass_without_motor,
        coordinate_system_orientation = "nose_to_tail"
    )
    rocket.add_motor(motor, rocket_args.motor_position)
    rocket.add_nose(rocket_args.nose_length, rocket_args.nose_kind, rocket_args.nose_position)
    rocket.add_trapezoidal_fins(
        n = rocket_args.fins_number, 
        root_chord = rocket_args.fin_root_chord, 
        tip_chord = rocket_args.fin_tip_chord, 
        span = rocket_args.fin_span, 
        position = rocket_args.fin_position, 
        sweep_length = rocket_args.fin_sweep_length
    )
    rocket.add_tail(
        top_radius = rocket_args.tail_top_radius, 
        bottom_radius = rocket_args.tail_bottom_radius, 
        length = rocket_args.tail_length, 
        position = rocket_args.tail_position
    )
    rocket.add_parachute(
        name = "Main", 
        cd_s = rocket_args.main_chute_cd, 
        trigger = rocket_args.main_chute_trigger, 
        sampling_rate = rocket_args.trigger_sampling_rate, 
        lag = 1.5, 
        noise = (0, 8.3, 0.5)
    )
    rocket.add_parachute(
        name = "Drogue", 
        cd_s = rocket_args.drogue_chute_cd, 
        trigger = "apogee", 
        sampling_rate = rocket_args.trigger_sampling_rate, 
        lag = 1.5, 
        noise = (0, 8.3, 0.5)
    )
    rocket.set_rail_buttons(
        upper_button_position = rocket_args.upper_rail_button_position, 
        lower_button_position = rocket_args.lower_rail_button_position, 
        angular_position = 45
    )

    return rocket