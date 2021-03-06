#!/bin/sh
env

if [ "x$GP_MODULE_SPECIFIC_CONTAINER" = "x" ]; then
    # Variable is empty
    echo "== no MODULE_SPECIFIC_CONTAINER specified. Using default for test purposes "
    GP_MODULE_SPECIFIC_CONTAINER="`python /usr/local/bin/make_repo_name.py $GP_MODULE_LSID $GP_MODULE_NAME`"
fi

CONTAINER_TAG=$GP_MODULE_SPECIFIC_CONTAINER
CONTAINER_VERSION=1
#PROFILE="--profile genepattern"
PROFILE=""

aws --region us-east-1 ecr describe-images --repository-name $CONTAINER_TAG  > repo.json 
if [ -s repo.json ];
then
   echo "Container already exists in ECR"
   exit
else
   echo "== saving in ECR as $GP_MODULE_SPECIFIC_CONTAINER =="
   echo "false"
fi

# get the id of the last container run via a docker call and strip the part we want with python
idvar="`python /usr/local/bin/getContainerId.py`" 

# commit the container as a new image
docker commit $idvar $CONTAINER_TAG

echo "Committed $CONTAINER_TAG locally to docker"

# login to the AWS ECR
aws --region us-east-1 ecr get-login --no-include-email  > dockerlogin.sh
sh dockerlogin.sh

# create a repository for this container if it doesn't already exist

aws --region us-east-1 ecr create-repository --repository-name $CONTAINER_TAG  > repos.json
echo "repo creation returned..."
more repos.json

AWS_ACCOUNT="`python /usr/local/bin/get_aws_account.py`"
echo " +++  identified aws account as $AWS_ACCOUNT "

# tag the just-saved container for the ECR
# the aws id # is hard coded - should get it dynamically
docker tag $CONTAINER_TAG 718039241689.dkr.ecr.us-east-1.amazonaws.com/$CONTAINER_TAG:$CONTAINER_VERSION

# push into the ECR
docker push 718039241689.dkr.ecr.us-east-1.amazonaws.com/$CONTAINER_TAG:$CONTAINER_VERSION

# announce success
echo "Saved 718039241689.dkr.ecr.us-east-1.amazonaws.com/$CONTAINER_TAG:$CONTAINER_VERSION  container in the ECR"

