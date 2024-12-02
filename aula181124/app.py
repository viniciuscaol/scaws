import boto3
from urllib.parse import urlparse

sqs = boto3.client('sqs', region_name='us-east-1') 

# Cria a fila SQS
response = sqs.create_queue(
    QueueName='Ada_Fila',
    Attributes={
        'DelaySeconds': '5'  # Atraso opcional para as mensagens
    }
)

# Obtém a URL da fila criada
queue_url = response['QueueUrl']
print("Fila criada com sucesso. URL da Fila:", queue_url)

queue_url = urlparse(queue_url).path.split('/')[-1]

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Aluno Vinicius entregou o projeto'
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,  # Número máximo de mensagens a serem recebidas
    WaitTimeSeconds=10  # Tempo de espera  
)

# Verifica se há mensagens e exibe a primeira
if 'Messages' in response:
    message = response['Messages'][0]
    print("Mensagem recebida:", message['Body'])

    
    # sqs.delete_message(
    #     QueueUrl=queue_url,
    #     ReceiptHandle=message['ReceiptHandle']
    # )
    print("Mensagem processada com sucesso.")
else:
    print("Nenhuma mensagem encontrada na fila.")

# sqs = boto3.client('sqs', region_name='us-east-1')

# sqs.delete_queue(QueueUrl=queue_url)
# print("Fila excluída com sucesso.")