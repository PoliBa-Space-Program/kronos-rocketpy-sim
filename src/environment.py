import rocketpy
import args


def init_environment(environment_args: args.Args.Environment) -> rocketpy.Environment:
    datetime = [
        int(environment_args.date_and_time.split('-')[0]),
        int(environment_args.date_and_time.split('-')[1]),
        int(environment_args.date_and_time.split('-')[2].split('T')[0]),
        int(environment_args.date_and_time.split('-')[2].split('T')[1].split(':')[0])
    ]

    environment = rocketpy.Environment(
        latitude = environment_args.latitude,
        longitude = environment_args.longitude,
        elevation = environment_args.elevation,
        date = datetime,
        timezone = environment_args.timezone
    )
    environment.set_atmospheric_model(
        type = environment_args.atmospheric_model_type,
        file = environment_args.atmospheric_model_file
    )

    return environment