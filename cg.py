#!/usr/bin/env python
import os
from string import Template

opts = {"module_name": "visitor", "filename": "Visitor", "name": "visitor", "display_name": "测试模块",
         "package_name": "com.dj.codeg.m","entity":"test.entity","system_package":"com.dj.codeg","request_path_prefix":"/"}

basedirs =   [ {
    "source":"./temp/backend",
    "target":"./src/main/java"+"/"+opts['package_name'].replace(".","/"),
},{
    "source":"./temp/web",
    "target":"./web/src/m",
},{
    "source":"./temp/futter",
    "target":"./app/codeg/lib/m",
}]


def cg(basedir, distdir, param):
    for entry in os.scandir(basedir):
        if entry.is_dir():
            cg(basedir + "/" + entry.name, distdir + "/" + entry.name,param);
        else:
            path_template = Template(distdir)
            pathname = path_template.substitute(param)
            os.makedirs(pathname,exist_ok=True);
            filename_template = Template(distdir + "/" + entry.name)
            filename = filename_template.substitute(param)
            #print("filename"+filename);
            f = open(basedir + "./" + entry.name, encoding='utf8')
            file_template = Template(f.read())
            filecontent = file_template.substitute(param)
            print("create:" + filename);
            # print(filecontent);
            distfile = open(filename, "w", encoding='utf8')
            distfile.write(filecontent)
            distfile.close()

def help():
    pass

if __name__ == "__main__":
    print("=======================================================================")
    for d in basedirs:
        cg(d["source"],d["target"],opts)
    print("=======================================================================")