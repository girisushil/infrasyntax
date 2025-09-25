
(This file remains the same as the previous "detailed implementation")
import re

def segment_nginx(content):
pattern = re.compile(
r"((?:^\s*#.\n))"
r"(\sserver\s{"
r"(?:[^{}]|{(?:[^{}]|{(?:[^{}]|{[^{}]})})})"
r"\s})",
re.MULTILINE
)
matches = pattern.findall(content)
if not matches: return [{"comments": "", "code": content}]
return [{"comments": match[0].strip(), "code": "".join(match).strip()} for match in matches]

def segment_dockerfile(content):
stages = re.split(r'\n\s*FROM\s+', content, flags=re.IGNORECASE)
if len(stages) <= 1: return [{"comments": "", "code": content}]
blocks = []
for i, stage in enumerate(stages):
if i == 0 and stage.strip() == "": continue
code = f"FROM {stage.strip()}" if i > 0 else stage.strip()
lines = stage.strip().split('\n')
comments = "\n".join([line.strip() for line in lines if line.strip().startswith('#')])
blocks.append({"comments": comments, "code": code})
return blocks

def segment_yaml(content):
documents = content.split('\n---')
if len(documents) <= 1: return [{"comments": "", "code": content}]
return [{"comments": "", "code": f"---{doc}".strip()} for doc in documents if doc.strip()]

def segment_file(content, file_type):
file_type = file_type.lower() if file_type else ""
if 'nginx.conf' in file_type or '.conf' in file_type: return segment_nginx(content)
if 'dockerfile' in file_type: return segment_dockerfile(content)
if '.yml' in file_type or '.yaml' in file_type: return segment_yaml(content)
return [{"comments": "", "code": content}]
