#import boto.sdb

#conn = boto.sdb.connect_to_region('us-west-2',aws_access_key_id='<YOUR_AWS_KEY_ID>',aws_secret_access_key='<YOUR_AWS_SECRET_KEY>')
#print(conn)

from __future__ import print_function
import boto3


def quote(string):
    return string.replace("'", "''").replace('"', '""').replace('`', '``')


def put_attributes(sdb, domain, id, color):
    response = sdb.put_attributes(
        DomainName=domain,
        ItemName=id,
        Attributes=[
            {
                'Name': 'color',
                'Value': color,
                'Replace': True
            },
        ],
    )
    print(response)
    
if __name__ == "__main__":
    domain = "TEST_DOMAIN"
    reg='us-east-1'
    aws_key_id='AKIATOQWG7QP62CTB55S'
    aws_secret_key='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'
    
    sdb = boto3.client('sdb',aws_access_key_id=aws_key_id,aws_secret_access_key=aws_secret_key,region_name=reg)
    response = sdb.create_domain(
        DomainName=domain
    )
    
    print(response)
    
    response = sdb.list_domains()
    print('Domain List :',response)
    
    print("Current domains: %s" % response['DomainNames'])
    '''
    put_attributes(sdb, domain, "id1", "red")
    put_attributes(sdb, domain, "id2", "redblue")
    put_attributes(sdb, domain, "id3", "blue")
    response = sdb.select(
        SelectExpression='select * from %s where color like "%%%s%%"' % (domain, quote('blue')),
    )
    print(response)
    response = sdb.delete_domain(
        DomainName=domain
    )
    print(response)
    '''
