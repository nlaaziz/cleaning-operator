# cleaning-operator
# cleaning-operator

DockerHub cleaning-operator image url:

https://hub.docker.com/repository/docker/nlaaziz/cleaning-operator


## IDEA

This operator ensures that your openshift cluster is cleaned when resources are no longuer used or needed.
An expiry date is set by the creator of the resource at creation time ( or a default value is set in custom resource definition), then the operator deletes 'out of date' objects.

This operator is in developement process
