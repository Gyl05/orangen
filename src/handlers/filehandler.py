import os
from base.web import RequestHandler


class FileHandler(RequestHandler):
    async def get(self):
        self.write({'code': 200, 'msg': '下载文件'})
    
    async def post(self):
        if self.request.files:
            for filename, real_name_body in self.request.files.items():
                tmpdir = os.path.join(os.path.dirname(__file__), 'tmpfiledir')
                if not os.path.exists(tmpdir):
                    os.mkdir(tmpdir)
                with open(os.path.join(tmpdir, real_name_body[0]['filename']), 'wb') as f:
                    f.write(real_name_body[0]['body'])
        self.write({'code': 200, 'msg': f'上传文件{filename}'})
