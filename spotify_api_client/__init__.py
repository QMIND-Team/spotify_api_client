from . import request as RequestModule
from . import url_parser

Request = RequestModule.Request
parse_url = url_parser.parse

client = Request()
get = client.get
search = client.search
search_all = client.search_all
