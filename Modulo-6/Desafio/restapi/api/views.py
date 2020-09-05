
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    if request.method == 'POST':
        question = request.data['question']
        result = [item for items, i in Counter(question).most_common()
                for item in [items] * i]

        return Response({'solution': result})