

from rest_framework import serializers
from problems.models import Question

class QuestionSeriazizer(serializers.ModelSerializer):

    assessment = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:

        model = Question

        fields = "__all__"

        read_only_fields = ["id","assessment","created_at","updated_at","created_by"]