import urllib.request, json, os

try:
    os.remove("./script/liens_builds.txt")
except OSError as e:
    print(e.errno)

with open('./script/liens_versions.txt') as lines:
    for line in lines:
        with urllib.request.urlopen(line) as url:
            data = json.loads(url.read().decode())
            builds = data['builds']

            save_file = open("./script/liens_builds.txt","a")

            for build in builds:
                path = build['url'] + "api/json?pretty=true"
                #print(path)
                save_file.write(path + "\n")

            #print("\n")

save_file.close

messages = []
commits = []
files = []

with open('./script/liens_builds.txt') as lines:
    for line in lines:
        with urllib.request.urlopen(line) as url:
            data = json.loads(url.read().decode())
            changeSets = data['changeSets']

            for changeSet in changeSets:
                items = changeSet['items']
                for item in items:
                    msg = item['msg'].split(':')[0]
                    if "XWIKI-" in msg:
                        messages.append(msg)
                        commits.append(item['commitId'])
                        files.append(item['affectedPaths'])

try:
    os.remove("Resultats_protocole_3.csv")
except OSError as e:
    print(e.errno)

res = open("Resultats_protocole_3.csv","a")
res.write("Issue key;Commit ID;Associated Files\n")
for i in range (0, len(messages)):
    res.write(messages[i] + ";" + commits[i] + ";" +str(files[i]) + "\n")