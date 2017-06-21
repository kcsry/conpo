from lepo.router import Router
from lepo.validate import validate_router
from pkg_resources import resource_filename

from . import handlers

router = Router.from_file(resource_filename('conpo.api', 'swagger.yaml'))
router.add_handlers(handlers)
validate_router(router)
urlpatterns = router.get_urls()
