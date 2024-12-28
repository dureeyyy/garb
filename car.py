from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Car(FirstPersonController):
    def __init__(self, 
                 position = (0, 0, 0), 
                 rotation = (0, 0, 0), 
                 topspeed = 30, 
                 acceleration = 0.15, 
                 braking_strength = 30, 
                 friction = 0.6, 
                 camera_speed = 8, 
                 drift_speed = 35):
        super().__init__(
            model = "boy-main.obj",
            texture = "man-main.png",
            position = position,
            rotation = rotation,
        )

        

        self._collider = "box"
        self.speed = 0              # Current forward speed
        self.acceleration = 0.05    # Rate of speed increase
        self.friction = 0.98        # Rate of speed decay
        self.max_speed = 2          # Maximum forward speed
        self.steering = 0           # Steering angle
        self.turn_speed = 1         # Rate of steering
        self.rotation_sensitivity = 3
        self.scale = 1 
        # self.animation = FrameAnimation3d(
        #     "running.obj",  # Animation file
        #     fps=30,
        #     position=self.position,
        #     scale=20,
        #     visible=False  # Hide animation by default
        # )

    

    def update(self):
        # --- Forward and Reverse ---
        if held_keys['w']:
            self.speed += self.acceleration
            self.position += self.forward * self.speed

            # Play animation when moving forward
            # self.animation.visible = True
            # self.animation.position = self.position 
        elif held_keys['s']:
            # self.animation.visible = False
            self.speed -= self.acceleration  # Accelerate backward

        # Limit the speed to max_speed
        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))

        # Apply friction
        self.speed *= self.friction

        # --- Steering ---
        if held_keys['a']:
            self.steering -= self.turn_speed * time.dt
        elif held_keys['d']:
            self.steering += self.turn_speed * time.dt
        else:
            self.steering *= 0.9  # Gradually straighten the steering

        # Clamp the steering to prevent oversteering
        self.steering = max(-1, min(self.steering, 1))

        # --- Move and Rotate ---
        # Move forward in the direction the car is facing
        self.rotation_y += self.steering * self.rotation_sensitivity * self.speed
        self.position += self.forward * self.speed

        plane_size = 100  # Half the width/length of the plane
        self.position = Vec3(
            clamp(self.position.x, -plane_size, plane_size),
            self.position.y,
            clamp(self.position.z, -plane_size, plane_size)
        )
        