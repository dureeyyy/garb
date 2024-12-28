from ursina import *

class Player(Entity):
    def __init__(self,
                 model,
                 texture,
                 origin, 
                 position,
                 parent,
                 scale): 
        super().__init__(
            model = model,
            texture = texture,
            origin = origin,
            position = position,
            parent = parent,
            scale = scale
        )

        

    def update(self):
        plane_size = 100  # Half the width/length of the plane
        
        self.position = Vec3(
            clamp(self.position.x, -plane_size, plane_size),
            self.position.y,
            clamp(self.position.z, -plane_size, plane_size)
        )
        
       
        
