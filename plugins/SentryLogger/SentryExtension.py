from cura import ApplicationMetadata

from UM.Application import Application
from UM.Extension import Extension


try:
    import sentry_sdk

    from sentry_sdk.hub import Hub
    from sentry_sdk.utils import event_from_exception
    from sentry_sdk import configure_scope
    
    from .SentryCredentials import SENTRY_SDK_URL

    sentry_env = "production"
    if ApplicationMetadata.CuraVersion == "master":
        sentry_env = "development"
    try:
        if ApplicationMetadata.CuraVersion.split(".")[2] == "99":
            sentry_env = "nightly"
    except IndexError:
        pass
    
    sentry_sdk.init(SENTRY_SDK_URL,
                    environment = sentry_env,
                    release = "cura%s" % ApplicationMetadata.CuraVersion,
                    default_integrations = False,
                    max_breadcrumbs = 300,
                    server_name = "cura")
    
    with_sentry_sdk = True
except:
    with_sentry_sdk = False


 
class SentryExtension(Extension):

    def __init__(self, parent = None):
        Extension.__init__(self)

        self._application.initializationFinished.connect(self._onAppInitialized)

    def _onAppInitialized(self):
        pass
    
    def getScope(self):
        return 


