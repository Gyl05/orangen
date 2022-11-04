from base.web import BaseRequestHandler
from models.site import WebsiteModel

class WebSiteHandler(BaseRequestHandler):

    async def post(self):
        sitename = self.request.json_args.get("sitename")
        uri = self.request.json_args.get("uri")
        sitemodel = WebsiteModel()
        msg, res = await sitemodel.create_site(sitename, uri)
        self.write({'code': 201, 'content': msg})
    
    async def get(self):
        sitemodel = WebsiteModel()
        msg, res = await sitemodel.get_all_site()
        self.write({'code': 200, 'content': res})