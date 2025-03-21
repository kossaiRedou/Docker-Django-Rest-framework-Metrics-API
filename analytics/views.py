from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SalesData
from .serializers import SalesDataSerializer

@api_view(['GET'])
def list_datasets(request):
    datasets = SalesData.objects.all()
    serializer = SalesDataSerializer(datasets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upload_dataset(request):
    print(request.FILES)  # 🔍 Debug : Voir si le fichier est bien reçu
    
    file = request.FILES.get('file')
    
    if not file:
        return Response({"error": "Aucun fichier reçu. Vérifiez que vous envoyez bien un fichier avec form-data."}, status=400)

    dataset = SalesData.objects.create(name=file.name, file=file)
    return Response({"message": "Dataset uploaded successfully"})


@api_view(['GET'])
def top_products(request, dataset_id):
    dataset = SalesData.objects.get(id=dataset_id)
    top_products = dataset.get_top_products()
    return Response(top_products)
