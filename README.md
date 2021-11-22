# APCJ40_MKII
by chris joseph

A custom remote script for the APC40 MKII for Ableton Live 11. 

Changes:

- nudge + + copies a clip 
- nudge + - deletes a clip 
- shift + nudge now nudges 

Planned Changes: 

- shift + bank turns on VU meters 
- user mode is a step sequencer
- shift + clip view is undo 
- shift + detail view is redo 
- shift + record is capture midi
- press and hold select clip to expand or collapse a group


You can download the Step Sequencer Edition in the step-sequencer Branch
 
Bugs with Step Sequencer: 

- Velocity slider doesn't work (it doesn't play the note at that velocity, but it sequences it at it) 
- Pads are always lit upon disconnect, velocity slider pads always lit (issue is with the make_button command ControlElementUtils.py)
- Note repeat is always engaged (it's been disabled)
- Nudge isn't working 
- Undo and Redo isn't working
- The loop selector isn't working 
- the Playhead isn't showing up
- In NoteEditorComponent and APCNoteEditorComponent the tuple (x, y) isn't handled properly 

Special Thanks to: 

gluon: https://github.com/gluon/AbletonLive11_MIDIRemoteScripts

xnamanahx: https://github.com/xnamahx/APC40_MkIIx

cylab: https://github.com/cylab/APCequencer

martinpechmann: https://github.com/martinpechmann/APC400000

hanzpetrov: http://remotescripts.blogspot.com/p/apc-64-40.html

fabriziopoce: https://github.com/matthewcieplak/APC_64_40_9l  

willmarshall: https://github.com/willrjmarshall/AbletonDJTemplateUnsupported
