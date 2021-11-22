# APCJ40_MKII

A custom remote script for the APC40 MKII for Ableton Live 11. 

So far the only changes are: 

- nudge + copies a clip 
- nudge - deletes a clip 
- shift + nudge now nudges 

Changes to come: 

- User Mode is a Step Sequencer 

You can download the Step Sequencer Edition in the step-sequencer Branch
 
Bugs with Step Sequencer: 

- Pad buttons are always lit upon disconnect (the issue is the custom make_button in ControlElementUtils)
- Playhead isn't working
- Starts on wrong grid size or wrong clip size 
- Loop selectors select a loop, they should navigate and extend the clip in my opinion
- Note repeat is always engaged (it's been disabled)

Special Thanks to: 

gluon: https://github.com/gluon/AbletonLive11_MIDIRemoteScripts

xnamanahx: https://github.com/xnamahx/APC40_MkIIx

cylab: https://github.com/cylab/APCequencer

martinpechmann: https://github.com/martinpechmann/APC400000


