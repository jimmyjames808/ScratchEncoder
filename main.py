import Project
from zipfile import ZipFile
import os
import json


class ScratchProj:
    """
    ScratchProj Class
    """

    def __init__(self, Background: str, Sprites=[], Costumes: list = [], Sounds: list = [], monitors: list = [],
                 Blocks: list = [], Variables: list=[], Lists: list=[]):
        if Sprites is None:
            Sprites = []
        self.monitors = []
        for monitor in monitors:
            self.monitors.append(monitor)
        self.meta = Project.Meta(semver="3.0.0", vm="2.3.0",
                                 agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
        self.Background = Project.Costume(name="Background", fileName=Background, rotationCenterX=363.5,
                                          rotationCenterY=360, bitmapResolution=2)
        self.Costumes = {self.Background.name: self.Background}
        for costume in Costumes:
            self.Costumes[costume.name] = costume
        self.Variables = []
        for variable in Variables:
            self.Variables.append(variable)
            self.monitors.append(variable.monitor)
        self.Lists = []
        for slist in Lists:
            self.Variables.append(slist)
            self.monitors.append(slist.monitor)
        self.Sounds = {}
        for sound in Sounds:
            self.Sounds[sound.name] = sound

        self.Blocks = {}
        for block in Blocks:
            self.Blocks[block.id] = block

        self.Sprites = {
            "Stage": Project.Target(isStage="true", name="Stage", variables=self.Variables, lists=self.Lists, broadcasts=[], blocks=[],
                                    comments=[], currentCostume=0, costumes=[self.Costumes.get("Background")],
                                    sounds=[], volume=100, layerOrder=0, tempo=60, videoTransparency=50,
                                    videoState="on", textToSpeechLanguage="null")}
        for sprite in Sprites:
            self.Sprites[sprite.name] = sprite

        self.targets = []
        for sprite in self.Sprites:
            self.targets.append(self.Sprites[sprite])

        self.targets = Project.Targets(targets=self.targets)

    def addVariable(self, Variable: Project.Variable):
        """
        :param Variable:
        """
        self.Variables.append(Variable)
        self.monitors.append(Variable.monitor)
        for Sprite in self.Sprites:
            self.Sprites[Sprite].variables.append(Variable)

    def addList(self, List: Project.List):
        """
        :param List:
        """
        self.Lists.append(List)
        self.monitors.append(List.monitor)
        for Sprite in self.Sprites:
            self.Sprites[Sprite].lists.append(List)

    def Encode(self, filePath):
        """
        :param filePath:
        """
        self.monitors = Project.Monitors(monitors=self.monitors)
        self.project = Project.Project(meta=self.meta, targets=self.targets, monitors=self.monitors)
        with open(f'{filePath}/project.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.project.format()).replace(': ', ':').replace(', ', ',').replace('"true"',
                                                                                                    'true').replace(
                '"false"', 'false').replace('"null"', 'null').replace('"warp": false', '"warp": "false"').replace(
                '"warp": true', '"warp": "true"').replace('"hasnext": true', '"hasnext": "true"').replace(
                '"hasnext": false', '"hasnext": "false"').replace('KHTML,', 'KHTML, '))

        with ZipFile(f'{filePath}/testing.sb3', 'w') as zip_object:
            zip_object.write(f'{filePath}/project.json')
            directory = os.fsencode("resources")
            for file in os.listdir(directory):
                zip_object.write(f"resources/{os.fsdecode(file)}")


Variable1ID = Project.newId()
ScratchProj = ScratchProj(Background="Image1.jpg", Variables=[Project.Variable(name="Var", sid=Variable1ID, value=4)])
ScratchProj.Sounds["pop"] = Project.Sound(name="pop", fileName="Sound1.wav", sformat="", rate=48000, sampleCount=1123)
Block1ID = Project.newId()
ScratchProj.Blocks[Block1ID] = Project.Block(sid=Block1ID, opcode="looks_nextbackdrop", snext="null", parent="null",
                                             inputs=[], fields=[], shadow="false", coords=[242, 168])
ScratchProj.Sprites.get("Stage").sounds.append(ScratchProj.Sounds.get("pop").format())
ScratchProj.Sprites.get("Stage").blocks[Block1ID] = ScratchProj.Blocks.get(Block1ID).format()
ScratchProj.Encode("ScratchProj")
