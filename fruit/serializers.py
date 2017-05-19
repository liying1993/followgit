from rest_framework import serializers

class Fruit(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name
class FruitSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)