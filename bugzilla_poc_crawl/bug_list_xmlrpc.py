import xmlrpc.client

bugzilla = xmlrpc.client.ServerProxy("https://bugzilla.redhat.com/xmlrpc.cgi")

# 构造查询条件
query = {"status": ["VERIFIED"]}

# 调用Bug.search方法并传入查询条件
bug_list = bugzilla.Bug.search(query)

for bug in bug_list['bugs']:
    # 打印Bug信息
    print(bug['id'])
    # print("Bug ID:", bug["id"])
    # print("Summary:", bug["summary"])

print(len(bug_list['bugs']))