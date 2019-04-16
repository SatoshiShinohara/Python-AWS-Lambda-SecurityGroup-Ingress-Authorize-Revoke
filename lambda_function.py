import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # 対象となるセキュリティグループのID
    Target_GroupId = 'sg-XXXXXXXXXXXXXXXX'
    
    # 追加・削除対象のIPアドレス・ポート
    Authorize_Revoke_IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'description 1/2'
                },
            ],
            'FromPort': 10000,
            'ToPort': 10001,
        },
        {
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'description 2/2'
                },
            ],
            'FromPort': 20000,
            'ToPort': 20001,
        },
    ]
    
    if event['action'] == 'authorize':
        # セキュリティグループに許可IPアドレスを追加する
        ec2.authorize_security_group_ingress(
            GroupId=Target_GroupId,
            IpPermissions=Authorize_Revoke_IpPermissions
        )
    elif event['action'] == 'revoke':
        # セキュリティグループから許可IPアドレスを削除する
        ec2.revoke_security_group_ingress(
            GroupId=Target_GroupId,
            IpPermissions=Authorize_Revoke_IpPermissions  
        )
  
