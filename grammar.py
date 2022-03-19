import language_tool_python
import os
import re

# set directory to path of corpus
path = r"C:\Users\mugge\Desktop\Uni\WiSe2021\CLV\PNL\2021 clean\test"
os.chdir(path)

tool = language_tool_python.LanguageTool('en-US')
stopwords = ["et", "al", "WGI", "WGII", "SLCFs", "GHGs", "GHG", "SLCF", "IPBES", "SRCCL", "SROCC", "UNEP", "UNFCCC",
             "DESA", "LTTG", "SED", "SBSTA", "NDCs", "NDC", "GMST", "GMSL", "SROCC"]

def grammar(text):
    tokens = re.findall(r"[\w']+", text)
    matches = 0
    for token in tokens:
        if token not in stopwords:
            matches += len(tool.check(token))
            if len(tool.check(token)) > 0:
                print(token, matches)
    return matches


total = 0
for count, file in enumerate(os.listdir()):
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        print(f"\n-------- FILE {count} --------")
        with open(file_path, 'r', encoding="UTF-8") as f:
            text = f.read()
            total += grammar(text)
print(total)