import urllib.request, json, os

master_url = "https://ci.xwiki.org/job/XWiki/job/xwiki-platform/api/json?pretty=true"

try:
    os.remove("./script/liens_versions.txt")
except OSError as e:
    print(e.errno)


with urllib.request.urlopen(master_url) as url:
    data = json.loads(url.read().decode())
    jobs = data["jobs"]
    versions_file = open("./script/liens_versions.txt","a")
    for job in jobs:
        path = job["url"] + "api/json?pretty=true"
        versions_file.write(path + "\n")
    versions_file.close