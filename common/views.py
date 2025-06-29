# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Serializer

class Datas(APIView):
	def get(self, request):
		datas = Model.objects.all()
		serializer = Serializer(datas) # QuerySet이 2개 이상일 때 Object->JSON
		return Response(serializer.data) # serialized된 데이터를 return

	def post(self, request):
		data = request.data => JSON
		datas = Model.objects.create(Serializer(data)) # JSON->Objects

	def put(self, request):
		data = request.data => JSON
		datas = Model.objects.update(Serializer(data)) # JSON->Objects

	def delete(self, request):
		JSON => ID값 뽑아와서 
		data = Model.objects.get(id=id)
		data.delete()  # 객체 삭제 -> dir()