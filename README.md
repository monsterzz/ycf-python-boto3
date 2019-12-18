# Yandex.Cloud Serverless Functions : Boto3

Small example which shows how to use boto3 to access
Yandex Object Storage.

Prerequisites:

* docker
* make
* zip

To build deployment package:

    make all

Deployment package is 7Mb+, so we need to use Object Storage
to deploy it (at least for the first time).

* create storage bucket in your folder;
* upload `dist.zip` using web console or any S3 compatible client;

In this example we will use `bgleb-dev` as such bucket.

Also you need to have Service Account and access keys to access Object Storage.
It could be created using web console or with `yc` (don't forget to write down your access key and secret key):

    yc iam service-account create --name function-sa
    yc iam access-key create --service-account-name function-sa
    yc resource-manager folder add-access-binding <Folder-Name> \
        --subject serviceAccount:<ServiceAccount-ID> --role editor

To deploy Function with this package:

    yc serverless function create --name boto
    yc serverless function version create       \
        --function-name boto                    \
        --runtime python37                      \
        --entrypoint main.handler               \
        --memory 128M                           \
        --execution-timeout 1s                  \
        --package-bucket-name bgleb-dev         \
        --package-object-name dist.zip          \
        --environment STORAGE_BUCKET=my-bucket  \
        --environment AWS_ACCESS_KEY_ID=XXX     \
        --environment AWS_SECRET_ACCESS_KEY=XXX

Test it:

    yc serverless function invoke --name boto

Get your own invocation URL using:

    yc serverless function get --name boto

**Don't forget to allow unauthorized function invocation**

Documentation: https://cloud.yandex.ru/docs/serverless-functions/
