import rocketpy
import args


def init_flight(flight_args: args.Args.Flight, environment: rocketpy.Environment, rocket: rocketpy.Rocket) -> rocketpy.Flight:
    flight = rocketpy.Flight(
        rocket = rocket,
        environment = environment,
        rail_length = flight_args.rail_length,
        inclination = flight_args.inclination,
        heading = flight_args.heading
    )

    return flight