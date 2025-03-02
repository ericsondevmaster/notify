import json
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework import views, response, status
from django.conf import settings
from django.template.loader import render_to_string
from webhooks.models import Webhook
from webhooks.messages import outflow_message
from services.callmebot import CallMeBot

logger = logging.getLogger(__name__)


class WebhookOrderView(views.APIView):

    def post(self, request):
        data = request.data

        Webhook.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False),
        )

        product_name = data.get('product')
        quantity = data.get('quantity')
        product_cost_price = data.get('product_cost_price')
        product_selling_price = data.get('product_selling_price')
        total_value = product_selling_price * quantity
        profit_value = total_value - (product_cost_price * quantity)

        message = outflow_message.format(
            product_name,
            quantity,
            total_value,
            profit_value,
        )
        callmebot = CallMeBot()
        callmebot.send_message(message)

        data['total_value'] = total_value
        data['profit_value'] = profit_value

        try:
            # Configuração do email
            msg = MIMEMultipart()
            msg['Subject'] = 'Nova Saída (SGE)'
            msg['From'] = f'SGE <{settings.EMAIL_HOST_USER}>'
            msg['To'] = settings.EMAIL_ADMIN_RECEIVER
            html_content = render_to_string('outflow.html', data)
            msg.attach(MIMEText(html_content, 'html'))

            # Envio do email usando smtplib
            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.starttls()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)

            logger.info("Email enviado com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao enviar email: {e}")

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
