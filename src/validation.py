from training_Validation_insertion import train_validation
from flask import Response
from parameters import read_params
import argparse


def validationRouteClient(config_path):
    try:
        config = read_params(config_path)
        path = config['data_source']['batch_files']

        train_valObj = train_validation(path)  # object initialization
        train_valObj.train_validation()  # calling the training_validation function

    except ValueError:
        return Response("Error Occurred! %s" % ValueError)

    except KeyError:
        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:
        return Response("Error Occurred! %s" % e)

    return Response("Validation successful!!")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    parsed_args = args.parse_args()
    validationRouteClient(config_path=parsed_args.config)