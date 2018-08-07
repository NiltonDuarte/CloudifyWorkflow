from cloudify.decorators import workflow
from cloudify.workflows import ctx

@workflow
def my_workflow_method(param, **kwargs):
    mparam = param