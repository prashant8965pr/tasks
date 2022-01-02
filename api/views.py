import requests
from rest_framework.views import APIView
from django.db.models import Count
from api.models import CardInfo
from api.serializers import CardInfoSerializer, AllCardInfoListSerializer, CardInfoListSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateCardInfoView(APIView):
    @staticmethod
    def post(request):
        serializer = CardInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            url = f"https://lookup.binlist.net/{serializer.validated_data['card_number']}"
            headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
            data = requests.post(url, data={"sample": "data"}, headers=headers)
            if data.status_code == 200:
                url_data = data.json()
                payload = {
                    "scheme": url_data['scheme'],
                    "type": url_data['type'],
                    "bank": url_data['bank']['name']
                }
                return Response(
                    {"success": True, "payload" : payload},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                    {"Error": "Cart number Not Valid"},
                    status=status.HTTP_400_BAD_REQUEST,
                )


class ListCardInfoView(APIView):
    @staticmethod
    def get(_):
        cart_data_list = CardInfo.objects.all().values('card_number').annotate(hits=Count("card_number"))
        all_data = CardInfoListSerializer(cart_data_list, many=True).data
        return Response(
            {"success": True, "payload": all_data},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ListAllCardInfoView(APIView):
    @staticmethod
    def get(_):
        cart_data_list = CardInfo.objects.all()
        all_data = AllCardInfoListSerializer(cart_data_list, many=True).data
        return Response(
            {"success": True, "payload": all_data},
            status=status.HTTP_400_BAD_REQUEST,
        )