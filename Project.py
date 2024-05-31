import shutil
import hashlib
import uuid


def newId():
    """
        Generates UUID hex form
    :return:
    """
    return uuid.uuid4().hex


def md5(fileName: str):
    """
        Md5 hasher and file copier
        :param fileName:
        :return:
    """
    if not isinstance(fileName, str):
        raise TypeError

    file_type = fileName.split(sep=".")[1]

    with open(fileName, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    shutil.copy(f"{fileName}", f"resources/{file_hash.hexdigest()}.{file_type}")

    return [f"{file_hash.hexdigest()}", file_type]


class Monitor:
    """
    SB3 Files Monitor Class
    """
    def __init__(self, sid: str, mode: str, opcode: str, params: list, spriteName: str, value, width: int, height: int, x: int, y: int, visible: str, sliderMin: int = 0, sliderMax: int = 100, isDiscrete: str = "true"):
        if not isinstance(sid, str) or not isinstance(mode, str) or not isinstance(opcode, str) or not isinstance(params, list) or not isinstance(spriteName, str) or not isinstance(width, int) or not isinstance(height, int) or not isinstance(x, int) or not isinstance(y, int):
            raise TypeError

        self.id = sid
        self.mode = mode
        self.opcode = opcode
        self.params = {}
        self.spriteName = spriteName
        self.value = value
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.visible = visible
        self.sliderMin = sliderMin
        self.sliderMax = sliderMax
        self.isDiscrete = isDiscrete
        for p in params:
            self.params[params[0]] = params[1]

    def format(self):
        if self.opcode != "data_listcontents":
            return {
                "id": self.id,
                "mode": self.mode,
                "opcode": self.opcode,
                "params": self.params,
                "spriteName": self.spriteName,
                "value": self.value,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                "visible": self.visible,
                "sliderMin": self.sliderMin,
                "sliderMax": self.sliderMax,
                "isDiscrete": self.isDiscrete
            }
        else:
            return {
                "id": self.id,
                "mode": self.mode,
                "opcode": self.opcode,
                "params": self.params,
                "spriteName": self.spriteName,
                "value": self.value,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                "visible": self.visible
            }


class Monitors:
    """
    SB3 Files Monitors Class
    """
    def __init__(self, monitors: list):
        if not isinstance(monitors, list):
            raise TypeError

        self.monitors = []
        for m in monitors:
            self.monitors.append(m.format())


class Meta:
    """
    SB3 Files Meta Class
    """
    def __init__(self, semver: str, vm: str, agent: str):
        if not isinstance(semver, str) or not isinstance(vm, str) or not isinstance(agent, str):
            raise TypeError

        self.semver = semver
        self.vm = vm
        self.agent = agent

    def format(self):
        return {
            "semver": self.semver,
            "vm": self.vm,
            "agent": self.agent
        }


class Targets:
    """
    SB3 Files Targets Class
    """
    def __init__(self, targets: list):
        if not isinstance(targets, list):
            raise TypeError
        self.targets = []
        for t in targets:
            self.targets.append(t.format())


class Target:
    """
    SB3 Files Target Class
    """
    def __init__(self, isStage: str, name: str, variables: list, lists: list, broadcasts: list, blocks: list, comments: list, currentCostume: int, costumes: list, sounds: list, layerOrder: int, volume: int, tempo: int, videoState: str, videoTransparency: int, textToSpeechLanguage: str, visible: str="false", x: int=0, y: int=0, size: int=100, direction: int=90, draggable: str="false", rotationStyle: str="all around"):
        if not isinstance(isStage, str) or not isinstance(name, str) or not isinstance(variables, list) or not isinstance(lists, list) or not isinstance(broadcasts, list) or not isinstance(blocks, list) or not isinstance(comments, list) or not isinstance(currentCostume, int) or not isinstance(costumes, list) or not isinstance(sounds, list) or not isinstance(layerOrder, int) or not isinstance(volume, int) or not isinstance(tempo, int) or not isinstance(videoState, str) or not isinstance(videoTransparency, int) or not isinstance(textToSpeechLanguage, str) or not isinstance(visible, str) or not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int) or not isinstance(direction, int) or not isinstance(draggable, str) or not isinstance(rotationStyle, str):
            raise TypeError

        self.isStage = isStage
        self.name = name
        self.variables = {}
        self.lists = {}
        self.broadcasts = {}
        self.blocks = {}
        self.comments = {}
        self.currentCostume = currentCostume
        self.costumes = []
        self.sounds = []
        self.layerOrder = layerOrder
        self.volume = volume
        self.tempo = tempo
        self.videoState = videoState
        self.videoTransparency = videoTransparency
        self.textToSpeechLanguage = textToSpeechLanguage
        self.visible = visible
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.draggable = draggable
        self.rotationStyle = rotationStyle
        for v in variables:
            self.variables[v.id] = [v.name, v.value]
        for l in lists:
            self.lists[l.id] = [l.name, l.value]
        for b in broadcasts:
            self.broadcasts[b.id] = b.name
        for b in blocks:
            self.blocks[b.id] = b.format()
        for c in comments:
            self.comments[c.id] = c.format()
        for c in costumes:
            self.costumes.append(c.format())
        for s in sounds:
            self.sounds.append(s.format())

    def format(self):
        if self.isStage == "true":
            return {
                "isStage": self.isStage,
                "name": self.name,
                "variables": self.variables,
                "lists": self.lists,
                "broadcasts": self.broadcasts,
                "blocks": self.blocks,
                "comments": self.comments,
                "currentCostume": self.currentCostume,
                "costumes": self.costumes,
                "sounds": self.sounds,
                "volume": self.volume,
                "layerOrder": self.layerOrder,
                "tempo": self.tempo,
                "videoTransparency": self.videoTransparency,
                "videoState": self.videoState,
                "textToSpeechLanguage": self.textToSpeechLanguage
            }
        else:
            return {
                "isStage": self.isStage,
                "name": self.name,
                "variables": self.variables,
                "lists": self.lists,
                "broadcasts": self.broadcasts,
                "blocks": self.blocks,
                "comments": self.comments,
                "currentCostume": self.currentCostume,
                "costumes": self.costumes,
                "sounds": self.sounds,
                "volume": self.volume,
                "layerOrder": self.layerOrder,
                "visible": self.visible,
                "x": self.x,
                "y": self.y,
                "size": self.size,
                "direction": self.direction,
                "draggable": self.draggable,
                "rotationStyle": self.rotationStyle
            }

    def __str__(self):
        return f"I'm ({self.name}) and i'm in layer ({self.layerOrder})"


class Comment:
    """
    SB3 Files Comment Class
    """
    def __init__(self, blockId: str, x, y, width: int, height: int, minimized: str, text: str, sid: str):
        if not isinstance(sid, str) or not isinstance(blockId, str) or not isinstance(width, int) or not isinstance(height, int) or not isinstance(minimized, str) or not isinstance(text, str):
            raise TypeError

        self.id = sid
        self.blockId = blockId
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minimized = minimized
        self.text = text

    def format(self):
        return {
            "blockId": self.blockId,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "minimized": self.minimized,
            "text": self.text
        }


class Variable:
    """
    SB3 Files Variable Class
    """
    def __init__(self, sid: str, name: str, value: int):
        if not isinstance(sid, str) or not isinstance(name, str) or not isinstance(value, int):
            raise TypeError

        self.id = sid
        self.name = name
        self.value = value

    def __str__(self):
        return f"I'm ({self.name}) my id is ({self.id}) and my value is ({self.value})"


class List:
    """
    SB3 Files List Class
    """
    def __init__(self, sid: str, name: str, value: list):
        if not isinstance(sid, str) or not isinstance(name, str) or not isinstance(value, list):
            raise TypeError

        self.id = sid
        self.name = name
        self.value = value

    def __str__(self):
        return f"I'm ({self.name}) my id is ({self.id}) and my value is ({self.value})"


class Broadcast:
    """
    SB3 Files Broadcast Class
    """
    def __init__(self, sid: str, name: str):
        if not isinstance(sid, str) or not isinstance(name, str):
            raise TypeError

        self.id = sid
        self.name = name

    def __str__(self):
        return f"My id is ({self.id}) and my name is ({self.name})"


class Input:
    """
    SB3 Files Input Class
    """
    def __init__(self, name: str, shadow: int, value):
        if not isinstance(name, str) or not isinstance(shadow, int):
            raise TypeError

        self.name = name
        self.shadow = shadow
        self.value = value


class Field:
    """
    SB3 Files Field Class
    """
    def __init__(self, name: str, value, sid=-1):
        if not isinstance(name, str):
            raise TypeError

        self.name = name
        if sid != -1:
            self.value = [value, sid]
        else:
            self.value = [value, "null"]


class Block:
    """
    SB3 Files Block Class
    """
    def __init__(self, sid: str, opcode: str, snext: str, parent: str, inputs: list, fields: list, shadow: str, mutation: list = None, coords: list = None, comment: str = None):
        if mutation is None:
            mutation = []
        if not isinstance(sid, str) or not isinstance(opcode, str) or not isinstance(snext, str) or not isinstance(parent, str) or not isinstance(inputs, list) or not isinstance(fields, list) or not isinstance(shadow, str):
            raise TypeError

        if coords is not None:
            self.x = coords[0]
            self.y = coords[1]
        if comment is not None:
            self.comment = comment
        else:
            self.comment = None
        self.id = sid
        self.opcode = opcode
        self.next = snext
        self.parent = parent
        self.shadow = shadow
        self.inputs = {}
        self.fields = {}
        self.mutation = mutation
        for i in inputs:
            self.inputs[i.name] = [i.shadow, i.value]
        for f in fields:
            self.fields[f.name] = f.value
        if self.parent != "null":
            self.topLevel = "false"
        else:
            self.topLevel = "true"
        if not self.mutation:
            self.tagName = "mutation"
            self.children = []
            if self.opcode == "procedures_prototype" or self.opcode == "procedures_call":
                self.procode = f"{mutation[0]} {mutation[1]}"
                self.argumentids = mutation[2]
                self.warp = mutation[3]
            if self.opcode == "procedures_prototype":
                self.argumentnames = mutation[4]
                self.argumentdefaults = mutation[5]
            if self.opcode == "control_stop":
                self.hasnext = mutation[0]

    def format(self):
        """
        Formats Block Into Dict
        """
        formattedBlock = {}
        if self.opcode != "procedures_prototype" or self.opcode != "procedures_call" or self.opcode != "control_stop":
            formattedBlock = {
                "opcode": self.opcode,
                "next": self.next,
                "parent": self.parent,
                "inputs": self.inputs,
                "fields": self.fields,
                "shadow": self.shadow,
                "topLevel": self.topLevel
            }
        elif self.opcode == "procedures_prototype":
            formattedBlock = {
                "opcode": self.opcode,
                "next": self.next,
                "parent": self.parent,
                "inputs": self.inputs,
                "fields": self.fields,
                "shadow": self.shadow,
                "topLevel": self.topLevel,
                "mutation": {
                    "tagName": self.tagName,
                    "children": self.children,
                    "proccode": self.procode,
                    "argumentids": self.argumentids,
                    "argumentnames": self.argumentnames,
                    "argumentdefaults": self.argumentdefaults,
                    "warp": self.warp
                }

            }
        elif self.opcode == "procedures_call":
            formattedBlock = {
                "opcode": self.opcode,
                "next": self.next,
                "parent": self.parent,
                "inputs": self.inputs,
                "fields": self.fields,
                "shadow": self.shadow,
                "topLevel": self.topLevel,
                "mutation": {
                    "tagName": self.tagName,
                    "children": self.children,
                    "proccode": self.procode,
                    "argumentids": self.argumentids,
                    "warp": self.warp
                }
            }
        elif self.opcode == "control_stop":
            formattedBlock = {
                "opcode": self.opcode,
                "next": self.next,
                "parent": self.parent,
                "inputs": self.inputs,
                "fields": self.fields,
                "shadow": self.shadow,
                "topLevel": self.topLevel,
                "mutation": {
                    "tagName": self.tagName,
                    "children": self.children,
                    "hasnext": self.hasnext
                }
            }
        if self.topLevel == "true":
            formattedBlock["x"] = self.x
            formattedBlock["y"] = self.y
        if self.comment is not None:
            formattedBlock["comment"] = self.comment

        return formattedBlock

    def __str__(self):
        pass


class Costume:
    """
    SB3 Files Costume Class
    """
    def __init__(self, name: str, fileName: str, rotationCenterX, rotationCenterY, bitmapResolution: int = 1):
        if not isinstance(name, str) or not isinstance(fileName, str) or not isinstance(bitmapResolution, int):
            raise TypeError

        self.bitmapResolution = bitmapResolution
        self.name = name
        md5a = md5(fileName)
        self.dataFormat = md5a[1]
        self.assetId = md5a[0]
        self.md5ext = f"{md5a[0]}.{md5a[1]}"
        self.rotationCenterX = rotationCenterX
        self.rotationCenterY = rotationCenterY

    def format(self):
        return {"name": self.name,
                "dataFormat": self.dataFormat,
                "assetId": self.assetId,
                "md5ext": self.md5ext,
                "rotationCenterX": self.rotationCenterX,
                "rotationCenterY": self.rotationCenterY
        }


class Sound:
    """
    SB3 Files Sound Class
    """
    def __init__(self, name: str, fileName: str, rate: int, sampleCount: int, sformat: str):
        if not isinstance(name, str) or not isinstance(fileName, str) or not isinstance(rate, int) or not isinstance(sampleCount, int) or not isinstance(sformat, str):
            raise TypeError

        self.name = name
        md5a = md5(fileName)
        self.assetId = md5a[0]
        self.dataFormat = md5a[1]
        self.sformat = sformat
        self.rate = rate
        self.sampleCount = sampleCount
        self.md5ext = f"{md5a[0]}.{md5a[1]}"

    def format(self):
        return {
          "name": self.name,
          "assetId": self.assetId,
          "dataFormat": self.dataFormat,
          "format": self.sformat,
          "rate": self.rate,
          "sampleCount": self.sampleCount,
          "md5ext": self.md5ext
        }


class Project:
    """
    SB3 Files Project Class
    """
    def __init__(self, targets: Targets, monitors: Monitors, meta: Meta):
        if not isinstance(targets, Targets) or not isinstance(monitors, Monitors) or not isinstance(meta, Meta):
            raise TypeError

        self.targets = targets
        self.monitors = monitors
        self.meta = meta

    def format(self):
        return {
            "targets": self.targets.targets,
            "monitors": self.monitors.monitors,
            "extensions": [],
            "meta": self.meta.format()
        }
