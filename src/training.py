from trainingModel import trainModel
from flask import Response


def trainRouteClient():
    try:
        trainModelObj = trainModel()  # object initialization
        trainModelObj.trainingModel()  # training the model for the files in the table

    except ValueError:
        return Response("Error Occurred! %s" % ValueError)

    except KeyError:
        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:
        return Response("Error Occurred! %s" % e)

    return Response("Training successful!!")


trainRouteClient()
