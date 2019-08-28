import os
from openstack import connection
import globalVariable

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', globalVariable.cdnPath)

# token认证
# username = "xxxxxxxxxxx"
# password = "xxxxxxxxxxx"
# projectId = "xxxxxxxxxxx"
# userDomainId = "xxxxxxxxxxx"
# auth_url = "xxxxxxxxxxx"
#
# conn = connection.Connection(
#     auth_url=auth_url,
#     user_domain_id=userDomainId,
#     project_id=projectId,
#     username=username,
#     password=password
# )

# AKSK认证
projectId = globalVariable.projectId
cloud = globalVariable.cloud   # cdn use: cloud = "myhwclouds.com"
region= globalVariable.region    # example: region = "cn-north-1"
AK = globalVariable.AK
SK = globalVariable.SK

conn = connection.Connection(
              project_id=projectId,
              cloud=cloud,
              region=region,
              ak=AK,
              sk=SK)



