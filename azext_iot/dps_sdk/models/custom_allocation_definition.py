# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CustomAllocationDefinition(Model):
    """Custom allocation definition.

    :param webhook_url: The webhook URL used for allocation requests.
    :type webhook_url: str
    :param api_version: The API version of the provisioning service types
     (such as IndividualEnrollment) sent in the custom allocation request.
     Supported versions include: "2018-09-01-preview"
    :type api_version: str
    """

    _validation = {
        'webhook_url': {'required': True},
        'api_version': {'required': True},
    }

    _attribute_map = {
        'webhook_url': {'key': 'webhookUrl', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
    }

    def __init__(self, webhook_url, api_version):
        super(CustomAllocationDefinition, self).__init__()
        self.webhook_url = webhook_url
        self.api_version = api_version
