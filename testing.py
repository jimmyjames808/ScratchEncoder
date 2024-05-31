import json
import os
from zipfile import ZipFile
import Project

import glob

files = glob.glob("resources/*")
for f in files:
    os.remove(f)

Block1ID = Project.newId()
Block2ID = Project.newId()
Comment1ID = Project.newId()

Sound1 = Project.Sound(name="pop", fileName="Sound1.wav", sformat="", rate=48000, sampleCount=1123)

Costume1 = Project.Costume(name="backdrop1", fileName="Image1.jpg", rotationCenterX=363.5, rotationCenterY=360, bitmapResolution=2)

Comment1 = Project.Comment(sid=Comment1ID, blockId=Block1ID, x=561.3483796296296, y=260.74074074074076, width=200, height=200, minimized="false", text="hello")

Field1 = Project.Field(name="BACKDROP", value="backdrop1")

Block2 = Project.Block(sid=Block2ID, opcode="looks_backdrops", snext="null", parent=Block1ID, inputs=[], fields=[Field1], shadow="true")

Input1 = Project.Input(name="BACKDROP", shadow=1, value="Hello")

Block1 = Project.Block(sid=Block1ID, opcode="looks_switchbackdropto", snext="null", parent="null", inputs=[Input1], fields=[], shadow="false", comment=Comment1ID, coords=[242, 253])

Stage = Project.Target(isStage="true", name="Stage", variables=[], lists=[], broadcasts=[], blocks=[Block1, Block2], comments=[Comment1], currentCostume=0, costumes=[Costume1], sounds=[Sound1], volume=100, layerOrder=0, tempo=60, videoTransparency=50, videoState="on", textToSpeechLanguage="null")

targets = Project.Targets(targets=[Stage])

monitors = Project.Monitors(monitors=[])

meta = Project.Meta(semver="3.0.0", vm="2.3.0", agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

project = Project.Project(meta=meta, monitors=monitors, targets=targets)

print(json.dumps(project.format()).replace(': ', ':').replace(', ', ',').replace('"true"', 'true').replace('"false"', 'false').replace('"null"', 'null').replace('"warp": false', '"warp": "false"').replace('"warp": true', '"warp": "true"').replace('"hasnext": true', '"hasnext": "true"').replace('"hasnext": false', '"hasnext": "false"'))

with open('project.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(project.format()).replace(': ', ':').replace(', ', ',').replace('"true"', 'true').replace('"false"', 'false').replace('"null"', 'null').replace('"warp": false', '"warp": "false"').replace('"warp": true', '"warp": "true"').replace('"hasnext": true', '"hasnext": "true"').replace('"hasnext": false', '"hasnext": "false"').replace('KHTML,', 'KHTML, '))

with ZipFile('testing.sb3', 'w') as zip_object:
    zip_object.write('project.json')
    directory = os.fsencode("resources")
    for file in os.listdir(directory):
        zip_object.write(f"resources/{os.fsdecode(file)}")


