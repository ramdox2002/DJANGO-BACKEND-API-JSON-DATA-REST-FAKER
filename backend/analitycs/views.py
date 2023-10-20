from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GenerateDataAnalitycs

class UpdateGenerateData(APIView):
    def get(self, request):
        generate_data = GenerateDataAnalitycs.objects.first()
        views = generate_data.views
        json_generated = generate_data.json_generated


        return Response({
            "views": views,
            "jsonGenerated": json_generated
        })

    def post(self, request):
        field_to_update = request.data.get('field_to_update')  # 'views' or 'json_generated'

        if field_to_update not in ['views', 'json_generated']:
            return Response({'error': 'Invalid field name'}, status=400)

        try:
            # Intenta obtener un objeto GenerateDataAnalitycs existente
            generate_data = GenerateDataAnalitycs.objects.first()

            if generate_data is None:
                # Si no existe, crea uno nuevo con valores iniciales
                generate_data = GenerateDataAnalitycs(
                    views=0,
                    json_generated=0
                )

            # Aumentar en 1 el valor del campo especificado
            if field_to_update == 'views':
                generate_data.views += 1
            elif field_to_update == 'json_generated':
                generate_data.json_generated += 1

            # Guardar el objeto actualizado
            generate_data.save()

            return Response({'success': f'{field_to_update} updated successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
