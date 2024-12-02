import boto3
from urllib.parse import urlparse
import Criar_Fila as cf

queue_url = cf.queue_url

queue_url = urlparse(queue_url).path.split('/')[-1]

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Aluno Vinicius entregou o projeto'
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])