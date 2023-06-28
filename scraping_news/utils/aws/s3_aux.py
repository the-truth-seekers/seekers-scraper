import boto3


# Definir credenciais Aws (cat .aws/credentials) no diretório home do usuário na pasta '.aws' no arquivo credentials
# Obs: Em caso de erro formatar o arquivo em ANSI
def send_file_to_bucket(bucket_name: str, filepath: str, estrutura_s3: str = ''):
    s3 = boto3.client('s3')
    s3.upload_file(filepath, bucket_name, estrutura_s3)
