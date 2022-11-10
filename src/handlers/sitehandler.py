from base.web import BaseRequestHandler, Param, define_api
from models.site import WebsiteModel

class WebSiteHandler(BaseRequestHandler):

    @define_api(
        name="新增站点",
        params=[
            Param(name="sitename", required=True, type=str, label="站点名称"),
            Param(name="uri", required=True, type=str, label="地址")
        ],
        return_msg={'code': 201, 'content': "xxx"}
    )
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
    
    async def delete(self):
        sitemodel = WebsiteModel()
        ids:list = self.get_arguments('id')
        delete_ids = await sitemodel.delete_by_id(*ids)
        self.write({'code': 204, 'content': delete_ids})