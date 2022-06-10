import pygame


class Object:
    def __init__(self, root, name_image: str, name_id: str, position_x: int, position_y: int, height: int, width: int,
                 speed: float, collision):
        self.root = root
        self.name_image = name_image
        self.name_id = name_id
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.speed = speed
        self.collision = collision

        self.object_image = None

        self.set_object_image()

    def set_object_image(self):
        prefix = str.lower(self.name_image)
        # create and resize image
        self.object_image = pygame.image.load("asset/image/"+prefix+".png")
        self.object_image = pygame.transform.scale(self.object_image, (self.width, self.height))
        # draw the object in the root
        self.draw()

    def draw(self):
        # draw the rect using the position x, y, width, height
        pygame.draw.rect(self.root, (0, 0, 0), (self.position_x, self.position_y, self.width, self.height), 1)
        # scale image
        self.object_image = pygame.transform.scale(self.object_image, (self.width, self.height))
        # draw the image using the position x, y
        self.root.blit(self.object_image, (self.position_x, self.position_y))
