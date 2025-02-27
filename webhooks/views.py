from rest_framework import views, response, status


class WebhookOrderView(views.APIView):

    def post(self, request):
        data = request.data

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
