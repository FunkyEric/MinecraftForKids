import mcpi.minecraft as minecraft
import minecraftstuff as stuff
import time


class Player:
    def __init__(self, name, ip='192.168.1.129', ):
        self.server = minecraft.Minecraft.create(ip)
        self.id = self.server.getPlayerEntityId(name)
        self.pos = self.get_pos()

    def get_pos(self):
        self.pos = self.server.entity.getTilePos(self.id)
        return self.pos

    def set_pos(self, pos):
        self.server.entity.setTilePos(self.id, *pos)

    def protect(self):
        pos = self.get_pos()
        self.server.setBlocks(pos.x-1, pos.y-1, pos.z-1, pos.x+1, pos.y+2, pos.z+1, 20)
        self.server.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y+1, pos.z, 0)

    def tower(self):
        pos = self.get_pos()
        for i in range(16):
            self.server.setBlocks(pos.x-2, pos.y+i, pos.z-2, pos.x+2, pos.y+i, pos.z+2, 45)
            if i == 15:
                self.server.setBlocks(pos.x - 2, pos.y + 15, pos.z - 2, pos.x + 2, pos.y + 15, pos.z + 2, 85)
            if i != 14:
                self.server.setBlocks(pos.x-1, pos.y+i, pos.z-1, pos.x+1, pos.y+i, pos.z+1, 0)

            self.server.setBlock(pos.x, pos.y+i, pos.z+1, 65)
        self.server.entity.setPos(self.id, pos.x, pos.y+15, pos.z)

    def build_wall(self):
        build_range = []
        self.server.postToChat('Start to build...')
        while True:
            for event in self.server.events.pollBlockHits():
                if event.entityId == self.id:
                    build_range.append(event.pos)
                if len(build_range) == 2:
                    block_type = self.server.getBlock(*build_range[1])
                    self.server.setBlocks(*build_range[0], *build_range[1], block_type)
                    return

    def clear_wall(self):
        clear_range = []
        self.server.postToChat('Start to clear...')
        while True:
            for event in self.server.events.pollBlockHits():
                if event.entityId == self.id:
                    clear_range.append(event.pos)
                if len(clear_range) == 2:
                    self.server.setBlocks(*clear_range[0], *clear_range[1], 0)
                    return

    def fast_leaves(self):
        t = time.time()
        while True:
            pos = self.get_pos()
            self.server.setBlock(pos.x, pos.y-1, pos.z, 161)
            if time.time() - t > 10:
                return

    def fall_water(self):
        while True:
            pos = self.get_pos()
            block1_type = self.server.getBlock(pos.x, pos.y-1, pos.z)
            block2_type = self.server.getBlock(pos.x, pos.y-15, pos.z)
            if block1_type == 0 and block2_type != 0:
                self.server.postToChat('dangerous！！！')
                self.server.setBlock(pos.x, pos.y-6, pos.z, 8)
                return

    def side_build(self):
        while True:
            for event in self.server.events.pollBlockHits():
                if event.entityId == self.id:
                    if event.face == 4 or event.face == 5:
                        self.server.setBlock(event.pos.x, event.pos.y - 2, event.pos.z-1, 161)
                        self.server.setBlock(event.pos.x, event.pos.y-2, event.pos.z+1, 161)

                    if event.face == 2 or event.face == 3:
                        self.server.setBlock(event.pos.x + 1, event.pos.y - 2, event.pos.z, 161)
                        self.server.setBlock(event.pos.x - 1, event.pos.y - 2, event.pos.z, 161)
            for event in self.server.events.pollChatPosts():
                if event.entityId == self.id:
                    if event.message == 'stop':
                        return

    def test(self):
        pass

    def build_qrcode(self):
        import qrcode
        import easygui
        image = qrcode.QRCode()
        image.add_data(easygui.enterbox('input your content:'))
        qr_list = image.get_matrix()

        pos = self.get_pos()
        X = pos.x
        Y = pos.y
        for row in qr_list:
            for col in row:
                time.sleep(0)
                if col == 0:
                    self.server.setBlock(X, Y, pos.z, 80)
                if col == 1:
                    self.server.setBlock(X, Y, pos.z, 49)
                X += 1
            Y += 1
            X = pos.x

    def prison(self):
        while True:
            pos = self.get_pos()
            self.server.setBlocks(pos.x-2, pos.y-1, pos.z-2,
                                  pos.x+2, pos.y+3, pos.z+2, 1)
            self.server.setBlocks(pos.x-2, pos.y, pos.z-2,
                                  pos.x+2, pos.y+2, pos.z+2, 0)
            self.server.setBlocks(pos.x-2, pos.y, pos.z-2,
                                  pos.x-2, pos.y+2, pos.z-2, 188)
            self.server.setBlocks(pos.x-2, pos.y, pos.z+2,
                                  pos.x-2, pos.y+2, pos.z+2, 188)
            self.server.setBlocks(pos.x+2, pos.y, pos.z-2,
                                  pos.x+2, pos.y+2, pos.z-2, 188)
            self.server.setBlocks(pos.x+2, pos.y, pos.z+2,
                                  pos.x+2, pos.y+2, pos.z+2, 188)
            # self.server.setBlock(pos.x, pos.y, pos.z, 27)
            for event in self.server.events.pollChatPosts():
                if event.entityId == self.id:
                    if event.message == 'stop':
                        return