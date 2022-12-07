from rest_framework import serializers


class CantSubscribeToYourSelf(serializers.ValidationError):
    ...
