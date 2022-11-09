from base.web import RequestHandler


class FileHandler(RequestHandler):
    async def get(self):
        self.write({'code': 200, 'msg': '下载文件'})
    
    async def post(self):
        self.write({'code': 200, 'msg': '上传文件'})
