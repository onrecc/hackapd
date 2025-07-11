from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC_A, KC_B, KC_C, KC_D, KC_VOLU, KC_VOLD
from kmk.extensions.rotary_encoder import RotaryEncoderExtension

import board

keyboard = KMKKeyboard()

# Direct pin mapping for individual switches
keyboard.direct_pins = [
    [board.GP1,  board.GP2],   # SW1, SW2
    [board.GP4,  board.GP3],   # SW3, SW4
]

keyboard.keymap = [
  [KC_A, KC_B],
  [KC_C, KC_D],
]

rotary_ext = RotaryEncoderExtension()
rotary_ext.pins = ((board.GP26, board.GP27),)
rotary_ext.resolutions = (4,)

rotary_ext.callbacks = {0: (KC_VOLU, KC_VOLD)}
keyboard.extensions.append(rotary_ext)

if __name__ == "__main__":
  keyboard.go()