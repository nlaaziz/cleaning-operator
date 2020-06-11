# cleaning-operator

DockerHub cleaning-operator image url:

https://hub.docker.com/repository/docker/nlaaziz/cleaning-operator


## IDEA

This operator ensures that your openshift cluster is cleaned when resources are no longer used or needed.
An expiry date is set by the creator of the resource at creation time ( or a default value is set in the Custom Resource Definition), then the operator deletes 'out of date' objects.

This operator is in the developement process

## ansible based openshift operators documentation:

https://docs.openshift.com/container-platform/4.4/operators/operator_sdk/osdk-ansible.html
