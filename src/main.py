import rocketpy.plots
import rocketpy.plots.flight_plots
import json
import environment, motor, rocket, flight
import rocketpy
import sys, datetime, os
import args


def main(file: str, path: str):
    rocketpy_args = None
    with open(file, 'r') as f:
        rocketpy_args = args.Args(json.loads(f.read()))

    env = environment.init_environment(rocketpy_args.environment)
    solid_motor = motor.init_motor(rocketpy_args.motor)
    dr_v1 = rocket.init_rocket(rocketpy_args.rocket, solid_motor)
    sim1 = flight.init_flight(rocketpy_args.flight, env, dr_v1)

    rocketpy.plots.flight_plots._FlightPlots(sim1)

    pathname = datetime.datetime.now().isoformat().replace('-', '_').replace(':', '_').split('.')[0]

    os.makedirs(os.path.join(path, pathname))

    sim1.export_data(os.path.join(path, pathname, 'flight.csv'), 'x', 'y', 'z', 'vx', 'vy', 'vz', 'e0', 'e1', 'e2', 'e3', 'w1', 'w2', 'w3', 'latitude', 'longitude', 'wind_velocity_x', 'wind_velocity_y', 'density', 'pressure', 'dynamic_viscosity', 'speed_of_sound', 'ax', 'ay', 'az', 'alpha1', 'alpha2', 'alpha3', 'speed', 'horizontal_speed', 'acceleration', 'path_angle', 'attitude_vector_x', 'attitude_vector_y', 'attitude_vector_z', 'attitude_angle', 'lateral_attitude_angle', 'phi', 'theta', 'psi', 'R1', 'R2', 'R3', 'M1', 'M2', 'M3', 'aerodynamic_lift', 'aerodynamic_drag', 'aerodynamic_bending_moment', 'aerodynamic_spin_moment', 'rail_button1_normal_force', 'rail_button1_shear_force', 'rail_button2_normal_force', 'rail_button2_shear_force', 'rotational_energy', 'translational_energy', 'kinetic_energy', 'potential_energy', 'total_energy', 'thrust_power', 'drag_power', 'attitude_frequency_response', 'omega1_frequency_response', 'omega2_frequency_response', 'omega3_frequency_response', 'static_margin', 'stability_margin', 'stream_velocity_x', 'stream_velocity_y', 'stream_velocity_z', 'free_stream_speed', 'mach_number', 'reynolds_number', 'dynamic_pressure', 'total_pressure', 'angle_of_attack')

    print(pathname)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])