from rest_framework import serializers
from .models import Library,Student

class LibrarySerializers(serializers.ModelSerializer):
    ## Validators 
    def start_with_P(value):
        if value[0].upper()!= 'P':
            raise serializers.ValidationError("Book Name Should We Start With P")
        else:
            return value
    b_name = serializers.CharField(validators=[start_with_P])

    class Meta:
        model = Library
        fields = '__all__'

    ## Name Validations
    def validate(self, data):
        bn = data.get('b_name')
        if bn.title() == 'Python Programming':
            raise serializers.ValidationError("This Name is Already Register")
        else:
            return data
    
    ## Validators


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['id','stu_name','help','library.b_name']