from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from emisora.models import Programa
import datetime, json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.


def index(request):
	return render(request, 'emisora/index.html')

def audio(request):
	return render(request, 'emisora/audio.html')

def parrilla(request):
	return render(request, 'emisora/parrilla/index.html')

def play(request):
	return render(request, 'emisora/play/index.html')



@xframe_options_exempt
@csrf_exempt
def get_parrilla(request):
	# La peticion debe ser en metodo GET
	if request.method == "GET":
		#ano = request.GET.get("ano")
		#mes = request.GET.get("mes")
		#dia = request.GET.get("dia")

		try:
			#ano = int(ano)
			#mes = int(mes)
			#dia = int(dia)
			#programas = Programa.objects.filter(fecha_inicio=datetime.date(ano, mes, dia), habilitado=True)
			programas = Programa.objects.all()
			data = []
			for programa in programas:
				data.append({
					'categoria': programa.subcategoria.categoria.nombre,
					'subcategoria':programa.subcategoria.nombre,
					'nombre':programa.nombre,
					'descripcion':programa.descripcion,
					'fecha_inicio':programa.fecha_inicio,
					'fecha_final':programa.fecha_final,
					'imagen_banner':programa.imagen_banner.url,
					'tipo_programa':programa.tipo_programa,
					'url_pregrabado':programa.url_pregrabado,
				})

			response = HttpResponse(json.dumps(data, cls=DjangoJSONEncoder))
			response['Access-Control-Allow-Origin'] = '*'
			return response

		except Exception as e:
			response = JsonResponse({'status':'error', 'response':'No se encuentran registros de programas o ' + str(e)})
			response['Access-Control-Allow-Origin'] = '*'
			return response