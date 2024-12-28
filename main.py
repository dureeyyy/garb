from car import Car
from player import Player
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor
from panda3d.core import Texture, TextureStage, Filename, Loader


app = Ursina()

plane = Entity(model="plane",
               texture ="grass",
               scale=(100, 1, 100),
               collider = "box")

player = FirstPersonController(model="assets/characters/main/idle-anims/model.obj",
                               texture = "assets/characters/main/idle-anims/texture.png",
                               scale = 1,
                               collider = "box")

player.speed = 10
camera.z =-10

actor = Actor('assets/characters/main/animations/idle/idle.gltf', {
    'running' :'assets/characters/main/animations/running/running.gltf',
    'idle': 'assets/characters/main/animations/idle/idle.gltf',
    'jumping': 'assets/characters/main/animations/jumping/jumping.gltf',
    'running-jumping': 'assets/characters/main/animations/running jumping/running-jump.gltf'
})

# texture = loader.loadTexture("assets/characters/main/idle-anims/texture.png")

actor.reparent_to(player)
actor.setH(actor, 90)
# actor.setTexture(texture)

sky = Sky(texture="sky_sunrise")

# Define animation control
def update():
    
    if held_keys['w']:
        actor.show()
        player.model.hide()
        if actor.getCurrentAnim() != 'running':  # Avoid restarting the animation if it's already playing
            actor.loop('running', fromFrame=0, toFrame=22)

    elif held_keys['space']:
        actor.show()
        player.model.hide()
        if actor.getCurrentAnim() != 'jumping':  # Avoid restarting the animation if it's already playing
            actor.loop('jumping', fromFrame=0, toFrame=22)

    else:
        actor.hide()
        player.model.show()
        # if actor.getCurrentAnim():  # Avoid restarting the animation if it's already playing
        #     actor.loop('idle', fromFrame=0, toFrame=30)

app.run() 