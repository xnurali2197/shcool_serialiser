class SchoolSerializer(serializers.ModelSerializer):
    full_info = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'city', 'full_info']

    def get_full_info(self, obj):
        return f"{obj.name} - {obj.city}"
